from src.parsing import get_all_papers
from src.constants import ARXIV_CS_URL
from src.agents.summarizer import generate_summaries
from src.utils import save_to_markdown


def main():
    interests = input(
        "🤖 Hello, what topics in Computer Science are you interested in? Please give a short sentence listing them. \n👤 "
    )

    papers = get_all_papers(ARXIV_CS_URL)
    newletter = generate_summaries(interests, papers)
    save_to_markdown(newletter, "examples")


if __name__ == "__main__":
    main()
