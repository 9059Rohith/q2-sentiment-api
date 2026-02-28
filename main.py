"""
Question 2: FastAPI Sentiment Analysis with Structured Outputs
Endpoint: POST /comment
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from openai import OpenAI
import os
from typing import Literal

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# Request/Response Models
class CommentRequest(BaseModel):
    comment: str


class SentimentResponse(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Overall sentiment of the comment"
    )
    rating: int = Field(
        ge=1, le=5, description="Sentiment intensity (5=highly positive, 1=highly negative)"
    )


@app.post("/comment", response_model=SentimentResponse)
async def analyze_sentiment(request: CommentRequest):
    """
    Analyze sentiment of a comment using OpenAI's structured output.
    
    Args:
        request: Comment to analyze
        
    Returns:
        Structured sentiment analysis with sentiment and rating
    """
    try:
        # Use OpenAI's structured output feature
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """You are a sentiment analysis expert. Analyze the comment and return:
- sentiment: "positive", "negative", or "neutral"
- rating: 1-5 (5=highly positive, 3=neutral, 1=highly negative)

Guidelines:
- Positive: Praise, satisfaction, enthusiasm → rating 4-5
- Neutral: Factual, balanced, no strong emotion → rating 3
- Negative: Criticism, disappointment, frustration → rating 1-2"""
                },
                {
                    "role": "user",
                    "content": f"Analyze this comment: {request.comment}"
                }
            ],
            response_format=SentimentResponse,
        )
        
        return completion.choices[0].message.parsed
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API - POST /comment"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
