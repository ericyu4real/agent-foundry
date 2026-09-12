"""A tiny MCP server that exposes safe randomization tools."""

import random

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("random-tools")


@mcp.tool()
def random_integer(minimum: int = 0, maximum: int = 100) -> int:
    """Return a random integer between minimum and maximum, inclusive."""
    if minimum > maximum:
        raise ValueError("minimum must be less than or equal to maximum")
    return random.randint(minimum, maximum)


@mcp.tool()
def random_choice(options: list[str]) -> str:
    """Return one item from a non-empty list of options."""
    if not options:
        raise ValueError("options must not be empty")
    return random.choice(options)


if __name__ == "__main__":
    mcp.run(transport="stdio")
