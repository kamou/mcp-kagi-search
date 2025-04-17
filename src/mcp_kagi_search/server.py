import os
import requests
from requests.exceptions import RequestException
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

# MCP initialization
mcp = FastMCP("kagi_search")

KAGI_API_URL = "https://kagi.com/api/v0/search"
KAGI_API_TOKEN = os.getenv("KAGI_API_TOKEN")

@mcp.tool()
def kagi_search(query: str) -> dict:
    """
    Search the provided query using Kagi Search API and return results.

    Usage:
        kagi_search("steve jobs")
    """
    headers = {
        "Authorization": f"Bot {KAGI_API_TOKEN}"
    }
    params = {"q": query}

    try:
        response = requests.get(KAGI_API_URL, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            raise McpError(ErrorData(INTERNAL_ERROR, f"Kagi API error: {response.status_code}, {response.text}"))
        return response.json()
    except RequestException as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Request failed: {str(e)}")) from e
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Unexpected error: {str(e)}")) from e