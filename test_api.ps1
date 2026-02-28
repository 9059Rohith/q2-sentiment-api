# Test Q2 Sentiment Analysis API

Write-Host "Testing Sentiment Analysis API..." -ForegroundColor Green
Write-Host ""

# Test with a sample comment
$body = @{
    comment = "This product is amazing! I love it so much!"
} | ConvertTo-Json

try {
    Write-Host "Sending request to http://localhost:8000/comment" -ForegroundColor Yellow
    $response = Invoke-RestMethod -Uri "http://localhost:8000/comment" -Method Post -Body $body -ContentType "application/json"
    
    Write-Host "`n✅ SUCCESS!" -ForegroundColor Green
    Write-Host "Sentiment: $($response.sentiment)" -ForegroundColor Cyan
    Write-Host "Rating: $($response.rating)/5" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "✅ Your API is working! Submit this URL:" -ForegroundColor Green
    Write-Host "http://localhost:8000/comment" -ForegroundColor White -BackgroundColor DarkGreen
} catch {
    Write-Host "`n❌ ERROR: Cannot connect to server" -ForegroundColor Red
    Write-Host "Make sure the server is running: .\start_server.ps1" -ForegroundColor Yellow
}
