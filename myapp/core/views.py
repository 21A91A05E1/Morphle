from django.http import HttpResponse
import os
from datetime import datetime
import subprocess

def htop_view(request):
    system_username = os.getenv("USER","codespace")
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1')

    content = f"""
    <h1>Name: [Jammu Siva Lakshmi Pravalika]</h1>
    <h2>User: {system_username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>TOP output:<br>{top_output}</pre>
    """
    return HttpResponse(content)
