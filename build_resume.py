from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import ollama


REPO_ROOT = Path(__file__).resolve().parent
CONFIG_DIR = REPO_ROOT / "config"
TEMPLATES_DIR = REPO_ROOT / "templates"
PROMPTS_DIR = REPO_ROOT / "prompts"
DEFAULT_PROFILE_FILE = REPO_ROOT / "profile.toml"


def generate_experience_prompt(job_posting: str) -> str:
    with open(PROMPTS_DIR / "prompt_experience.md", "r") as file:
        prompt = file.read()
    prompt = prompt.replace("{{ job_posting }}", job_posting)
    with open("config/experience.json", "r") as file:
        experience = json.load(file)
    prompt = prompt.replace("{{ experience }}", json.dumps(experience))
    return prompt


def generate_skills_prompt(job_posting: str) -> str:
    with open(PROMPTS_DIR / "prompt_skills.md", "r") as file:
        prompt = file.read()
    prompt = prompt.replace("{{ job_posting }}", job_posting)
    with open("config/skills.json", "r") as file:
        skills = json.load(file)
    prompt = prompt.replace("{{ skills }}", json.dumps(skills))
    return prompt


if __name__ == "__main__":

    # Prompt the user to input the job posting.
    with open("job_posting.txt", "r") as file:
        job_posting = file.read()
    
    # # Generate the experience section.
    # experience_prompt = generate_experience_prompt(job_posting)
    # stream = ollama.chat(
    #     model="ministral-3", 
    #     messages=[{"role": "user", "content": experience_prompt}],
    #     stream=True,
    # )
    # for chunk in stream:
    #     print(chunk['message']['content'], end='', flush=True)

    # Generate the skills section.
    skills_prompt = generate_skills_prompt(job_posting)
    stream = ollama.chat(
        model="ministral-3", 
        messages=[{"role": "user", "content": skills_prompt}],
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    # Load the template.
    with open("template.md", "r") as file:
        template = file.read()




