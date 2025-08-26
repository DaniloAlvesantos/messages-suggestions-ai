# WhatsApp AI Assistant

An unlimited AI API for WhatsApp message suggestions using Ollama, Python, FastAPI and the llama3.2:1b model. This project provides intelligent, contextual message suggestions in Brazilian Portuguese for WhatsApp conversations.

## 🚀 Features

- **AI-Powered Suggestions**: Generate 3 contextual message suggestions for any WhatsApp conversation
- **Brazilian Portuguese**: Optimized for Brazilian Portuguese with natural, friendly responses
- **Customer Service Focus**: Professional yet welcoming tone perfect for business communications
- **Chrome Extension Ready**: CORS configured for Chrome extension integration
- **Fast Response**: Uses lightweight llama3.2:1b model for quick suggestions
- **Unlimited Usage**: No API limits when running locally with Ollama

## 🛠️ Tech Stack

- **Backend**: Python 3.12 + FastAPI
- **AI Model**: Ollama with llama3.2:1b
- **Containerization**: Docker support
- **CORS**: Configured for Chrome extension integration

## 📋 Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai/) installed locally
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ollama-api-rest
```

### 2. Install Ollama and Pull the Model

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the llama3.2:1b model
ollama pull llama3.2:1b
```

### 3. Set Up Python Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Start Ollama Server

```bash
# Start Ollama server (in a separate terminal)
ollama serve
```

### 5. Run the API

```bash
# Activate virtual environment
source .venv/bin/activate

# Start the FastAPI development server
fastapi dev app.py
```

The API will be available at `http://localhost:8000`

## 🐳 Docker Setup

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t whatsapp-ai-assistant .

# Run the container
docker run -p 8000:8000 -p 11434:11434 whatsapp-ai-assistant
```

## 📖 API Usage

### Generate Message Suggestions

**Endpoint**: `POST /generate`

**Request Body**:
```json
{
  "prompt": "User's message or conversation context"
}
```

**Response**:
```json
{
  "suggestions": {
    "0": "Oiee, como vai? 🥰",
    "1": "Claro, temos sim!",
    "2": "Boa tarde, como posso ajudar? 🥰"
  },
  "original_message": "User's original message"
}
```

### Example cURL Request

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Cliente perguntando sobre produtos disponíveis"}'
```

## 🔧 Configuration

### Model Configuration

You can change the Ollama model by modifying the `OLLAMA_MODEL` variable in `app.py`:

```python
OLLAMA_MODEL = "llama3.2:1b"  # Change to your preferred model
```

### CORS Configuration

The API is configured to accept requests from:
- Chrome extension: `chrome-extension://bjkcdchdaniilnidjmgmekfaijipdhhe`
- All origins: `*` (for development)

Modify the CORS settings in `app.py` as needed for production.

## 🌐 Chrome Extension Integration

This API is designed to work with a Chrome extension for WhatsApp Web. The CORS configuration allows the extension to make requests to the local API.

## 📁 Project Structure

```
ollama-api-rest/
├── app.py              # FastAPI application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## 🔍 API Documentation

Once the server is running, visit `http://localhost:8000/docs` to see the interactive API documentation powered by FastAPI's automatic OpenAPI generation.

## 🎯 Use Cases

- **Customer Service**: Generate professional responses for business WhatsApp accounts
- **Personal Assistant**: Get suggestion for personal conversations
- **E-commerce**: Quick responses for product inquiries
- **Support Teams**: Standardized, friendly responses for support tickets

## 🛡️ Error Handling

The API includes error handling for:
- Ollama API connection issues
- Invalid request formats
- Model generation failures

## 🚀 Performance

- **Model**: llama3.2:1b (lightweight, fast inference)
- **Response Time**: Typically < 2 seconds for 3 suggestions
- **Memory Usage**: ~1-2GB RAM for the model

## 🔮 Future Enhancements

- [ ] Support for multiple languages
- [ ] Context awareness across conversations
- [ ] Custom tone/style configurations
- [ ] Message history integration
- [ ] Advanced prompt templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the [Ollama documentation](https://github.com/ollama/ollama)
- Review the [FastAPI documentation](https://fastapi.tiangolo.com/)

---

**Made by Danilo Alves for better WhatsApp conversations**