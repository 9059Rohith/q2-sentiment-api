# Question 2: Sentiment Analysis API

## Setup

```bash
cd q2_sentiment_analysis
pip install -r requirements.txt
```

## Environment Variables

```bash
export OPENAI_API_KEY="your-key-here"
```

## Run

```bash
python main.py
```

## Test

```bash
curl -X POST http://localhost:8000/comment \
  -H "Content-Type: application/json" \
  -d '{"comment": "This product is amazing!"}'
```

## Expected Response

```json
{
  "sentiment": "positive",
  "rating": 5
}
```
