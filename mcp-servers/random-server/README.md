# Random MCP server

A lightweight local MCP server with two tools:

- `random_integer(minimum, maximum)` — returns an inclusive random integer.
- `random_choice(options)` — returns one item from a non-empty list.

Run it from the repository root with:

```bash
uv run python mcp-servers/random-server/server.py
```

The server uses MCP's stdio transport, so an MCP-compatible client can launch
it as a local subprocess. No network access or persistent state is required.

Run the lightweight checks with:

```bash
uv run python mcp-servers/random-server/test_server.py
```
