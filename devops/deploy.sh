#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Create a systemd service file for MongoDB
sudo tee /etc/systemd/system/mongodb.service > /dev/null <<EOL
[Unit]
Description=MongoDB Database Server
After=network.target

[Service]
User=mongodb
ExecStart=/usr/bin/mongod --config /etc/mongod.conf
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Create a systemd service file for the FastAPI app
sudo tee /etc/systemd/system/botopia.service > /dev/null <<EOL
[Unit]
Description=Botopia FastAPI Application
After=network.target

[Service]
User=botopia
WorkingDirectory=/home/botopia/botopia-bot-api
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
Environment="PYTHONPATH=/home/botopia/botopia-bot-api"

[Install]
WantedBy=multi-user.target
EOL

# Enable and start the services
sudo systemctl enable mongodb
sudo systemctl enable botopia
sudo systemctl start mongodb
sudo systemctl start botopia

# Print status
sudo systemctl status mongodb
sudo systemctl status botopia
