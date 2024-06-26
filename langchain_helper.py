from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API")

# Initialize the OpenAI model
llm = OpenAI(temperature=0.7)


# # Define the second prompt template
# prompt_temp_get_country_places = PromptTemplate(
#     input_variables=["country"],
#     template="Suggest tourist attractions in {country}."
# )

# # Create the second chain
# places_chain = SimpleSequentialChain(llm=llm_model, prompt=prompt_temp_get_country_places)

# # Create a combined chain (this may vary based on your library version)
# combined_chain = SimpleSequentialChain(
#     chains=[country_desc_chain, places_chain]
# )

# # Run the chain with the input
# response = combined_chain.run({'country': 'Sri Lanka'})

# print(response)

def generate_country_summary(country):
    
    # Implement prompt template
    prompt_temp_get_country = PromptTemplate(
        input_variables=['country'],
        template="Provide a brief description of {country} in a way that highlights tourist attractions. Descibe these topics,  Historical Facts, Top Attractions, Cultural Insights, Travel Tips. Separate paragraphs by each topic"
    )

    llm_chain = prompt_temp_get_country | llm

    response = llm_chain.invoke({'country': country})
    return response
