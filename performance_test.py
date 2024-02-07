import pytest
import requests

@pytest.mark.benchmark(min_rounds=10, disable_gc=True)
def test_search_performance(benchmark):
    keyword = "example"
    result = benchmark(lambda: perform_search(keyword))
    assert "response_time" in result.stats
    assert result.stats["response_time"].mean < 0.1  # Set your desired threshold

def perform_search(keyword):
    requests.get(f'search?query={keyword}')