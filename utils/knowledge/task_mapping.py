"""
=========================================
PromptWise AI
Role → Task Mapping
=========================================

This module maps each AI role to the
tasks it can realistically perform.

Used in:
- Dataset Generation
- Prompt Builder
- Recommendation Engine
"""

TASK_MAPPING = {

    "Expert Data Scientist": [
        "Analyze Dataset",
        "Perform Exploratory Data Analysis",
        "Build Machine Learning Model",
        "Feature Engineering",
        "Predict Outcomes",
        "Hyperparameter Tuning",
        "Evaluate Model Performance",
        "Explain Insights"

    ],

    "Senior Machine Learning Engineer": [
        "Train ML Pipeline",
        "Optimize ML Model",
        "Deploy ML Model",
        "Perform Feature Selection",
        "Compare Algorithms",
        "Tune Hyperparameters",
        "Explain ML Workflow",
        "Model Monitoring"
    ],

    "Senior Software Engineer": [
        "Write Code",
        "Debug Code",
        "Optimize Algorithm",
        "Code Review",
        "Refactor Code",
        "Implement Authentication",
        "Develop REST API",
        "Fix Bugs"
    ],

     "Software Architect" : [
        "Design System Architecture",
        "Microservice Design",
        "Database Design",
        "API Design",
        "Design Patterns",
        "Scalability Planning",
        "System Optimization",
        "Cloud Architecture"
     ],

     "Data Analyst" : [
        "Analyze Business Data",
        "Generate Dashboard",
        "Create Visualizations",
        "Interpret KPIs",
        "Generate Reports",
        "Data Cleaning",
        "SQL Analysis",
        "Trend Analysis"
     ],

     "Business Analyst" : [
        "Business Requirement Analysis",
        "SWOT Analysis",
        "Market Analysis",
        "Risk Analysis",
        "Process Optimization",
        "Requirement Gathering",
        "Business Documentation",
        "Decision Support"
     ],

     "Research Scientist" : [
        "Literature Review",
        "Research Methodology",
        "Hypothesis Formation",
        "Research Summary",
        "Compare Research Papers",
        "Experimental Design",
        "Research Proposal",
        "Scientific Writing"
     ],

     "Cybersecurity Specialist" : [
        "Security Assessment",
        "Vulnerability Analysis",
        "Threat Modeling",
        "Penetration Testing",
        "Incident Response",
        "Risk Mitigation",
        "Security Best Practices",
        "Compliance Review"
     ],

     "Cloud Solutions Architect":[
        "Design Cloud Infrastructure",
        "AWS Architecture",
        "Azure Architecture",
        "Cloud Migration",
        "Cost Optimization",
        "Cloud Security",
        "Serverless Design",
        "Cloud Deployment"
     ],

     "DevOps Engineer": [
        "CI/CD Pipeline",
        "Docker Configuration",
        "Kubernetes Deployment",
        "Infrastructure Automation",
        "Monitoring",
        "Logging",
        "Cloud Deployment",
        "Performance Optimization"
     ]

}