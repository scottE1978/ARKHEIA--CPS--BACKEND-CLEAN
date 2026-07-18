from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def root():
    return """
    <html>
        <head>
            <title>ARKHEIA-CPS Backend</title>
        </head>
        <body style="font-family: system-ui; max-width: 700px; margin: 40px auto;">
            <h1>ARKHEIA-CPS Backend</h1>
            <p>Status: <strong>Online</strong></p>
            <p>This is your backend service. Use the links below to explore the API:</p>
            <ul>
                <li><a href="/docs">API Docs (Swagger UI)</a></li>
                <li><a href="/billing/analyze">Billing endpoint (POST)</a></li>
                <li><a href="/contracts/analyze">Contracts endpoint (POST)</a></li>
            </ul>
        </body>
    </html>
    """
