# <h1>🧠 <strong>Multiple Sclerosis Research API</strong></h1>
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#api-endpoints">API Endpoints</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version">
</p>

## 📊 Overview

This API provides comprehensive, up-to-date information on Multiple Sclerosis (MS), leveraging FastAPI for high performance and Llama 3 for AI-enhanced responses. Access data from 2000 to present, including general information, symptoms, statistics, treatments, and research advances.

## ✨ Key Features

- 🚀 **High-Performance API**: Built with FastAPI for fast and efficient data retrieval
- 🤖 **AI-Enhanced Responses**: Integrated with Llama 3 for dynamic, detailed information
- 📈 **Comprehensive MS Data**: Covering various aspects of Multiple Sclerosis
- 🔄 **Real-time Updates**: Regularly updated with the latest research and statistics
- 📚 **Interactive Documentation**: Swagger UI for easy API exploration

## 🛠 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Llama_3-FF6F61?style=for-the-badge&logo=AI" alt="Llama 3">
  <img src="https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=SQL" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic" alt="Pydantic">
</p>

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/general-info` | Retrieve general MS information |
| GET    | `/symptoms` | List MS symptoms |
| GET    | `/statistics` | Get MS statistics |
| GET    | `/treatments` | List MS treatments since 2000 |
| GET    | `/research-advances` | Get latest MS research advances |
| GET    | `/llama-query` | AI-enhanced query responses |

## 🚀 Getting Started

1. **Clone the repository**
2. **Set up a virtual environment**
3. **Install dependencies**
4. **Run the API**
5. **Access the API documentation**

Open your browser and navigate to `http://localhost:8000/docs`

## 📖 Usage

Here's a quick example of how to use the API with Python:

```python
import requests

# Get general information about MS
response = requests.get("http://localhost:8000/general-info")
print(response.json())

# Make an AI-enhanced query
query = "What are the latest treatments for MS?"
response = requests.get(f"http://localhost:8000/llama-query?query={query}")
print(response.json())
