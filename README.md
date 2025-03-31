# Personal Chatbot

## Overview
This project is a **Personal AI Chatbot** built using **Llama-2** and **Streamlit**, providing an interactive chatbot experience. The chatbot leverages **Llama Index** and **LangChain** to manage conversation history and generate responses efficiently.

## Features
- Uses **Llama-2-7B** for AI-driven conversation.
- **Streamlit-based UI** for easy interaction.
- **Supports Markdown responses**.
- **Clearing conversation history** with a single click.
- **Efficient response generation** using GPU-accelerated inference.

## Installation
To set up and run the chatbot locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
Ensure you have Python installed (preferably 3.8 or later). Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Download the Llama Model
The chatbot requires the **Llama-2-7B-Chat GGUF** model. Download it using `wget`:
```bash
python download_model.py
```
Alternatively, you can manually download it from:
[Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)

### 4. Run the Chatbot
Start the chatbot using Streamlit:
```bash
streamlit run app.py
```
To access it remotely, use:
```bash
npx localtunnel --port 8501
```

## File Structure
```
📂 your-repo-name
│── app.py              # Main chatbot application
│── download_model.py   # Script to download the Llama model
│── requirements.txt    # Required dependencies
│── README.md           # Documentation
```

## Technologies Used
- **Llama-2** (Meta AI)
- **Llama Index**
- **LangChain**
- **Streamlit** (for UI)
- **Cohere** (optional for enhanced language understanding)

## Usage
1. Enter your query in the chat input field.
2. Wait for the chatbot to generate a response.
3. Clear conversation history if needed.

## Known Issues
- Initial model download may take time.
- Requires GPU support for optimal performance.

## Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

Developed with ❤️ by [Your Name](https://github.com/Ajaygenuinedoubt)

