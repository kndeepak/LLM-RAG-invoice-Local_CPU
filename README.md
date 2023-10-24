# Invoice data processing with Llama2 13B LLM RAG on Local CPU

## Quickstart

### RAG runs on: LlamaCPP, Haystack, Weaviate

1. Download the Llama2 13B model, check models/model_download.txt for the download link.
2. Install Weaviate local DB with Docker

`docker compose up -d`
   
3. Install the requirements: 

`pip install -r requirements.txt`

4. Copy text PDF files to the `data` folder.
5. Run the script, to convert text to vector embeddings and save in Weaviate vector storage: 

`python ingest.py`

6. Run the script, to process data with Llama2 13B LLM RAG and return the answer: 

`python main.py "What is the invoice number value?"`


SERVER 


7. Load Server using FAST API 

 'uvicorn main:app --reload' 
 
8.Run query in this format 

'http://127.0.0.1:8000/get_answer/?query=YourQuestionHere '

