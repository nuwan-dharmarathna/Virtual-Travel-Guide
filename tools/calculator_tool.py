from langchain.tools import tool
from pydantic import BaseModel, Field

# define pydentics models for the tool's input parameters

# class CalculationInput(BaseModel):
#     operation: str = Field(..., description="The mathematical operation to perform")
#     factor: float = Field(..., description="A factor which to multiply thr result of the operation")
    
# # Use the tool decorator with the args_schema parameter pointing to the pydentic model
# @tool("perform_calculation", args_schema=CalculationInput, return_direct=True)
# def perform_calculation(operation:str, factor:float) -> str:
#     """
#     Perform a specified mathematical operation and multiplies the result by a given factor.
    
#     Parameters:
#     - operation (str): A String representing the mathematical operation to perform (e.g. "15+2")
#     - factor (float): A factor by which to multiply the result of the operation
    
#     Returns:
#     - A string representing of the calculation result
    
#     """
    
#     #perform the calculation
#     result = eval(operation) * factor
    
#     #return the result as a string
#     return f"The result of {operation} multiplied by {factor} is {result}."


class CalculatorTools():

    @tool("Make a calculation")
    def calculate(operation):
        """Useful to perform any mathematical calculations,
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical
        expression, a couple examples are `200*7` or `5000/2*10`
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"