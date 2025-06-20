import asyncio
from agents import Runner
from my_agents.maths_teacher import math_teacher,english_teacher


#to store the answer in the variable
#USING ASYNCH APPROACH


input_task = input(f"Ask Questions to {english_teacher.name}:  ") #ask dynamic questions
async def main():
        result = await Runner.run(english_teacher,input_task) 
        print(result.final_output)
        



asyncio.run(main())