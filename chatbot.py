import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.Conversation import Conversation

# Api key for the GroqModel
API_KEY = os.getenv("API_KEY") or "YOUR_API"

# Initialize the GroqModel
llm = GroqModel(api_key=API_KEY)

# Create a SimpleConversationAgent with the GroqModel
conversation = Conversation()
agent = SimpleConversationAgent(llm=llm, conversation=conversation)

# Define the function to be executed for the gradio interface
def converse(input_text, history):
    result = agent.exec(input_text)
    return result

# Create the Gradio interface components
demo = gr.ChatInterface(
    fn=converse,
    title="Abhishek Chatbot",
    description="A chatbot powered by GroqModel and Swarmauri. This is designed by Abhishek as a part of the Swarmauri Task.",
    multimodal=False,
)

if __name__ == "__main__":
    demo.launch(share=True)

