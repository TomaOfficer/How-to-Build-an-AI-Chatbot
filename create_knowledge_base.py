from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext
from llama_index.node_parser import SimpleNodeParser
from llama_index.llms import OpenAI


def construct_base_from_directory(path):
  # load all of the files inside of the folder named "data" and store them in a variable called documents
  print("Loading your data for the knowledge base...")
  documents = SimpleDirectoryReader(path).load_data()

  # Define the LLM (GPT-4 in this case)
  llm = OpenAI(temperature=0.1, model="gpt-4")
  service_context = ServiceContext.from_defaults(llm=llm)

  print("Creating knowledge base.")
  index = GPTVectorStoreIndex.from_documents(documents,
                                             service_context=service_context)

  print("Knowledge base created. Saving to disk...")
  index.storage_context.persist()
