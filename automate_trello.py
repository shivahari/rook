'''
An automate Trello module to automate creating Trello boards using an MCP server
An AI assistant can use this module to help create Trello boards using Natural Language instructions
'''

import os
import requests
from fastmcp import FastMCP

mcp = FastMCP("Automate Trello board")

@mcp.tool()
def create_trello_board(board_name: str) -> str:
    "Create a Trello board"
    key = os.getenv("TRELLO_KEY")
    token = os.getenv("TRELLO_TOKEN")
    params = {"key":key,
              "token": token,
              "name": board_name}
    url = "https://api.trello.com/1/boards/"
    response = requests.post(url=url, params=params)
    return "Successfully created new Trello Board"

if __name__ == "__main__":
    mcp.run()
