
# note: testing is done in project folder(here in app) not in the feature or microservice folder(here it is treated as project)
#---------------------------------if i use openai  then testing code -----------------------------
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# django.setup()

# from mem0client.memory_client import DjangoMemory

# memory = DjangoMemory()

# result = memory.add(
#     messages="John finished the AI project",
#     user_id="user123"
# )

# print(result)

#--------------------------------------------------------------------------------

# ------------------------------ if i use ollama then testing is follow like this ( ollama running in manually )------------------------------
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# django.setup()

# from mem0.configs.base import MemoryConfig
# from mem0client.memory_client import DjangoMemory

# config = MemoryConfig(
#     llm={
#         "provider": "ollama",
#         "config": {
#             "model": "llama3",
#             "base_url": "http://host.docker.internal:11434"
#         }
#     },
#     embedder={
#         "provider": "ollama",
#         "config": {
#             "model": "nomic-embed-text",
#             "base_url": "http://host.docker.internal:11434"
#         }
#     }
# )

# memory = DjangoMemory(config=config)

# result = memory.add(
#     messages="John finished the AI project",
#     user_id="user123"
# )

# print(result)

#------------------------------------------------------------

#----------------------------------------- if i use ollama in contianer -------------------from mem0.configs.base import MemoryConfig
# from mem0client.memory_client import DjangoMemory

# config = MemoryConfig(
#     llm={
#         "provider": "ollama",
#         "config": {
#             "model": "llama3",
#             "base_url": "http://ollama:11434"
#         }
#     },
#     embedder={
#         "provider": "ollama",
#         "config": {
#             "model": "nomic-embed-text",
#             "base_url": "http://ollama:11434"
#         }
#     }
# )

#--------------------------------- lama --------------------------------
# memory = DjangoMemory(config=config)
import os
import django

# # Tell mem0 where Ollama server is
# os.environ["OLLAMA_HOST"] = "http://ollama:11434"

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# django.setup()

# from mem0.configs.base import MemoryConfig
# from mem0client.memory_client import DjangoMemory

# config = MemoryConfig(
#     llm={
#         "provider": "ollama",
#         "config": {
#             "model": "llama3"
#         }
#     },
#     embedder={
#         "provider": "ollama",
#         "config": {
#             "model": "nomic-embed-text"
#         }
#     }
# )

# memory = DjangoMemory(config=config)

# result = memory.add(
#     messages="John finished the AI project",
#     user_id="user123"
# )

# print(result)

# result = memory.get_all(user_id="user123")
# print(result)

#----------------------------------- phi 3 --------------------------------

import os
import django

# Tell mem0 where Ollama server is
os.environ["OLLAMA_HOST"] = "http://ollama:11434"

# Start Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from mem0.configs.base import MemoryConfig
from mem0client.memory_client import DjangoMemory

config = MemoryConfig(
    llm={
        "provider": "ollama",
        "config": {
            "model": "phi3:latest"
        }
    },
    embedder={
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest"
        }
    },
    # vector_store={
    #     "provider": "qdrant",
    #     "config": {
    #         "path": "/app/qdrant_mem0"
    #     }
    # }
    vector_store={
    "provider": "qdrant",
    "config": {
        "path": "/app/qdrant_mem0",
        "collection_name": "memories_768"
    }
}
)

memory = DjangoMemory(config=config)

memory.add(
    "John finished the AI project",
    user_id="user123"
)

result = memory.get_all(user_id="user123")

print("Stored Memories:")
print(result)