from typing import Dict

import arxiv
import datetime
import json

class ArxivParser:
    def __init__(self):
        self.client = arxiv.Client()

        self.cat_json_path: str = "arxiv-categories.json"
        self.categories: Dict[str, str] = self.get_categories()

    def get_categories(self) -> Dict[str, str]:
        """
        Get the list of categories from the JSON.
        """
        
        with open(self.cat_json_path, 'r') as f:
            categories = json.load(f)

        taxonomy_dict: Dict[str, str] = {item["tag"]: item["name"] for item in categories}
        return taxonomy_dict

    def papers_by_category_for_date(self,category: str, day: datetime.date, max_batch: int = 200) -> arxiv.Result:
        """
        Yield all arXiv results for `category` that were submitted/announced on `day`.

        Parameters
        ----------
        category : str   # e.g. "cs.AI", "astro-ph.GA"
        day : date       # which calendar date to collect
        max_batch : int  # API page size
        """
        search = arxiv.Search(
            query=self.submitted_date_query(category, day),
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
            max_results=max_batch
        )
        
        results = self.client.results(search)


    def submitted_date_query(self, category: str, day: datetime.date):
        start = day.strftime("%Y%m%d") + "0000"
        end   = day.strftime("%Y%m%d") + "2359"
        query = f"cat:{category}+AND+submittedDate:[{start}+TO+{end}]"
        return query
    
    def todays_papers_by_category(self, category: str):
        '''Convenience method for getting today's papers by category'''
        return self.papers_by_category_for_date(category, datetime.date.today())

    def yesterdays_papers_by_category(self, category: str):
        '''Convenience method for getting yesterday's papers by category'''
        return self.papers_by_category_for_date(category, datetime.date.today() - datetime.timedelta(days=1))

if __name__ == "__main__":
    parser = ArxivParser()
    query_str = parser.yesterdays_papers_by_category("cond-mat.soft")
    for paper in query_str:
        print('foo')
        print(paper.title, paper.entry_id)

    result = parser.search(query_str)