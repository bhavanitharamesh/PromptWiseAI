import os
import json
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Load API Key
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SYSTEM_PROMPT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "system_prompt.txt"
)

RECOMMENDER_PROMPT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "recommender_prompt.txt"
)

# --------------------------------------------------
# Load Prompt Files
# --------------------------------------------------

with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

with open(RECOMMENDER_PROMPT_PATH, "r", encoding="utf-8") as f:
    RECOMMENDER_PROMPT = f.read()

# --------------------------------------------------
# Prompt Generator
# --------------------------------------------------

def generate_prompt(
    role,
    task,
    context,
    constraint,
    output_format,
    goal
):

    user_prompt = f"""
AI Role:
{role}

Task:
{task}

Context:
{context}

Constraints:
{constraint}

Output Format:
{output_format}

Goal:
{goal}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\n\n" + user_prompt
    )

    return response.text


# --------------------------------------------------
# Recommendation Engine
# --------------------------------------------------

def recommend_ai(
    role,
    task,
    context,
    constraint,
    output_format,
    goal
):

    user_prompt = f"""
User Requirement

Role:
{role}

Task:
{task}

Context:
{context}

Constraints:
{constraint}

Output Format:
{output_format}

Goal:
{goal}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=RECOMMENDER_PROMPT + "\n\n" + user_prompt
    )

    text = response.text.strip()

    print("\n========== GEMINI RESPONSE ==========")
    print(text)
    print("=====================================\n")

    # Remove markdown if Gemini returns ```json
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Extract JSON array
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if not match:
        print("No JSON array found.")
        return []

    json_text = match.group()

    try:
        recommendations = json.loads(json_text)

        print("\n========== PARSED RESULT ==========")
        print(recommendations)
        print("===================================\n")

        return recommendations

    except Exception as e:
        print("\n========== JSON ERROR ==========")
        print(e)
        print(json_text)
        print("================================\n")
        return []