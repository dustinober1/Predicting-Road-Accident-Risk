#!/bin/bash

# Road Accident Risk Prediction - Environment Setup Script
# This script activates the virtual environment and provides helpful information

echo "🚗 Road Accident Risk Prediction - Environment Setup"
echo "=================================================="

# Check if we're in the right directory
if [ ! -d ".venv" ]; then
    echo "❌ Error: Virtual environment not found!"
    echo "   Please run: python -m venv .venv"
    echo "   Then install dependencies: pip install -r requirements.txt"
    exit 1
fi

# Check if virtual environment is already activated
if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ Virtual environment already activated: $VIRTUAL_ENV"
else
    echo "🔄 Activating virtual environment..."
    source .venv/bin/activate

    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment activated successfully!"
        echo "   Python: $(python --version)"
        echo "   Location: $VIRTUAL_ENV"
    else
        echo "❌ Failed to activate virtual environment"
        exit 1
    fi
fi

echo ""
echo "📁 Project Structure:"
echo "   ├── notebooks/road_accident_risk_prediction.ipynb  # Main notebook"
echo "   ├── playground-series-s5e10/                      # Competition data"
echo "   ├── docs/                                         # Documentation"
echo "   ├── src/                                          # Source code"
echo "   └── submission.csv                                # Generated predictions"
echo ""
echo "🚀 Quick Commands:"
echo "   jupyter notebook                                  # Launch Jupyter"
echo "   python src/make_submission_backup.py              # Run legacy script"
echo "   pip install -r requirements.txt                    # Install dependencies"
echo ""
echo "📊 Competition Info:"
echo "   Goal: Predict accident risk (0-1) with RMSE < 0.05"
echo "   Data: playground-series-s5e10/"
echo "   Models: CatBoost, XGBoost, LightGBM ensemble"
echo ""
#!/bin/bash

# Road Accident Risk Prediction - Environment Setup Script
# This script activates the virtual environment and provides helpful information

echo "🚗 Road Accident Risk Prediction - Environment Setup"
echo "=================================================="

# Check if we're in the right directory
if [ ! -d ".venv" ]; then
    echo "❌ Error: Virtual environment not found!"
    echo "   Please run: python -m venv .venv"
    echo "   Then install dependencies: pip install -r requirements.txt"
    exit 1
fi

# Check if virtual environment is already activated
if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ Virtual environment already activated: $VIRTUAL_ENV"
else
    echo "🔄 Activating virtual environment..."
    source .venv/bin/activate

    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment activated successfully!"
        echo "   Python: $(python --version)"
        echo "   Location: $VIRTUAL_ENV"
    else
        echo "❌ Failed to activate virtual environment"
        exit 1
    fi
fi

echo ""
echo "📁 Project Structure:"
echo "   ├── notebooks/road_accident_risk_prediction.ipynb  # Main notebook"
echo "   ├── playground-series-s5e10/                      # Competition data"
echo "   ├── docs/                                         # Documentation"
echo "   ├── src/                                          # Source code"
echo "   └── submission.csv                                # Generated predictions"
echo ""
echo "🚀 Quick Commands:"
echo "   jupyter notebook                                  # Launch Jupyter"
echo "   python src/make_submission_backup.py              # Run legacy script"
echo "   pip install -r requirements.txt                    # Install dependencies"
echo ""
echo "📊 Competition Info:"
echo "   Goal: Predict accident risk (0-1) with RMSE < 0.05"
echo "   Data: playground-series-s5e10/"
echo "   Models: CatBoost, XGBoost, LightGBM ensemble"
echo ""
echo "🎯 Ready to start! Open notebooks/road_accident_risk_prediction.ipynb"
echo "=================================================="

# Optional: Show current status
echo ""
echo "💡 Tip: Run 'jupyter notebook' to start working!"
echo "=================================================="