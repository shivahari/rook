# rook

## Overview
This project automates the creation of Trello boards using an AI assistant by leveraging MCP ([Model Control Protocol](https://www.anthropic.com/news/model-context-protocol)) server. Create a Trello board in a [multi-turn](https://poly.ai/blog/multi-turn-conversations-what-are-they-and-why-do-they-matter-for-your-customers/) conversation with the assistant.

## Prerequisites
To use this project, ensure you have the following:
- A [Trello](https://trello.com/) account with API access
- Python3.10 or greater
- [Ollama](https://ollama.com)
- [goose](https://block.github.io/goose/)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shivahari/rook.git
   cd rook
   ```
2. Install dependencies:
   ```sh
   python3.10 -m venv <venv_name> # Create virtual environment
   source <venv_name>/bin/activate # Activate virtual environment
   pip install -r requirements.txt # Install requirements
   ```
3. Set up environment variables:
   ```sh
   export TRELLO_KEY=your_api_key
   export TRELLO_TOKEN=your_api_token
   ```
4. Setup Ollama
   - [Download & install Ollama](https://ollama.com/download)
5. Setup goose
   - [Install goose](https://block.github.io/goose/docs/getting-started/installation)
   - [Configure goose to use Local LLM - qwen2.5](https://block.github.io/goose/docs/getting-started/providers#local-llms-ollama) 

## Usage
1. Create a `goose session`:
   ```sh
   goose session --with-extension "python automate_trello.py"
   ```
2. Instruct the assistant:
   ```sh
   starting session | provider: ollama model: qwen2.5:3b
   logging to /Users/ai/.config/goose/sessions/TTtanC97.jsonl


   Goose is running! Enter your instructions, or try asking what goose can do.


   ( O)> What can you do for me?
   I can assist with creating a Trello board or list resources from extensions. How may I assist you today?

   ( O)> Can you help creating a Trello board?
   Of course! Could you please provide me with the name for your Trello board?

   ( O)> Skip it
   Sure, I can create a Trello board, can you suggest a name?

   ( O)> Let's name it "MCP Board"

   ─── create_trello_board | i0se8run ──────────────────────────
   board_name: MCP Board
 
   Your Trello board named "MCP Board" has been successfully created.
   ```
> [!NOTE]  
> The reponse from the assistant will not be exactly the same as listed, this is expected

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any issues or inquiries, reach out via shivahari@qxf2.com or open an issue in the repository.

---
Happy automating! 🚀
