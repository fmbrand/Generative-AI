from fastapi import FastAPI 
from transformers import pipeline 

## create a new FASTAPI app instance 
app= FastAPI()

## Initialze the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home ():
    return{"message":"Hello World"}
# Define a function to handle the GET request at '/genereate'
@app.get("./generate")
def gEnerate(text:str):
    # use the pipeline to generate text from given input text
    output=pipe(text)
    # return the generate text in Json response
    return {"output":output[0]['generated_text']}
