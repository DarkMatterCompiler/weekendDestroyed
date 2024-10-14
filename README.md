
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
