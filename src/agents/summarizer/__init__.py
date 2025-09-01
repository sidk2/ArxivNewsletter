from strands import Agent
from ..utils import get_bedrock_model, load_paper_summary_prompt
from ...constants import SUMMARIZER_PROMPT_PATH
from typing import List, Dict
import json


def generate_summaries(interests: str, papers: List[Dict[str, str]]) -> str:
    bedrock_model = get_bedrock_model()

    agent = Agent(model=bedrock_model)
    prompt = load_paper_summary_prompt(SUMMARIZER_PROMPT_PATH, interests=interests, papers=json.dumps(papers))

    response = agent(prompt)

    return response.message['content'][-1]['text']
