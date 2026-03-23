from mcp.server.fastmcp import FastMCP

# Create an MCP instance with a name (no port argument here)
mcp = FastMCP("fastmcp-demo")

# Define a simple tool
@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

# Start the server
if __name__ == "__main__":
    # No port argument — MCP reads default or environment port
    mcp.run()