# Predicting Road Accident Risk 🚗💥

**Kaggle Playground Series - Season 5, Episode 10**

[![Competition](https://img.shields.io/badge/Kaggle-Competition-20BEFF?logo=kaggle)](https://kaggle.com/competitions/playground-series-s5e10)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Overview

This repository contains a machine learning solution for predicting road accident risk on different types of roads. The competition uses **Root Mean Squared Error (RMSE)** as the evaluation metric, and our goal is to achieve a score below **0.05**.

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
│   └── road_accident_risk_prediction.ipynb  # Main modeling notebook
├── playground-series-s5e10/       # Competition data
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   └── sample_submission.csv      # Submission format
├── src/                           # Source code (if needed)
├── .gitignore                     # Git ignore file
├── README.md                      # This file
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
   .venv\Scripts\activate

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

### Running the Jupyter Notebook

1. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook:**
   - Navigate to `notebooks/road_accident_risk_prediction.ipynb`
   - Run all cells to train models and generate predictions

3. **The notebook includes:**
   - Data loading and exploration
   - Feature engineering (27 features)
   - Training 3 models: CatBoost, XGBoost, LightGBM
   - 5-fold cross-validation with tqdm progress tracking
   - Ensemble predictions with optimal weighting
   - Comprehensive visualizations

### Output

The notebook generates:
- `submission.csv` - Ready to submit to Kaggle
- Model performance metrics and visualizations
- Feature importance analysis

## 🎯 Methodology

### Feature Engineering
- **Interaction features:** speed_per_lane, curvature_speed, accidents_per_lane
- **Boolean combinations:** risky_conditions, peak_holiday, school_morning
- **Risk indicators:** high_speed_curve, no_signs_bad_weather
- **Polynomial features:** curvature_squared, speed_squared, accidents_squared
- **Categorical combinations:** road_weather, road_lighting, weather_time
- **Binned features:** speed_category, curvature_category

### Model Ensemble
1. **CatBoost Regressor** - Handles categorical features natively
2. **XGBoost Regressor** - Gradient boosting with regularization
3. **LightGBM Regressor** - Fast gradient boosting framework

### Training Strategy
- 5-fold cross-validation
- Early stopping to prevent overfitting
- Weighted ensemble averaging
- Progress tracking with tqdm

## 📊 Results

| Model | CV RMSE |
|-------|---------|
| CatBoost | TBD |
| XGBoost | TBD |
| LightGBM | TBD |
| **Ensemble** | **Target: < 0.05** |

*Run the notebook to see actual scores*

## 🔧 Customization

To improve performance:

1. **Hyperparameter tuning:**
   - Adjust `iterations`, `learning_rate`, `depth` for each model
   - Use Optuna or GridSearchCV for automated tuning

2. **Additional features:**
   - Add more interaction terms
   - Create aggregated statistics
   - Include the original dataset for training

3. **Advanced ensembling:**
   - Stack predictions with meta-learner
   - Use blending techniques
   - Try different weight optimization methods

## 📈 Monitoring Progress

The notebook uses `tqdm` for real-time progress tracking:
- Training progress for each fold
- Model-by-model training updates
- Clear visualization of CV scores

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

*Last updated: October 13, 2025*
