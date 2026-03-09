

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
from mem0client.memory_client import DjangoMemory

config = MemoryConfig(
    llm={
        "provider": "ollama",
        "config": {
            "model": "llama3",
            "base_url": "http://ollama:11434"
        }
    },
    embedder={
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "base_url": "http://ollama:11434"
        }
    }
)

memory = DjangoMemory(config=config)