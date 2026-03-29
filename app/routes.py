from fastapi import APIRouter
from app.watcher import Watcher
from app import config
from app.schemas import StartRequest

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Auto File Organizer API is running"}


@router.post("/start")
def start(req: StartRequest):
    if config.is_running:
        return {"message": "Watcher already running"}

    watcher = Watcher()
    watcher.start(req.directory)

    config.watcher_instance = watcher
    config.watch_directory = req.directory
    config.is_running = True

    return {"message": f"Started watching {req.directory}"}


@router.post("/stop")
def stop():
    if not config.is_running:
        return {"message": "Watcher is not running"}

    config.watcher_instance.stop()

    config.watcher_instance = None
    config.is_running = False

    return {"message": "Watcher stopped"}


@router.get("/status")
def status():
    return {
        "running": config.is_running,
        "directory": config.watch_directory
    }