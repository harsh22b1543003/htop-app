from flask import Flask
import os
import time
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop_info():
    # Get system details
    name = "Your Name"
    username = os.getenv("USER", "codespace")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get htop output using top command
    top_output = subprocess.getoutput("top -b -n 1")

    # Format output as HTML
    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
