#!/bin/bash

# Update system and install dependencies
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3-pip python3-venv mongodb nginx

# Create application user and directory
sudo useradd -r -m -s /bin/bash botopia
sudo mkdir -p /home/botopia/botopia-bot-api
sudo chown -R botopia:botopia /home/botopia/botopia-bot-api

# Copy application files
sudo cp -r /app/* /home/botopia/botopia-bot-api/

# Set up MongoDB
sudo mkdir -p /data/db
sudo chown -R mongodb:mongodb /data/db

# Create systemd service for MongoDB
sudo tee /etc/systemd/system/mongodb.service > /dev/null <<EOL
[Unit]
Description=High-performance, schema-free document-oriented database
After=network.target

[Service]
User=mongodb
ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Create systemd service for the FastAPI app
sudo tee /etc/systemd/system/botopia.service > /dev/null <<EOL
[Unit]
Description=Botopia FastAPI Application
After=network.target

[Service]
User=botopia
WorkingDirectory=/home/botopia/botopia-bot-api
Environment="PATH=/home/botopia/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="PYTHONPATH=/home/botopia/botopia-bot-api"
ExecStart=/home/botopia/.local/bin/uvicorn src.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Set up Nginx as reverse proxy
sudo tee /etc/nginx/sites-available/botopia > /dev/null <<EOL
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOL

# Enable and start services
sudo systemctl enable mongodb
sudo systemctl enable botopia
sudo systemctl enable nginx

sudo systemctl start mongodb
sudo systemctl start botopia
sudo systemctl start nginx

# Print status
sudo systemctl status mongodb
sudo systemctl status botopia
sudo systemctl status nginx
