import logging
from typing import Optional, List

from open_webui.retrieval.web.main import SearchResult, get_filtered_results
from open_webui.env import SRC_LOG_LEVELS

from firecrawl import Firecrawl

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["RAG"])


def search_firecrawl(
    firecrawl_url: str,
    firecrawl_api_key: str,
    query: str,
    count: int,
    filter_list: Optional[List[str]] = None,
) -> List[SearchResult]:
    try:
        firecrawl = Firecrawl(api_key=firecrawl_api_key, api_url=firecrawl_url)
        response = firecrawl.search(
            query=query, limit=count, ignore_invalid_urls=True, timeout=count * 3
        )
        results = response.web
        if filter_list:
            results = get_filtered_results(results, filter_list)
        results = [
            SearchResult(
                link=result.url,
                title=result.title,
                snippet=result.description,
            )
            for result in results[:count]
        ]
        log.info(f"External search results: {results}")
        return results
    except Exception as e:
        log.error(f"Error in External search: {e}")
        return []
