from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from langchain_community.tools import DuckDuckGoSearchResults, DuckDuckGoSearchRun
    from langchain_community.tools.ddg_search.tool import DDGInput, DuckDuckGoSearchTool

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "DDGInput": "langchain_community.tools.ddg_search.tool",
    "DuckDuckGoSearchRun": "langchain_community.tools",
    "DuckDuckGoSearchResults": "langchain_community.tools",
    "DuckDuckGoSearchTool": "langchain_community.tools.ddg_search.tool",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "DDGInput",
    "DuckDuckGoSearchResults",
    "DuckDuckGoSearchRun",
    "DuckDuckGoSearchTool",
]
