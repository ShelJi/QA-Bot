# QA-Bot

`pip install transformers torch streamlit`

## 🤖 1. Transformers

**Library:** Part of Hugging Face.

**Used for:** Natural Language Processing (NLP) tasks like:

- Text classification
- Question answering
- Translation
- Text generation (like ChatGPT!)

```python
from transformers import pipeline

qa = pipeline("question-answering")
qa(question="What is the capital of France?", context="France's capital is Paris.")
# Output: {'answer': 'Paris'}
```

## 🔥 2. Torch (PyTorch)

**Library:** Developed by Facebook AI.

**Used for:** Deep learning and building neural networks.

**Alternative to:** TensorFlow.

Works behind the scenes in many models from Hugging Face.

```python
import torch

x = torch.tensor([1.0, 2.0])
y = x * 2
print(y)  # tensor([2., 4.])
```

## 🌐 3. Streamlit

**Library:** For building interactive web apps in Python.

**Great for:** AI demos, dashboards, data science tools.

```python
import streamlit as st

st.title("Hello Streamlit!")
name = st.text_input("Enter your name")
st.write("Hello", name)
```

## 🧠 Hugging Face

Hugging Face is an AI company and open-source platform that focuses on making machine learning models easy to use, especially for natural language processing (NLP).

Think of Hugging Face as:

`"GitHub + App Store for AI Models"`

It offers:

- Pre-trained models (like ChatGPT, BERT, etc.)
- Datasets
- APIs
- Training tools
- Model hosting and sharing

## 🔧 Main Tools from Hugging Face

### 1. 🤗 transformers library

Provides thousands of pre-trained models for:

- Text classification
- Translation
- Question answering
- Text generation
- Works with PyTorch and TensorFlow

```python
from transformers import pipeline
qa = pipeline("question-answering")
qa(question="Where is Hugging Face based?", context="Hugging Face is based in New York.")
# Output: {'answer': 'New York'}
```

### 2. 🤗 datasets library

Access to huge open-source datasets used for training and evaluation.

### 3. 🤗 Model Hub

Website: https://huggingface.co/models

You can search, download, and upload models easily.

### 4. 🤗 Spaces

Host your ML apps using Streamlit, Gradio, or HTML for free.

✅ Why Use Hugging Face?
Saves time: No need to train models from scratch

Easy to integrate: Use models with just a few lines of code

Community-driven: Thousands of models contributed by users and researchers
