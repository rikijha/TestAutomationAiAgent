import asyncio

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_openai import ChatOpenAI
import os
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv(".env")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class ShoppingCart(BaseModel):
    login_status: str
    cart_status: str
    Estimated_Total:str


controller = Controller(output_model=ShoppingCart)


async def validation():
    task = (
        'Important : I am a UI Automation tester validating the tasks'
        'Open website http://localhost:4200/'
        'login with Email and password , use Email davidpaul@test.com and password david12345'
        'After login, go to Electronics and select first 2 products and add to cart'
        'Go to Shopping cart and store the Estimated Total value'
        'Increase the total quantity of any one product by clicking add quantity button and check if Estimated Total value updates accordingly'
    )
    llm = ChatOpenAI(model='gpt-4o', api_key=OPENAI_API_KEY)
    agent = Agent(task, llm,controller=controller, use_vision=True)
    history = await agent.run()
    print(history.final_result())


asyncio.run(validation())
