# MCP Kagi Search

### Setup and Usage

1. Install dependencies:

```bash
uv sync
source .venv/bin/activate
```

2. Set the Kagi API Token:

```bash
export KAGI_API_TOKEN='your_actual_token_here'
```

3. Run MCP server in development mode:

```bash
mcp dev src/mcp_kagi_search/server.py
```

4. Test via MCP Inspector:

- Open MCP inspector at `http://localhost:5173`.
- Run the `kagi_search` tool with a query (e.g., "steve jobs").

5. CLI Installation:

```bash
uv pip install .
```

- Verify the CLI:

```bash
mcp-kagi-search --help
```