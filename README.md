# RAG-First

This is a simple implementation of a Retrieval-Augmented Generation (RAG) system using Python. The project leverages the LangChain framework and ChromaDB for efficient document retrieval and language generation.

## Features

- **Document Retrieval**: Uses ChromaDB to store and retrieve relevant documents.
- **Language Generation**: Powered by LangChain to generate context-aware responses.
- **Seamless Integration**: Combines retrieval and generation for enhanced performance.

## Requirements

- Python 3.8 or higher
- LangChain
- ChromaDB

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/RAG-first.git
   cd RAG-first
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your documents and load them into ChromaDB.
2. Run the `lang.py` script to start the RAG system:
   ```bash
   python lang.py
   ```

## How It Works

The `lang.py` script orchestrates the RAG pipeline:

- Documents are retrieved from ChromaDB based on the input query.
- LangChain processes the retrieved documents and generates a response.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [ChromaDB](https://github.com/chroma-core/chroma)
