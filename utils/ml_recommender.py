import os
import joblib
import numpy as np

# ------------------------------------------
# Load Model & Vectorizer
# ------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "prompt_ai_classifier.pkl"
    )
)

vectorizer = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "prompt_tfidf.pkl"
    )
)

# ------------------------------------------
# AI Details
# ------------------------------------------

AI_INFO = {

    "ChatGPT": {
        "website": "https://chat.openai.com",
        "speciality": "Coding, Prompt Engineering, General AI"
    },

    "Claude": {
        "website": "https://claude.ai",
        "speciality": "Long-form Writing, Documentation"
    },

    "Gemini": {
        "website": "https://gemini.google.com",
        "speciality": "Multimodal AI, Google Ecosystem"
    },

    "Perplexity": {
        "website": "https://www.perplexity.ai",
        "speciality": "Research & Web Search"
    },

    "GitHub Copilot": {
        "website": "https://github.com/features/copilot",
        "speciality": "Programming"
    },

    "Microsoft Copilot": {
        "website": "https://copilot.microsoft.com",
        "speciality": "Office Productivity"
    },

    "Cursor AI": {
        "website": "https://cursor.com",
        "speciality": "AI Coding IDE"
    },

    "DeepSeek": {
        "website": "https://chat.deepseek.com",
        "speciality": "Reasoning & Coding"
    },

    "Grok": {
        "website": "https://grok.com",
        "speciality": "Real-time Information"
    },

    "Qwen": {
        "website": "https://chat.qwen.ai",
        "speciality": "Coding & Multilingual"
    }

}

# ------------------------------------------
# Recommendation Function
# ------------------------------------------

def recommend_ai_ml(
    role,
    task,
    context,
    constraint,
    output_format,
    goal
):

    text = f"""
Role: {role}
Task: {task}
Context: {context}
Constraint: {constraint}
Output Format: {output_format}
Goal: {goal}
"""

    vector = vectorizer.transform([text])

    probabilities = model.predict_proba(vector)[0]

    top3 = np.argsort(probabilities)[::-1][:3]

    # Normalize Top 3

    top_scores = probabilities[top3]

    top_scores = top_scores / np.sum(top_scores)

    recommendations = []

    for idx, score in zip(top3, top_scores):

        ai = model.classes_[idx]

        recommendations.append({

            "name": ai,

            "confidence_score": round(score*100,2),

            "reason":
                f"Recommended because your requirement closely matches tasks where {ai} performs exceptionally well in {AI_INFO[ai]['speciality']}.",

            "official_website":
                AI_INFO[ai]["website"]

        })

    return recommendations