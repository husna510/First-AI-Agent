from agents import  Agent
from my_conf.conf import MODEL, MODEL2


math_teacher = Agent(
    name="Ratan Lal",
    instructions="You are a maths teacher, your name is Ratan Lal and you provide the detail answer with summary with heading \"summary\"", 
    model = MODEL
)


english_teacher = Agent(
    name="Atma Ram",
    instructions="You are an English teacher and you provide the detailed answers to the questions asked with summary with heading \"summary\"", 
    model = MODEL2
)
