from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>Django on AKS</title>
        </head>
        <body style="
            font-family: 'Segoe UI', Arial, sans-serif;
            text-align: center;
            margin-top: 80px;
            background: linear-gradient(to right, #e3f2fd, #ffffff);
        ">
            <div style="
                background: white;
                padding: 40px;
                margin: auto;
                width: 60%;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            ">
                <h1 style="color: #1976D2; font-size: 36px;">
                    🚀 Django App Deployed on AKS
                </h1>

                <p style="font-size: 20px; color: #555;">
                    This application is successfully deployed using a modern DevOps pipeline.
                </p>

                <hr style="margin: 20px 0;">

                <p style="font-size: 18px; color: #333;">
                    ⚙️ <b>Technologies Used:</b><br><br>
                    GitHub Actions (CI/CD) <br>
                    Azure Container Registry (ACR) <br>
                    Azure Kubernetes Service (AKS)
                </p>

                <p style="
                    margin-top: 20px;
                    font-size: 18px;
                    color: green;
                    font-weight: bold;
                ">
                    ✅ Deployment Successful | Pipeline Running Smoothly
                </p>

                <p style="margin-top: 30px; font-size: 14px; color: gray;">
                    Built & deployed by Cloud Engineer 🚀
                </p>
            </div>
        </body>
        </html>
    """)