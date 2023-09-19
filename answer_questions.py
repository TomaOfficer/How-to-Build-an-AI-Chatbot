from llama_index import StorageContext, load_index_from_storage
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine


def answer_question(query):
  # load knowledge base from disk. you may want to move this outside of the answer question function to increase performance
  index = load_index_from_storage(
      StorageContext.from_defaults(persist_dir="storage"))

  # Configure retriever with custom top-k setting
  retriever = VectorIndexRetriever(
      index=index,
      similarity_top_k=5,  # Change this number to your desired top-k
  )

  # make the knowledge base into a query engine—an object that queries can be run on
  query_engine = RetrieverQueryEngine(retriever)

  # run a query on the query engine. this will:
  # find text chunks that are similar to the query we gave it
  # give the query + the text chunks to GPT-3, and then return the answer
  response = query_engine.query(query)

  return response


def answer_questions():
  while True:
    query = input("Ask a question: ")
    if query == "quit":
      break
    response = answer_question(query)

    # Print the actual response (answer)
    print("Answer:", response)

    # Print the formatted sources
    print("Sources:", response.get_formatted_sources())
