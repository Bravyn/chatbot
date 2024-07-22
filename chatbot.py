import os
import pandas as pd
from pandasai import Agent
from config import api_key


def query_agent(data, question):
# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
    os.environ["PANDASAI_API_KEY"] = api_key

    agent = Agent(data)
    return agent.chat(question)

