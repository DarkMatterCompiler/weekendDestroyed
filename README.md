# PS1 Google Lens Pro Max
Video link: https://drive.google.com/file/d/1L-q7F59f1DgNA-YzworVFT4NaC4HFGJK/view?usp=sharing
## Image Captioning and Search Pipeline

This project integrates multiple AI models and a web search API to process images, generate search queries, and retrieve relevant information. It demonstrates how various AI models and APIs can be combined to create a system that understands visual content, interprets user queries, and fetches related information from the internet.

## Overview of the Pipeline

The pipeline begins by using the **MiniCPM-V-2** model to generate a caption for a given image. This caption describes the content of the image in a textual format. Following that, the **Qwen2.5-1.5B-Instruct** model takes both the caption and any additional user input to create a relevant search query. This query is then used to interact with the **Brave Search API**, which retrieves both text-based and image-based search results from the web. The pipeline is connected by using 2 google colab files as servers through the FastAPI and ngrok. The web app is created using streamlit.

The system is designed to demonstrate how different AI models can work together to understand images, create useful search queries, and retrieve relevant results, making it applicable for various domains such as e-commerce, content discovery, and more complex AI-driven applications.

## Features:
- Image captioning using MiniCPM-V-2 model
- Query generation based on image captions and user input via Qwen2.5-1.5B-Instruct model
- Text and image search through DuckDuckGo Search API
- Integration of AI models and external APIs for comprehensive information retrieval


# Retrieval-Augmented Generation (RAG) Pipeline

This repository contains the implementation of a Retrieval-Augmented Generation (RAG) pipeline that uses a combination of document retrieval and natural language generation to answer user queries based on a given corpus of documents. It is integrated with a FastAPI-based web app for query processing and response generation.

## Table of Contents

1. [Project Overview](#project-overview)
2. [How it Works](#how-it-works)
3. [Features](#features)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

This RAG pipeline is designed to answer complex queries using both document retrieval and generative language models. The pipeline classifies queries into different types, retrieves relevant documents from a corpus, and then uses a language model to generate an answer based on the retrieved documents. The pipeline supports three query types:

1. **Inference Queries**
2. **Temporal Queries**
3. **Comparison Queries**

The system retrieves and augments data from the corpus to improve answer quality and accuracy.

## How it Works

The pipeline is built using the following core components:

1. **Entity Extraction**: Extracts key entities such as topics, article names, and actions from the user query.
2. **Document Retrieval**: Based on extracted entities, the pipeline searches the corpus to find relevant documents.
3. **Query Classification**: Classifies the query into one of the three categories: `inference_query`, `temporal_query`, or `comparison_query`.
4. **Answer Generation**: The documents are passed to Meta-Llama-3.1 for generating the final answer. For some queries, the system breaks down the query into smaller sub-queries, retrieves relevant parts, and then combines them to generate the final answer.
5. **FastAPI Integration**: The pipeline is accessible through a FastAPI web application for easy interaction.

## Features

- **Multi-step query processing**: Queries are classified into different types, and the pipeline adjusts its retrieval and generation strategies accordingly.
- **Efficient document retrieval**: Documents are retrieved based on keywords, with support for actions, topics, and article names.
- **Scalable**: Can be integrated with large document corpora for efficient searching and answering.
- **Flexible query handling**: Breaks down complex queries into smaller parts to provide more accurate answers.
- **Web Integration**: Accessible through a FastAPI web app for querying and results display.


# RAG Pipeline with FastAPI and Ngrok Integration (Multiple Notebooks)

This project integrates a Retrieval-Augmented Generation (RAG) pipeline using FastAPI, exposed through **ngrok**. The FastAPI endpoints are deployed from four separate Google Colab notebooks, each providing one public URL. These URLs need to be integrated into your local `app.py` file for specific query types.

## Steps to Use

### 1. Install Requirements

Make sure you have the required packages installed locally or in your Colab notebook:

```bash
pip install pyngrok fastapi uvicorn pydantic
```

### 2. Run the Four Colab Notebooks

You need to run **four separate Colab notebooks**, each responsible for a different part of the RAG pipeline. Follow these steps for each notebook:

1. Open the Colab notebook.
2. Execute all cells in the notebook. The notebook will:
   - Install necessary dependencies.
   - Start a FastAPI app with the corresponding RAG pipeline.
   - Generate a public URL using **ngrok**.

3. After each notebook runs, you will see a unique **ngrok** URL. For example:
   ```
   FastAPI is publicly available at: http://<ngrok-generated-url>.ngrok.io
   ```

4. **Copy the generated ngrok URL** for each notebook, which will be used in your local `app.py` file.

### 3. Modify the URLs in `app.py`

You will need to update the four URLs in your local `app.py` file based on the URLs generated from each of the four Colab notebooks. Update the following variables:

```python
compurl = "https://<new-ngrok-url-1>.ngrok-free.app/rag-pipeline"  # URL from notebook 1
classurl = "https://<new-ngrok-url-2>.ngrok-free.app/rag-pipeline"  # URL from notebook 2
temporalurl = "https://<new-ngrok-url-3>.ngrok-free.app/rag_pipeline"  # URL from notebook 3
infurl = "https://<new-ngrok-url-4>.ngrok-free.app/rag_pipeline"  # URL from notebook 4
```

Replace each `<new-ngrok-url-x>` with the ngrok URLs from the respective Colab notebook outputs.

### 4. Run `app.py`

After updating the URLs, run the `app.py` file locally:

```bash
python app.py
```

Your local app will now send requests to the four different FastAPI endpoints hosted via ngrok, each handling a specific query type in the RAG pipeline.

---

### Example Workflow:

1. **Run all four Colab notebooks**. Each notebook will expose one of the four RAG pipeline endpoints using ngrok.
2. **Update the URLs** in your `app.py` with the ngrok URLs generated by the notebooks.
3. **Run `app.py`** to interact with the RAG pipeline endpoints through your local app.

---

### Troubleshooting

- **Ngrok session expiration:** Free-tier ngrok sessions expire after some time. If this happens, rerun the corresponding Colab notebook to get a new public URL and update your `app.py` accordingly.
- **Colab session management:** Ensure all four Colab sessions remain active for uninterrupted API access.

---

This guide should help you manage the integration of multiple Colab notebooks with your local app using ngrok.
