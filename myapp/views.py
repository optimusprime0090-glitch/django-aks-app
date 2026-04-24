from django.http import HttpResponse
import socket
import datetime
import os

def home(request):
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Env variables (CI/CD se set karega)
    version = os.getenv("APP_VERSION", "v1.0")
    environment = os.getenv("ENVIRONMENT", "Development")

    return HttpResponse(f"""
    <html>
    <head>
        <title>Cloud Dashboard</title>
    </head>
    <body style="
        font-family: 'Segoe UI';
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
        text-align: center;
        margin-top: 50px;
    ">

        <h1>🚀 Cloud Status Dashboard</h1>

        <div style="
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 12px;
            width: 50%;
            margin: auto;
        ">

            <h2 style="color: #00e676;">✅ Application Running</h2>

            <p><b>🌐 Host:</b> {hostname}</p>
            <p><b>⏱ Time:</b> {current_time}</p>
            <p><b>📦 Version:</b> {version}</p>
            <p><b>🌍 Environment:</b> {environment}</p>

        </div>

        <p style="margin-top: 30px; color: #ccc;">
            Powered by Django + AKS + CI/CD 🚀
        </p>

    </body>
    </html>
    """)


def health(request):
    return HttpResponse("OK", status=200)