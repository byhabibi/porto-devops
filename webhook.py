from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deploy/', methods=['POST'])
def deploy():
	os.system("cd /home/devops/portofolio/ && git pull origin main && docker compose down && docker compose up -d --build")
	return "Deployed", 200
app.run(host="0.0.0.0", port=9001)
