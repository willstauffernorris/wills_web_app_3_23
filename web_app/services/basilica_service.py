import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")
with basilica.Connection(API_KEY) as c:
    connection = basilica.Connection(API_KEY)

    print(type(connection))

    #breakpoint()

    print(type(c))

    sentences = ["Hello world!", "How are you?"]

    print(sentences)
    embeddings = c.embed_sentences(sentences)
    print(type(embeddings))
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]