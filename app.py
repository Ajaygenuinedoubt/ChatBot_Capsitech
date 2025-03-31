import wget
import streamlit as st
from llama_index import LlamaCPP, messages_to_prompt, completion_to_prompt
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Function to display a progress bar when downloading
def bar_custom(current, total, width=80):
    print("Downloading %d%% [%d / %d] bytes" % (current / total * 100, current, total))

# Download model (using wget)
model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"
wget.download(model_url, bar=bar_custom)

# Initialize Streamlit page
def init_page() -> None:
    st.set_page_config(page_title="Personal Chatbot")
    st.header("Personal Chatbot")
    st.sidebar.title("Options")

# Load the Llama model
def select_llm() -> LlamaCPP:
    return LlamaCPP(
        model_path="llama-2-7b-chat.Q2_K.gguf",
        temperature=0.1,
        max_new_tokens=500,
        context_window=3900,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": 1},
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )

# Initialize messages and the chatbot UI
def init_messages() -> None:
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content="You are a helpful AI assistant. Reply your answer in markdown format."
            )
        ]

# Get the answer from the model based on user input
def get_answer(llm, messages) -> str:
    response = llm.complete(messages)
    return response.text

# Main application loop
def main() -> None:
    init_page()
    llm = select_llm()
    init_messages()

    # User input
    if user_input := st.chat_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Bot is typing ..."):
            answer = get_answer(llm, st.session_state.messages)
            print(answer)
        st.session_state.messages.append(AIMessage(content=answer))

    # Display conversation history
    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)

if __name__ == "__main__":
    main()
