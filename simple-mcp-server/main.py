from mcp.server import FastMCP

# Create an instance of the FastMCP server
mcp = FastMCP("Demo")


# Define a simple tool that adds two numbers
@mcp.tool()
def add(x: int, y: int) -> int:
    '''This tool takes two integers as input and returns their sum.'''
    return x + y


# Define a resource that returns a greeting message
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    '''This resource takes a name as a parameter and returns a greeting message.'''
    return f"Hello, {name}!"