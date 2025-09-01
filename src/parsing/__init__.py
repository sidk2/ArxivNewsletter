import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def get_all_papers(url: str, limit: int = 50) -> List[Dict[str, str]]:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    papers = []
    for dd in soup.find_all("dd"):
        title_tag = dd.find("div", class_="list-title")
        link_tag = dd.find_previous("a", id=True)
        abstract_tag = dd.find("p", class_="mathjax")

        papers.append(
            {
                "title": (
                    title_tag.get_text(strip=True).replace("Title:", "")
                    if title_tag
                    else None
                ),
                "link": f"https://arxiv.org{link_tag['href']}" if link_tag else None,
                "abstract": (
                    abstract_tag.get_text(" ", strip=True) if abstract_tag else None
                ),
            }
        )

    return papers[:limit]
