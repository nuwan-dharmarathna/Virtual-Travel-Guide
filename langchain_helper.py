from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API")

llm = OpenAI(temperature=0.7)

print(llm("Suggest me some restaurent names in beach"))

def generate_country_summary(country):
    return{
        'destination': 'Wonder of India',
        'current_status': 'current status of india'
        
    }