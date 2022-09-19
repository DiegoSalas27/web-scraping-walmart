import json
from urllib.parse import urlencode
from parsel import Selector

def create_search_url(query: str, page=1, sort="price_low") -> str:
    """create url for a single walmart search page"""
    return "https://www.walmart.com/search?" + urlencode(
        {
            "q": query,
            "sort": sort,
            "page": page,
            "affinityOverride": "default",
        }
    )

def parse_search(html_text: str):
    """extract search results from search HTML response"""
    sel = Selector(text=html_text)
    data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    data = json.loads(data)

    total_results = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["count"]
    results = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]
    return results, total_results