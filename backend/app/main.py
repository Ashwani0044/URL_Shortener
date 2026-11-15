from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import URL
from .schemas import URLCreate, URLResponse
from .services.shortener import encode_base62

# Create tables on startup (for local development)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pro URL Shortener API", version="1.0.0")

@app.post("/api/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    long_url_str = str(payload.long_url)
    
    # Check if URL already exists to avoid duplicate entries
    existing_url = db.query(URL).filter(URL.long_url == long_url_str).first()
    if existing_url:
        return existing_url

    # Insert placeholder record to generate auto-increment ID
    new_url = URL(long_url=long_url_str, short_code="temp")
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    # Generate Base62 short code from the database ID
    short_code = encode_base62(new_url.id)
    new_url.short_code = short_code
    db.commit()
    db.refresh(new_url)

    return new_url

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(URL).filter(URL.short_code == short_code).first()
    
    if not url_record:
        raise HTTPException(status_code=404, detail="Short URL not found")

    # Increment click analytics counter
    url_record.clicks += 1
    db.commit()

    return RedirectResponse(url=url_record.long_url, status_code=302)