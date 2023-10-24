from fastapi import FastAPI, HTTPException, Query
from llm.wrapper import setup_rag_pipeline
from typing import Dict
import timeit

app = FastAPI()

# Initialize the RAG pipeline once, rather than on every request.
rag_pipeline = setup_rag_pipeline()

@app.get("/get_answer/", response_model=Dict[str, str])
async def get_answer(query: str = Query(default="What is the invoice number value?", description="Enter the query to pass into the LLM")):
    start = timeit.default_timer()
    
    json_response = rag_pipeline.run(query=query, params={"Retriever": {"top_k": 5}})
    
    answers = json_response['answers']
    answer = 'No answer found'
    for ans in answers:
        answer = ans.answer
        break
    
    end = timeit.default_timer()
    time_taken = end - start
    
    return {
        "answer": answer,
        "time_taken": str(time_taken) + " seconds"
    }
