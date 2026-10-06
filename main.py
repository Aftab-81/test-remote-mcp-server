from fastmcp import FastMCP
import random
import json

mcp = FastMCP(name = "CalculatorServer")

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generates a random number between min_val and max_val"""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Returns server information"""

    info = {
        "name": "CalculatorServer",
        "version": "1.0",
        "description": "A simple calculator server that can add numbers and generate random numbers.",
        "tools": ["add_numbers", "random_number"],
        "author": "Aftab"
    }

    return json.dumps(info, indent = 4)

# Start the server
if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 1244)