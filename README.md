# Paper Summarizer

**Paper Summarizer** is an application designed to generate concise summaries or research paper in PDF format. It leverages LLM to analyze text and produce summaries in Markdown format.

## Features
- Download and process research papers from a given PDF URL
- Automatically extract text from PDF files
- Generate summaries of research articles in less than 250 words
- Provide an interactive user interface

---

## Requirements
- Python 3.11 or later
- Conda (recommended for managing environments)
- Dependencies listed in `environment.yml` file

---

## Installation
1. Download Ollama from: https://ollama.com/download
2. Clone the repository:
```
git clone https://github.com/KamRoki/paper-summarizer
cd paper-summarizer
```
3. Set up the environment
```
conda env create -f environment.yml
conda activate paper-summarizer
```
4. Verify the installation
```
conda list
```

---

## Usage
1. **Run Ollama application**
1. **Run the Streamlit application:** Start the Streamlit app to interactively summarize papers:
```
streamlit run app.py
```
3. **Summarize a paper:**
    * Enter the URL of a research paper in PDF format
    * The app will extract the text and generate a summary

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you want to improve the project.

---

## Author
Created by Kamil Stachurski.