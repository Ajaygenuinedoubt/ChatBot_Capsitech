# Personal Chatbot

This project is a **Personal Chatbot** application built using **Llama Index**, **LangChain**, and **Streamlit**. It leverages a **Llama-2-7B-Chat** model to generate AI responses based on user input. The chatbot is designed to provide responses in markdown format and includes an interactive UI.

## Features
- Uses **Llama-2-7B-Chat** model for generating AI responses.
- Interactive chat interface built with **Streamlit**.
- Supports contextual memory to maintain conversation history.
- Provides a sidebar option to clear conversation history.
- Uses **Llama Index** and **LangChain** for AI interactions.

## Installation

### Prerequisites
Ensure you have **Python 3.8+** installed on your system. Then, install the required dependencies using:

```sh
pip install -r requirements.txt
```

### Additional Dependencies
If the packages are not included in `requirements.txt`, install them manually using:

```sh
pip install langchain wget llama-index cohere llama-cpp-python streamlit
```

## Model Setup
Before running the chatbot, download the **Llama-2-7B-Chat** model:

```python
import wget

def bar_custom(current, total, width=80):
    print("Downloading %d%% [%d / %d] bytes" % (current / total * 100, current, total))

model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"
wget.download(model_url, bar=bar_custom)
```

## Running the Application

To start the chatbot, run the following command:

```sh
streamlit run app.py
```

If you want to expose the chatbot publicly using LocalTunnel, run:

```sh
npx localtunnel --port 8501
```

## File Structure
```
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Usage
1. Open the chatbot in your browser using the **localhost link** provided by Streamlit.
2. Type a question in the chat input field.
3. The chatbot will generate a response based on the **Llama-2-7B-Chat model**.
4. To clear the conversation history, click the **"Clear Conversation"** button in the sidebar.

## Issues & Support
If you encounter any issues, feel free to raise an issue on the project's repository or reach out to the contributors.

## License
This project is open-source and available under the MIT License.

