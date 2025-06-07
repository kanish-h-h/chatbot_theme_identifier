## Phase 0: Foundation & Setup (1-2 days)

### Errors
- package the backend and app directory 
  ```bash
  touch backend/__init__.py backend/app/__init__.py
  ```
  ```
  ```

- setup the `pyproject.toml` at root
  - all dependencies in one place
  - certain packages work everywhere `from backend.app.main import app` works everywhere
  - better tool integration
    ```bash
    # these will all work from root
    pytest tests/
    black backend
    ruff check .
    ```

  - installation flow
    - from project root 
      ```bash
      pip install e .  # editable install
      pip install e ".[dev]"  # with dev dependencies
      ```

    - for production
      ```bash
      pip install .  # normal install
      ```

  - Special case: multiple packages
    ```bash
    chatbot_theme/
    |--backend/
    |--frontend/
    |--pyproject.toml   # contains both packages
    ```

    update `pyproject.toml`
    ```toml
    [tool.setuptools]
    packages = ["backend", "frontend"]
    ```

    ```
    ```
    ```
    ```
    ```
      ```
      ```
      ```
      ```
    ```
    ```


### Objective: Establish core infrastructure and development environment

### Tasks:
1. **Project Initialization**
   ```bash
   mkdir doc-chatbot && cd doc-chatbot
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
   
2. **Directory Structure Setup**
   ```bash
   mkdir -p backend/app backend/data tests docs demo
   touch .gitignore README.md
   touch backend/Dockerfile backend/requirements.txt
   touch backend/app/__init__.py
   ```

3. **Git Configuration (`.gitignore`)**
   ```gitignore
   venv/
   __pycache__/
   *.pyc
   .env
   backend/data/*
   !backend/data/.gitkeep
   chroma_db/
   .DS_Store
   ```

4. **Core Dependencies (`backend/requirements.txt`)**
   ```python
   fastapi==0.111.0
   uvicorn==0.29.0
   python-multipart==0.0.9
   PyPDF2==3.0.1
   pdf2image==1.17.0
   pytesseract==0.3.10
   openai==1.30.1
   chromadb==0.5.0
   python-dotenv==1.0.1
   tqdm==4.66.4
   ```

5. **Environment Configuration (`.env`)**
   ```env
   OPENAI_API_KEY=your_api_key_here
   EMBEDDING_MODEL=text-embedding-3-small
   OCR_ENGINE=tesseract
   CHUNK_SIZE=1000
   CHUNK_OVERLAP=200
   ```

6. **Minimal FastAPI Setup (`backend/app/main.py`)**
   ```python
   from fastapi import FastAPI
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   app = FastAPI(
       title="DocChatbot API",
       description="Document Analysis Chatbot",
       version="0.1.0"
   )
   
   @app.get("/")
   def health_check():
       return {"status": "active", "version": app.version}
   ```

7. **Docker Setup (`backend/Dockerfile`)**
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   
   # Install system dependencies for OCR
   RUN apt-get update && apt-get install -y \
       tesseract-ocr \
       libtesseract-dev \
       poppler-utils \
       && rm -rf /var/lib/apt/lists/*
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

8. **Basic Test (`tests/test_health.py`)**
   ```python
   from fastapi.testclient import TestClient
   from backend.app.main import app
   
   client = TestClient(app)
   
   def test_health_check():
       response = client.get("/")
       assert response.status_code == 200
       assert response.json()["status"] == "active"
   ```

### Verification:
1. Start development server:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```
2. Visit `http://localhost:8000` → Should see health status
3. Run tests:
   ```bash
   pytest tests/
   ```
4. Build Docker image:
   ```bash
   docker build -t docchatbot-backend .
   ```

### Phase 0 Deliverables:
- [x] Project directory structure
- [x] Virtual environment setup
- [x] Core dependencies installed
- [x] Basic API endpoint
- [x] Docker configuration
- [x] Test suite foundation
- [x] Environment management

## Next Steps:
1. Set up ChromaDB instance
2. Implement PDF processing pipeline
3. Create document ingestion endpoint
4. Build vector embedding system

Let me know when you're ready to proceed to Phase 1 (Document Processing Pipeline) and I'll provide the detailed implementation plan!
