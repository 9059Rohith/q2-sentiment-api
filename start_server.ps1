# Start Q2 Sentiment Analysis API Server

Write-Host "Starting Sentiment Analysis API..." -ForegroundColor Green

# Set API key
$env:OPENAI_API_KEY = "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"

Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -q fastapi uvicorn openai pydantic

Write-Host "`nStarting server on http://localhost:8000" -ForegroundColor Green
Write-Host "Endpoint: POST http://localhost:8000/comment" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server`n" -ForegroundColor Yellow

python main.py
