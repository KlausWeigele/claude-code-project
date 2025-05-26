"""
FastAPI backend application with CORS configuration for SvelteKit frontend.

This module provides a RESTful API with automatic documentation and CORS support
for seamless integration with the SvelteKit frontend application.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(
    title="AI-Powered SvelteKit Backend",
    description="Backend API with AI capabilities for SvelteKit frontend application",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],  # SvelteKit dev/preview ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response validation
class Item(BaseModel):
    """Model for item data structure."""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(BaseModel):
    """Model for creating new items."""
    name: str
    description: Optional[str] = None
    price: float

class TextAnalysisRequest(BaseModel):
    """Model for text analysis requests."""
    text: str
    analysis_type: str = "sentiment"  # sentiment, summary, keywords

class TextAnalysisResponse(BaseModel):
    """Model for text analysis responses."""
    original_text: str
    analysis_type: str
    result: str
    confidence: Optional[float] = None

class CodeGenerationRequest(BaseModel):
    """Model for code generation requests."""
    description: str
    language: str = "python"

class CodeGenerationResponse(BaseModel):
    """Model for code generation responses."""
    description: str
    language: str
    code: str
    explanation: str

# In-memory storage for demo purposes
items_db: List[Item] = [
    Item(id=1, name="Sample Item", description="This is a sample item", price=19.99),
    Item(id=2, name="Another Item", description="Another sample item", price=29.99),
]

@app.get("/")
async def root():
    """Root endpoint returning API information."""
    return {"message": "FastAPI backend is running!", "docs": "/docs"}

@app.get("/api/items", response_model=List[Item])
async def get_items():
    """Retrieve all items from the database."""
    return items_db

@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Retrieve a specific item by ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/api/items", response_model=Item)
async def create_item(item: ItemCreate):
    """Create a new item and add it to the database."""
    new_id = max([i.id for i in items_db], default=0) + 1
    new_item = Item(id=new_id, **item.dict())
    items_db.append(new_item)
    return new_item

@app.put("/api/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    """Update an existing item by ID."""
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_item = Item(id=item_id, **item.dict())
            items_db[i] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item by ID."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"Item {deleted_item.name} deleted successfully"}
    return {"error": "Item not found"}

@app.post("/api/ai/analyze-text", response_model=TextAnalysisResponse)
async def analyze_text(request: TextAnalysisRequest):
    """Analyze text using OpenAI for sentiment, summary, or keyword extraction."""
    try:
        if request.analysis_type == "sentiment":
            prompt = f"Analyze the sentiment of this text and provide a score from -1 (very negative) to 1 (very positive): '{request.text}'"
        elif request.analysis_type == "summary":
            prompt = f"Provide a concise summary of this text: '{request.text}'"
        elif request.analysis_type == "keywords":
            prompt = f"Extract the key topics and important keywords from this text: '{request.text}'"
        else:
            raise HTTPException(status_code=400, detail="Invalid analysis type")

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that provides accurate text analysis."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.3
        )

        result = response.choices[0].message.content.strip()
        
        return TextAnalysisResponse(
            original_text=request.text,
            analysis_type=request.analysis_type,
            result=result,
            confidence=0.95  # Mock confidence score
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {str(e)}")

@app.post("/api/ai/generate-code", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    """Generate code based on description using OpenAI."""
    try:
        prompt = f"Generate {request.language} code for: {request.description}. Provide clean, well-commented code."
        
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are an expert {request.language} programmer. Generate clean, efficient, and well-documented code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.2
        )

        code_result = response.choices[0].message.content.strip()
        
        # Generate explanation
        explanation_prompt = f"Explain how this {request.language} code works: {code_result}"
        explanation_response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful programming tutor. Explain code clearly and concisely."},
                {"role": "user", "content": explanation_prompt}
            ],
            max_tokens=200,
            temperature=0.3
        )

        explanation = explanation_response.choices[0].message.content.strip()
        
        return CodeGenerationResponse(
            description=request.description,
            language=request.language,
            code=code_result,
            explanation=explanation
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code generation failed: {str(e)}")

@app.get("/api/ai/demo-status")
async def get_ai_demo_status():
    """Check if AI services are available."""
    try:
        # Test OpenAI connection with a simple request
        test_response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'AI is working'"}],
            max_tokens=10
        )
        
        return {
            "status": "available",
            "model": "gpt-3.5-turbo",
            "message": "AI services are operational"
        }
    except Exception as e:
        return {
            "status": "unavailable",
            "error": str(e),
            "message": "AI services are currently unavailable"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)