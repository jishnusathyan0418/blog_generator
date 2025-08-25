import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


st.set_page_config(page_title="Blog Post Generator")
st.title("Blog Post Generator")

openai_api_key = st.sidebar.text_input(
    label="OpenAI API Key",
    type="password"
)

def generate_response(topic):
    llm = OpenAI(temperature=.2, api_key=openai_api_key)
    template="""
    As experienced startup and venture capital writer,
    generate a 400 word blog post on {topic}.
    
    you response should be in this format:
    first print the blog post,
    then sum the total number of words on it and print the result like this,the post has x words.
    """
    
    prompt = PromptTemplate(
        input_variables=["topics"],
        template=template
    )
    
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input(label="Enter topic: ", placeholder="your topic")
if not openai_api_key.startswith("sk-"):
    st.warning("Enter OpenA API Key")
    st.stop()
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)   
