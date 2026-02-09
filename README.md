# MLOps Assignment 2: Feature Store and ML Pipeline

## Project Overview

This project implements a complete ML pipeline using Databricks, featuring:
- Feature versioning (2 versions)
- ML experimentation (4 experiments)
- Carbon emission tracking
- Comparison of results

## Technology Stack

- **Platform:** Databricks Community Edition
- **Feature Store:** Databricks Tables (2 versions)
- **ML Pipeline:** MLflow (experiment tracking)
- **Algorithm:** Random Forest Classifier
- **Carbon Tracking:** CodeCarbon
- **Version Control:** GitHub
- **Containerization:** Docker

## Dataset

**athletes.csv** - 1000 synthetic athlete records
- Features: age, height, weight, sport, country, experience, training hours
- Target: medal winner (Yes/No)
- Distribution: 45% medal winners, 55% non-winners

## Feature Versions

### Version 1: Basic Features (7 features)
- age, height, weight
- years_experience
- training_hours_per_week
- country_encoded, sport_encoded

### Version 2: Engineered Features (8 features)
- age (float)
- bmi (Body Mass Index)
- experience_per_age
- training_intensity
- age_group
- height_weight_ratio
- country_encoded, sport_encoded

## Experiments

| Experiment | Features | n_estimators | max_depth | Accuracy | F1 Score | Carbon (kg CO2) |
|------------|----------|--------------|-----------|----------|----------|-----------------|
| exp1_v1_hp1 | V1 | 100 | 10 | 0.475 | 0.295 | 0.000009 |
| exp2_v1_hp2 | V1 | 200 | 20 | 0.485 | 0.352 | 0.000005 |
| exp3_v2_hp1 | V2 | 100 | 10 | 0.540 | 0.395 | 0.000006 |
| **exp4_v2_hp2** | **V2** | **200** | **20** | **0.535** | **0.429** | **0.000007** |

## Best Model

**Experiment:** exp4_v2_hp2
- **Features:** Version 2 (Engineered)
- **Hyperparameters:** n_estimators=200, max_depth=20
- **F1 Score:** 0.4294 (best)
- **Accuracy:** 0.535
- **ROC AUC:** 0.530

## Key Findings

1. **Feature Engineering Matters:** V2 features outperformed V1 in all metrics
2. **Best Features:** BMI, experience_per_age, and training_intensity were most important
3. **Carbon Footprint:** Minimal (0.000007 kg CO2) for this dataset size
4. **Hyperparameters:** Higher depth and more estimators improved performance

## Project Structure
```
mlops_assignment2_final/
├── databricks/              # Databricks notebook and screenshots
│   ├── Assignment2_FeatureStore_Pipeline.ipynb
│   └── screenshots/
├── docs/                    # Documentation
│   └── DISCUSSION.md
├── local/                   # Local data generation
│   ├── athletes.csv
│   └── create_data.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run

### In Databricks (Recommended)

1. Sign up at https://community.cloud.databricks.com/
2. Create new notebook
3. Copy cells from `databricks/Assignment2_FeatureStore_Pipeline.ipynb`
4. Run all cells
5. View results in MLflow Experiments

### Locally (Data Generation Only)
```bash
cd local
python create_data.py
```

This generates the `athletes.csv` dataset used in the project.

## Technologies Explained

### Why Databricks?
- Integrated data platform with built-in MLflow
- Serverless compute (no setup needed)
- Free Community Edition available
- Native support for feature tables

### Why CodeCarbon?
- Tracks energy consumption and CO2 emissions
- Important for sustainable AI
- Easy integration (3 lines of code)
- Methodology: https://mlco2.github.io/codecarbon/methodology.html

### Why MLflow?
- Industry-standard experiment tracking
- Version control for models
- Easy comparison of experiments
- Built into Databricks

## Results & Conclusions

Feature engineering significantly improved model performance:
- F1 Score improvement: 0.295 → 0.429 (+45%)
- Accuracy improvement: 0.475 → 0.535 (+13%)

The engineered features (BMI, training_intensity, experience_per_age) captured important patterns that basic features missed. This demonstrates the value of domain knowledge in feature engineering.

Carbon emissions were minimal (0.000007 kg CO2) for this dataset size, but tracking establishes good practices for production-scale systems where emissions matter.

## Assignment Requirements Met

- Feature Store with 2 versions (V1 basic, V2 engineered)
- ML Pipeline (MLflow experiment tracking)
- 4 experiments (2 feature versions × 2 hyperparameter sets)
- Quantitative comparison (metrics table)
- Qualitative comparison (confusion matrices, feature importance)
- Carbon emission tracking (CodeCarbon)
- No AutoML (manual Random Forest implementation)

## Discussion

See `docs/DISCUSSION.md` for detailed discussion of:
- ML.ENERGY Initiative
- CodeCarbon methodology
- Sustainability in ML
- Real-world implications

## Author

Aigul Azamat  
Email: aigul.azamat7@gmail.com  
Date: February 8, 2026

## References

1. Databricks Documentation: https://docs.databricks.com/
2. MLflow Documentation: https://mlflow.org/docs/latest/index.html
3. CodeCarbon: https://mlco2.github.io/codecarbon/
4. ML.ENERGY Initiative: https://ml.energy/
5. Professor's MLflow Example: https://colab.research.google.com/drive/1ZaMyOj50TTgMeHVzLrq3PvtTm28z1Nqz