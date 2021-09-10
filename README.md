# wandbot
A script to check your wandb runs and send you a telegram message on specific events
---

## Usage
- (optional, but recommended) create a new environment, eg. via `conda create -n wandbot python=3.9`
- install requirements via `pip install -r requirements.txt`
- set up telegram bot by running `telegram-send --configure` and following the instructions
- get a wandb API key from https://wandb.ai/settings
- launch script via `WANDB_API_KEY=<your key> python main.py`