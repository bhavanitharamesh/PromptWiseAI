"""
=========================================
PromptWise AI
Task → Context Mapping
=========================================

This module maps each task to realistic
business scenarios (contexts).

These contexts are used while generating
synthetic datasets and final prompts.

Used in:
- Dataset Generation
- Prompt Builder
- NLP Pipeline
"""
CONTEXT_MAPPING = {    "Analyze Dataset": [
        "E-commerce customer purchase dataset",
        "Hospital patient records",
        "Bank transaction dataset",
        "Telecom customer dataset",
        "Retail sales dataset"
    ],

    "Perform Exploratory Data Analysis": [
        "Customer churn dataset",
        "House price prediction dataset",
        "Movie recommendation dataset",
        "Employee attrition dataset",
        "Healthcare analytics dataset"
    ],

    "Build Machine Learning Model": [
        "Credit card fraud detection",
        "Skin care recommendation system",
        "Loan approval prediction",
        "Spam email detection",
        "Disease prediction system"
    ],

    "Feature Engineering": [
        "Insurance claim prediction",
        "Sales forecasting dataset",
        "Product recommendation dataset",
        "Student performance dataset",
        "Customer segmentation dataset"
    ],

    "Predict Outcomes": [
        "Rainfall prediction",
        "Stock price trend prediction",
        "Customer churn prediction",
        "Employee promotion prediction",
        "Medical diagnosis prediction"
    ],

    "Hyperparameter Tuning": [
        "Random Forest optimization",
        "XGBoost parameter tuning",
        "SVM optimization",
        "Gradient Boosting optimization",
        "Decision Tree tuning"
    ],

    "Evaluate Model Performance": [
        "Classification metrics evaluation",
        "Regression metrics evaluation",
        "Cross-validation analysis",
        "Confusion matrix interpretation",
        "ROC-AUC performance analysis"
    ],

    "Explain Insights": [
        "Business insights from sales data",
        "Healthcare trend analysis",
        "Marketing campaign analysis",
        "Financial performance analysis",
        "Customer behavior analysis"
    ],
    }