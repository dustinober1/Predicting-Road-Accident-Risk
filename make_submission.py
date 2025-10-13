from __future__ import annotations

import pathlib
from typing import List

import numpy as np
import pandas as pd
from catboost import CatBoostRegressor, Pool
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold


def main() -> None:
    data_dir = pathlib.Path("playground-series-s5e10")
    train_path = data_dir / "train.csv"
    test_path = data_dir / "test.csv"
    sample_submission_path = data_dir / "sample_submission.csv"

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    target_col = "accident_risk"
    categorical_cols: List[str] = [
        "road_type",
        "lighting",
        "weather",
        "road_signs_present",
        "public_road",
        "time_of_day",
        "holiday",
        "school_season",
    ]

    for col in categorical_cols:
        train_df[col] = train_df[col].astype("category")
        test_df[col] = test_df[col].astype("category")

    features = [col for col in train_df.columns if col not in {target_col, "id"}]
    X = train_df[features]
    y = train_df[target_col]
    X_test = test_df[features]

    kfold = KFold(n_splits=5, shuffle=True, random_state=42)

    categorical_indices = [features.index(col) for col in categorical_cols]

    oof_predictions = np.zeros(len(train_df))
    test_predictions = np.zeros(len(test_df))

    for fold, (train_idx, valid_idx) in enumerate(kfold.split(X, y), start=1):
        X_train, X_valid = X.iloc[train_idx], X.iloc[valid_idx]
        y_train, y_valid = y.iloc[train_idx], y.iloc[valid_idx]

        train_pool = Pool(X_train, y_train, cat_features=categorical_indices)
        valid_pool = Pool(X_valid, y_valid, cat_features=categorical_indices)
        test_pool = Pool(X_test, cat_features=categorical_indices)

        model = CatBoostRegressor(
            depth=8,
            iterations=3000,
            learning_rate=0.03,
            loss_function="RMSE",
            eval_metric="RMSE",
            subsample=0.8,
            colsample_bylevel=0.8,
            random_seed=fold,
            verbose=False,
        )

        model.fit(train_pool, eval_set=valid_pool, use_best_model=True, early_stopping_rounds=200)

        oof_predictions[valid_idx] = model.predict(valid_pool)
        test_predictions += model.predict(test_pool) / kfold.n_splits

        fold_rmse = mean_squared_error(y_valid, oof_predictions[valid_idx], squared=False)
        print(f"Fold {fold} RMSE: {fold_rmse:.5f}")

    cv_rmse = mean_squared_error(y, oof_predictions, squared=False)
    print(f"CV RMSE: {cv_rmse:.5f}")

    submission_df = pd.read_csv(sample_submission_path)
    submission_df["accident_risk"] = np.clip(test_predictions, 0.0, 1.0)
    output_path = pathlib.Path("submission.csv")
    submission_df.to_csv(output_path, index=False)
    print(f"Saved submission file to {output_path.resolve()}")


if __name__ == "__main__":
    main()
