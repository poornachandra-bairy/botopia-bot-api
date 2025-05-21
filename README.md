# Botopia Bot API

A FastAPI-based REST API for managing chatbots with MongoDB integration.

## Features

- Create and manage chatbots
- Store bot configurations in MongoDB
- RESTful API endpoints
- Docker support for deployment
- Environment-based configuration

## Installation

### Prerequisites

- Python 3.10+
- MongoDB
- Docker (optional)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/poornachandrabairy/botopia-bot-api.git
cd botopia-bot-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following content:
```
MONGODB_URI=mongodb://localhost:27017/botopia_db
PORT=8000
APP_ENV=development
```

5. Run the application:
```bash
PYTHONPATH=. uvicorn main:app --reload
```

### Docker Installation

1. Build and run the Docker container:
```bash
docker build -t botopia-bot-api .
docker run -d -p 8000:8000 botopia-bot-api
```

## API Endpoints

### Create Bot

```http
POST /api/bot
```

Request Body:
```json
{
    "bot_profile": {
        "name": "string",
        "bot_name": "string",
        "description": "string",
        "purpose": "string",
        "visibility": "string",
        "user_id": "string",
        "company_id": "string",
        "created_at": "2023-05-21T18:00:00+05:30",
        "updated_at": "2023-05-21T18:00:00+05:30"
    },
    "personality": {
        "tone": "string",
        "style": "string",
        "example_phrases": ["string"],
        "instructions": {
            "base_prompt": "string",
            "behavior_description": "string",
            "traits": ["string"]
        },
        "behaviors": {
            "argumentative": 0.1,
            "factual": 0.9,
            "correctness": 0.9,
            "sarcasm": 0.1,
            "rudeness": 0.1,
            "politeness": 0.9,
            "empathy": 0.8,
            "creativity": 0.7,
            "spontaneity": 0.6,
            "organization": 0.8
        },
        "skip_quotient": 0.5
    },
    "response_settings": {
        "response_format": "string",
        "fallback_message": "string"
    },
    "data_sources": {
        "upload_files": ["string"],
        "pasted_text_blocks": ["string"],
        "web_urls": ["string"],
        "external_integrations": {
            "google_drive_enabled": false,
            "notion_enabled": false,
            "slack_enabled": false
        }
    },
    "rag_settings": {
        "use_vector_store": false,
        "vector_store_type": "string",
        "restrict_answers_to_data": false,
        "allow_fallback_to_llm": false
    },
    "memory_settings": {
        "allow_memory": false,
        "memory_type": "string",
        "max_memory_length": 0
    },
    "tools_enabled": {
        "web_search": false,
        "code_execution": false,
        "custom_apis": ["string"]
    }
}
```

Response:
```json
{
    "message": "Bot created",
    "id": "string"
}
```

### Get Bots by User

```http
GET /api/bot/{user_id}
```

Response:
```json
[
    {
        "id": "string",
        "bot_profile": {
            "name": "string",
            "bot_name": "string",
            "description": "string",
            "purpose": "string",
            "visibility": "string",
            "user_id": "string",
            "company_id": "string",
            "created_at": "2023-05-21T18:00:00+05:30",
            "updated_at": "2023-05-21T18:00:00+05:30"
        },
        "personality": {
            "tone": "string",
            "style": "string",
            "example_phrases": ["string"],
            "instructions": {
                "base_prompt": "string",
                "behavior_description": "string",
                "traits": ["string"]
            },
            "behaviors": {
                "argumentative": 0.1,
                "factual": 0.9,
                "correctness": 0.9,
                "sarcasm": 0.1,
                "rudeness": 0.1,
                "politeness": 0.9,
                "empathy": 0.8,
                "creativity": 0.7,
                "spontaneity": 0.6,
                "organization": 0.8
            },
            "skip_quotient": 0.5
        },
        "response_settings": {
            "response_format": "string",
            "fallback_message": "string"
        },
        "data_sources": {
            "upload_files": ["string"],
            "pasted_text_blocks": ["string"],
            "web_urls": ["string"],
            "external_integrations": {
                "google_drive_enabled": false,
                "notion_enabled": false,
                "slack_enabled": false
            }
        },
        "rag_settings": {
            "use_vector_store": false,
            "vector_store_type": "string",
            "restrict_answers_to_data": false,
            "allow_fallback_to_llm": false
        },
        "memory_settings": {
            "allow_memory": false,
            "memory_type": "string",
            "max_memory_length": 0
        },
        "tools_enabled": {
            "web_search": false,
            "code_execution": false,
            "custom_apis": ["string"]
        }
    }
]
```

## Deployment

### Hostinger VPS

1. Install dependencies:
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv mongodb
```

2. Clone the repository:
```bash
git clone https://github.com/poornachandrabairy/botopia-bot-api.git
```

3. Set up environment:
```bash
chmod +x deploy.sh
./deploy.sh
```

4. Configure Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/botopia /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
