# Quick Start Guide

## Setting Up the Environment

### 1. Clone and Navigate
```bash
git clone https://github.com/dustinober1/Predicting-Road-Accident-Risk.git
cd Predicting-Road-Accident-Risk
```

### 2. Activate Environment (One Command!)
```bash
./activate.sh
```
*This script automatically activates the virtual environment and shows helpful project information!*

### 3. Or Manual Setup
If you prefer manual setup:
```bash
# Create virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Download Competition Data
Place the following files in `playground-series-s5e10/` folder:
- `train.csv`
- `test.csv`
- `sample_submission.csv`

Or use Kaggle API:
```bash
kaggle competitions download -c playground-series-s5e10
unzip playground-series-s5e10.zip -d playground-series-s5e10/
```

## Running the Solution

### Option 1: Jupyter Notebook (Recommended)
```bash
# Start Jupyter
jupyter notebook

# Open: notebooks/road_accident_risk_prediction.ipynb
# Run all cells (Cell -> Run All)
```

### Option 2: Python Script (Legacy)
```bash
python src/make_submission_backup.py
```

## What to Expect

The notebook will:
1. ✅ Load and explore data
2. ✅ Create 27 engineered features
3. ✅ Train 3 models (CatBoost, XGBoost, LightGBM) with progress bars
4. ✅ Perform 5-fold cross-validation
5. ✅ Create ensemble predictions
6. ✅ Generate `submission.csv`

**Expected Runtime:** 15-30 minutes (depending on your machine)

## Understanding the Output

### Cross-Validation Scores
```
CatBoost  CV RMSE: 0.0xxx
XGBoost   CV RMSE: 0.0xxx
LightGBM  CV RMSE: 0.0xxx
Ensemble  CV RMSE: 0.0xxx  ← Target: < 0.05
```

### Submission File
- Location: `submission.csv` (root directory)
- Format: Two columns (id, accident_risk)
- Ready to upload to Kaggle!

## Troubleshooting

### Issue: ImportError for LightGBM
**Solution:**
```bash
# On macOS, install libomp:
brew install libomp

# Or use Conda:
conda install -c conda-forge lightgbm
```

### Issue: Jupyter kernel not found
**Solution:**
```bash
python -m ipykernel install --user --name=.venv --display-name="Python (accident-risk)"
```

### Issue: Out of memory
**Solution:**
- Reduce `n_estimators` from 3000 to 1500
- Reduce `N_FOLDS` from 5 to 3

## Next Steps

### If CV Score > 0.05
1. **Hyperparameter Tuning:**
   - Use Optuna for automated search
   - Focus on learning_rate, depth, num_leaves

2. **Additional Features:**
   - Try more interaction terms
   - Add time-based aggregations
   - Include external datasets

3. **Advanced Ensembling:**
   - Stack with meta-learner (Ridge, XGBoost)
   - Try blending strategies
   - Optimize weights with scipy.optimize

### If CV Score < 0.05 ✨
1. Submit to Kaggle!
2. Check leaderboard score
3. If public LB score matches CV → Great model!
4. If public LB score differs → Check for overfitting

## Tips for Best Results

1. **Always track progress:** The notebook uses tqdm for this
2. **Monitor validation scores:** Early stopping prevents overfitting
3. **Experiment with features:** Not all features improve performance
4. **Test ensemble weights:** Try different combinations
5. **Save your models:** Use pickle/joblib for future predictions

## Support

- **Issues:** Open an issue on GitHub
- **Questions:** Check the docs/ folder for competition details
- **Updates:** Star the repo for latest improvements

---

Good luck! 🍀
