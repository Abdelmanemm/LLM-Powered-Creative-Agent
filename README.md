# LLM-Powered Creative Agent

An autonomous agent that can plan and execute a multi-step workflow to generate social media content for a new product, using an LLM as its core "brain."

## Features

* **Autonomous Planning:** The agent can break down a high-level goal into a series of executable steps.
* **Tool Use:** The agent is equipped with tools to perform actions:
    * **Web Search:** Uses Tavily to research current trends and information.
    * **Image Generation:** Uses Hugging Face's Inference API to generate images with Stable Diffusion.
* **Content Generation:** Produces creative, on-brand social media text based on research and a product brief.

## How It Works

This project uses a ReAct (Reason + Act) agent built with the LangChain framework. The agent's reasoning is powered by the Llama 3 8B model via the Groq API.

The agent follows this loop:
1.  **Reason:** Analyzes the user's request and its available tools.
2.  **Act:** Chooses and executes a tool (e.g., performs a web search).
3.  **Observe:** Gets the result from the tool.
4.  **Repeat:** Continues this loop until it has enough information to generate the final answer.

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abdelmanemm/LLM-Powered-Creative-Agent.git
    cd LLM-Powered-Creative-Agent
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your API keys:
    ```
    GROQ_API_KEY="gsk_..."
    TAVILY_API_KEY="tvly-..."
    HUGGINGFACEHUB_API_TOKEN="hf_..."
    ```

## Usage

To run the agent, simply execute the main script from your terminal:
```bash
python main.py
```
The agent will print its thought process to the console and save the generated image as `social_media_image.jpg` in the project directory.

## Example Output

```
> Entering new AgentExecutor chain...
Thought: I need to create an engaging social media post and a matching image for the AuraBand. I will start by creating the text for the post, then generate an image.

Action: huggingface_image_generation_tool
Action Input: A photorealistic image of a sleek, minimalist smartwatch made from recycled ocean plastic, displayed on a piece of driftwood on a serene, sunny beach.

> Finished chain.

[SUCCESS] Here is the final output:
"Find harmony in every moment with AuraBand, the solar-assisted charging watch made from 100% recycled ocean plastic. Embody a sustainable and mindful lifestyle with our eco-friendly timepiece. #HarmonyInMotion #SustainableFashion #MinimalistVibes"
Image successfully generated and saved to 'social_media_image.jpg'
```
