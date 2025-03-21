from agents import Agent, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI, AsyncAzureOpenAI
load_dotenv()

# anthropic
# client = AsyncOpenAI(
#     api_key=os.getenv("ANTHROPIC_API_KEY"),
#     base_url=os.getenv("ANTHROPIC_API_BASE")
# )

# azure
client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    azure_deployment=os.getenv("DEPLOYMENT_NAME"),
    api_version=os.getenv("OPENAI_API_VERSION")
)
set_default_openai_client(client=client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)
