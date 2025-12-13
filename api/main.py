# api/main.py
import os
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from api.core.loader import load_artifacts
from api.routes.upload import router as upload_router

# -------------------------------------------------
# Logging
# -------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("netguard")

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "web/static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "web/templates")

# -------------------------------------------------
# App
# -------------------------------------------------
app = FastAPI(title="NetGuard AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Static & Templates
# -------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

# -------------------------------------------------
# Startup
# -------------------------------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("Starting NetGuard AI backend...")
    success = load_artifacts(app)

    app.state.artifacts_loaded = bool(success)

    if success:
        logger.info("Artifacts loaded successfully")
    else:
        logger.error("Artifacts failed to load. API will run but predictions will fail.")

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/health")
async def health():
    return {
        "status": "running",
        "artifacts_loaded": bool(getattr(app.state, "artifacts_loaded", False)),
    }

app.include_router(upload_router)
