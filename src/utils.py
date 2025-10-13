"""
Utility functions for Road Accident Risk Prediction
"""

import pandas as pd
import numpy as np
from typing import Tuple, List
from sklearn.preprocessing import LabelEncoder


def load_data(data_dir: str = "../playground-series-s5e10") -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load train, test, and sample submission data.
    
    Args:
        data_dir: Path to data directory
        
    Returns:
        Tuple of (train_df, test_df, sample_submission)
    """
    train_df = pd.read_csv(f"{data_dir}/train.csv")
    test_df = pd.read_csv(f"{data_dir}/test.csv")
    sample_submission = pd.read_csv(f"{data_dir}/sample_submission.csv")
    
    return train_df, test_df, sample_submission


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create advanced features for the model.
    
    Args:
        df: Input dataframe
        
    Returns:
        DataFrame with additional features
    """
    df = df.copy()
    
    # Interaction features
    df['speed_per_lane'] = df['speed_limit'] / df['num_lanes']
    df['curvature_speed'] = df['curvature'] * df['speed_limit']
    df['accidents_per_lane'] = df['num_reported_accidents'] / df['num_lanes']
    
    # Boolean combinations
    df['risky_conditions'] = (
        (df['weather'] == 'rainy') & 
        (df['lighting'] == 'dim')
    ).astype(int)
    
    df['peak_holiday'] = (
        (df['holiday'] == True) & 
        (df['time_of_day'].isin(['evening', 'afternoon']))
    ).astype(int)
    
    df['school_morning'] = (
        (df['school_season'] == True) & 
        (df['time_of_day'] == 'morning')
    ).astype(int)
    
    # Risk score combinations
    df['high_speed_curve'] = (
        (df['speed_limit'] > 50) & 
        (df['curvature'] > 0.5)
    ).astype(int)
    
    df['no_signs_bad_weather'] = (
        (df['road_signs_present'] == False) & 
        (df['weather'] != 'clear')
    ).astype(int)
    
    # Polynomial features
    df['curvature_squared'] = df['curvature'] ** 2
    df['speed_squared'] = df['speed_limit'] ** 2
    df['accidents_squared'] = df['num_reported_accidents'] ** 2
    
    # Binned features
    df['speed_category'] = pd.cut(
        df['speed_limit'], 
        bins=[0, 35, 50, 70], 
        labels=['low', 'medium', 'high']
    )
    
    df['curvature_category'] = pd.cut(
        df['curvature'], 
        bins=[0, 0.33, 0.66, 1.0], 
        labels=['straight', 'moderate', 'sharp']
    )
    
    # Combined categorical features
    df['road_weather'] = df['road_type'] + '_' + df['weather']
    df['road_lighting'] = df['road_type'] + '_' + df['lighting']
    df['weather_time'] = df['weather'] + '_' + df['time_of_day']
    
    return df


def encode_categoricals(
    train: pd.DataFrame, 
    test: pd.DataFrame, 
    cat_cols: List[str]
) -> Tuple[pd.DataFrame, pd.DataFrame, dict]:
    """
    Label encode categorical features.
    
    Args:
        train: Training dataframe
        test: Test dataframe
        cat_cols: List of categorical column names
        
    Returns:
        Tuple of (encoded_train, encoded_test, encoders_dict)
    """
    train_encoded = train.copy()
    test_encoded = test.copy()
    
    encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        train_encoded[col] = le.fit_transform(train[col].astype(str))
        test_encoded[col] = le.transform(test[col].astype(str))
        encoders[col] = le
    
    return train_encoded, test_encoded, encoders


def get_feature_columns() -> Tuple[List[str], List[str]]:
    """
    Get lists of feature columns.
    
    Returns:
        Tuple of (all_features, categorical_features)
    """
    categorical_cols = [
        'road_type', 'lighting', 'weather', 'road_signs_present',
        'public_road', 'time_of_day', 'holiday', 'school_season',
        'speed_category', 'curvature_category',
        'road_weather', 'road_lighting', 'weather_time'
    ]
    
    return categorical_cols


def clip_predictions(predictions: np.ndarray, min_val: float = 0.0, max_val: float = 1.0) -> np.ndarray:
    """
    Clip predictions to valid range.
    
    Args:
        predictions: Array of predictions
        min_val: Minimum valid value
        max_val: Maximum valid value
        
    Returns:
        Clipped predictions
    """
    return np.clip(predictions, min_val, max_val)
