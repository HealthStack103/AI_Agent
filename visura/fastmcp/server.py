from mcp.server.fastmcp import FastMCP

# Create FastMCP app
mcp = FastMCP("learning-mcp")

# Define a tool
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


# run this mcp dev server.py
# verify that whether it is needed or not 
#  $body = '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"add","arguments":{"a":5,"b":7}}}'
# >> $body | python server.py
# >> 