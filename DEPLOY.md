# 🚀 Deploy Q2 to Render.com (FREE)

## Quick Deploy (5 minutes)

### 1. Create GitHub Repository
```powershell
cd c:\ga3\q5\q2_sentiment_analysis
git init
git add .
git commit -m "Q2 Sentiment Analysis API"
```

Push to GitHub:
- Create new repo: https://github.com/new
- Name it: `q2-sentiment-api`
- Then run:
```powershell
git remote add origin https://github.com/9059Rohith/q2-sentiment-api.git
git branch -M main
git push -u origin main
```

### 2. Deploy on Render

1. Go to https://render.com/
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select repository: `q2-sentiment-api`
5. Configure:
   - **Name:** `q2-sentiment-api`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** `Free`

6. **Environment Variables** (Click "Add Environment Variable"):
   ```
   OPENAI_API_KEY = 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
   ```

7. Click **"Create Web Service"**

### 3. Wait for Deployment (2-3 minutes)

You'll see logs like:
```
Building...
Installing dependencies...
Deploying...
Live ✅
```

Your URL will be: `https://q2-sentiment-api.onrender.com`

### 4. Test Your Deployed API

```powershell
curl -X POST https://q2-sentiment-api.onrender.com/comment `
  -H "Content-Type: application/json" `
  -d '{"comment":"This is amazing!"}'
```

### 5. Submit

**Submit:** `https://q2-sentiment-api.onrender.com/comment`

---

## Alternative: Quick ngrok Tunnel (Testing Only)

If you just want to test quickly without deploying:

1. **Download ngrok:** https://ngrok.com/download
2. **Start your local server:**
   ```powershell
   cd c:\ga3\q5\q2_sentiment_analysis
   .\start_server.ps1
   ```
3. **In another terminal:**
   ```powershell
   ngrok http 8000
   ```
4. **Copy the forwarding URL** (e.g., `https://abc123.ngrok.io`)
5. **Submit:** `https://abc123.ngrok.io/comment`

⚠️ **Note:** ngrok URLs expire when you close the tunnel!

---

## Files Created for Deployment

- `Procfile` - Tells Render how to start the server
- `runtime.txt` - Specifies Python version
- `render.yaml` - Infrastructure as code (optional)

---

## Troubleshooting

### "Service unavailable" after deployment
- Wait 1-2 minutes for cold start (free tier)
- Check Render logs for errors

### "API key invalid"
- Verify environment variable in Render dashboard
- Settings → Environment → Make sure OPENAI_API_KEY is set

### "Module not found"
- Check Build Logs in Render
- Verify all dependencies in requirements.txt

---

## Same Process for Q3, Q7, Q12

All four API endpoints (Q2, Q3, Q7, Q12) can be deployed the same way:
1. Push directory to separate GitHub repo
2. Deploy on Render with appropriate API key
3. Submit the deployed URL
