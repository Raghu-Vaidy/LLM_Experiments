import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()

