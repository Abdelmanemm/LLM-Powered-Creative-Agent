import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from huggingface_hub import InferenceClient

# --- 1. SETUP ---
load_dotenv()
print("Phase 4: Agent with Search and Image Generation Tools 🎨")
model = ChatGroq(model="llama3-8b-8192")

# --- 2. DEFINE TOOLS ---

# Tool 1: Web Search
search_tool = TavilySearchResults()

# Tool 2: Hugging Face Image Generation
@tool
def huggingface_image_generation_tool(prompt: str) -> str:
    """
    Generates an image from a text prompt using a Hugging Face model
    and saves it to a local file. Returns the file path.
    """
    client = InferenceClient()
    image = client.text_to_image(prompt, model="stabilityai/stable-diffusion-xl-base-1.0")
    # --- ROBUST FILE PATH FIX ---
    # Get the absolute path of the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Create a file path that is always inside that directory
    file_path = os.path.join(script_directory, "social_media_image.jpg")


    image.save(file_path)
    
    return f"Image successfully generated and saved to '{file_path}'"

# Assemble the list of ALL tools the agent can use
tools = [search_tool, huggingface_image_generation_tool]

# --- 3. CREATE THE AGENT ---
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(model, tools, react_prompt)
agent_executor = AgentExecutor(agent=agent, 
                               tools=tools, 
                               verbose=True,
                               handle_parsing_errors="Check your output and make sure it conforms to the Action/Action Input format.")

# --- 4. RUN THE AGENT ---
user_request = """
Your mission is to generate a complete social media post package for the AuraBand.

1.  First, create the text for the social media post, using the provided brief. The text should be engaging and on-brand.
2.  Second, after creating the text, create a detailed and creative prompt for a photorealistic image to accompany the post.
3.  Third, you MUST use the huggingface_image_generation_tool to generate the image using that prompt.

Your final answer MUST be the social media post text, followed by the exact file path returned by the image generation tool.

--- Product Brief ---
Product Name: AuraBand
Key Features: Solar-assisted charging, made from 100% recycled ocean plastic.
Brand Voice: Inspirational, calm, intelligent, minimalist.
Keywords: Harmony, balance, sustainable, mindful.
--- End Product Brief ---
"""

print("\n[INFO] Invoking the agent to generate text and an image...")
response = agent_executor.invoke({"input": user_request})

print("\n[SUCCESS] Here is the final output:")
print(response["output"])