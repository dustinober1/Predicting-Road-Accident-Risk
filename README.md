# Predicting Road Accident Risk 🚗💥

**Kaggle Playground Series - Season 5, Episode 10**

[![Competition](https://img.shields.io/badge/Kaggle-Competition-20BEFF?logo=kaggle)](https://kaggle.com/competitions/playground-series-s5e10)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Overview

This repository contains an advanced machine learning solution for predicting road accident risk on different types of roads. The competition uses **Root Mean Squared Error (RMSE)** as the evaluation metric, and our goal is to achieve a score below **0.05**.

### Competition Details
- **Goal:** Predict accident risk (0-1 continuous value) for different road configurations
- **Evaluation Metric:** RMSE (Root Mean Squared Error)
- **Dataset:** Synthetically generated from real-world road accident data
- **Timeline:** October 1 - October 31, 2025

## 🗂️ Project Structure

```
Predicting-Road-Accident-Risk/
├── docs/                           # Competition documentation
│   ├── Comp.md                    # Competition rules and overview
│   └── data.md                    # Dataset description
├── notebooks/                      # Jupyter notebooks
│   ├── road_accident_risk_prediction.ipynb  # Original modeling notebook
│   └── road_accident_risk_improved.ipynb    # Enhanced modeling notebook
├── playground-series-s5e10/       # Competition data
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   └── sample_submission.csv      # Submission format
├── src/                           # Source code (if needed)
├── .gitignore                     # Git ignore file
├── README.md                      # This file
├── requirements.txt               # Dependencies
└── submission.csv                 # Generated submission file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dustinober1/Predicting-Road-Accident-Risk.git
   cd Predicting-Road-Accident-Risk
   ```

2. **Activate the environment:**
   ```bash
   ./activate.sh
   ```
   *This script will activate the virtual environment and show helpful information.*

3. **Or set up manually:**
   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate it
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   .venv\\Scripts\\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Download competition data:**
   - Place `train.csv`, `test.csv`, and `sample_submission.csv` in `playground-series-s5e10/` folder
   - Or download via Kaggle API:
     ```bash
     kaggle competitions download -c playground-series-s5e10
     ```

## 💻 Usage

### Running the Jupyter Notebooks

1. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open the notebooks:**
   - Navigate to `notebooks/road_accident_risk_improved.ipynb` (recommended)
   - Or `notebooks/road_accident_risk_prediction.ipynb` (original)

3. **The improved notebook includes:**
   - Enhanced data loading and exploration
   - Advanced feature engineering (39+ features)
   - Training 3 optimized models: CatBoost, XGBoost, LightGBM
   - 5-fold cross-validation with tqdm progress tracking
   - Ensemble predictions with optimal weighting
   - Advanced stacking techniques
   - Comprehensive visualizations and analysis

### Output

The notebook generates:
- `submission.csv` - Ready to submit to Kaggle
- Model performance metrics and visualizations
- Feature importance analysis
- Residual analysis and model comparison plots

## 🎯 Methodology

### Enhanced Feature Engineering
- **Interaction features:** speed_per_lane, curvature_speed, accidents_per_lane
- **Boolean combinations:** risky_conditions, peak_holiday, school_morning
- **Risk indicators:** high_speed_curve, no_signs_bad_weather, high_risk_combo
- **Polynomial features:** curvature_squared, speed_squared, accidents_squared
- **Categorical combinations:** road_weather, road_lighting, weather_time, lighting_weather
- **Binned features:** speed_category, curvature_category
- **Statistical aggregations:** accidents_log, curvature_log
- **Advanced interactions:** speed_to_curvature_ratio, lanes_times_weather, lighting_times_weather

### Optimized Model Ensemble
1. **CatBoost Regressor** - Handles categorical features natively with optimized parameters
2. **XGBoost Regressor** - Gradient boosting with regularization and early stopping
3. **LightGBM Regressor** - Fast gradient boosting framework with optimized parameters

### Advanced Training Strategy
- 5-fold cross-validation with stratified splits
- Early stopping to prevent overfitting
- Hyperparameter optimization for each model
- Weighted ensemble averaging with best weight combinations
- Advanced stacking with meta-features
- Progress tracking with tqdm

## 📊 Results

| Model | CV RMSE |
|-------|---------|
| CatBoost | 0.05611 |
| XGBoost | 0.05605 |
| LightGBM | 0.05605 |
| **Ensemble** | **0.05603** |

*Best ensemble uses weights: (0.33, 0.33, 0.34) for CatBoost, XGBoost, LightGBM respectively*

## 🔧 Customization

To further improve performance:

1. **Hyperparameter tuning:**
   - Use Optuna or GridSearchCV for automated tuning
   - Experiment with different regularization parameters
   - Adjust learning rates and tree depths

2. **Additional features:**
   - Add more domain-specific interaction terms
   - Create time-based or geographic aggregations
   - Include external data sources if available

3. **Advanced ensembling:**
   - Try different meta-learners (Neural Networks, Random Forest)
   - Implement blending techniques
   - Use different cross-validation strategies

4. **Model Architecture:**
   - Try Neural Networks or TabNet
   - Implement more complex stacking layers
   - Experiment with model-specific feature selection

## 📈 Monitoring Progress

The notebook uses `tqdm` for real-time progress tracking:
- Training progress for each fold
- Model-by-model training updates
- Clear visualization of CV scores
- Fold-wise performance analysis

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kaggle** for hosting the Playground Series competition
- **Competition Dataset:** Derived from [Simulated Roads Accident Data](https://www.kaggle.com/datasets/ianktoo/simulated-roads-accident-data/)
- All contributors and the ML community

## 📧 Contact

**Dustin Ober**
- GitHub: [@dustinober1](https://github.com/dustinober1)
- Competition: [Kaggle Profile](https://www.kaggle.com/)

---

⭐ If you find this helpful, please star the repository!

*Last updated: October 19, 2025*