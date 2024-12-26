import uvicorn
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from apitimer.timer import Timer, timer_registry

app = FastAPI()


@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"error": f"{exc.__class__.__name__}: {exc}"},
    )


@app.post("/timer/new")
def new_timer() -> dict[str, str]:
    tid = str(uuid.uuid4())
    timer = Timer(tid)
    timer_registry.register(timer)
    return {"tid": tid}


@app.post("/timer/start")
def start_timer(tid: str) -> None:
    timer_registry.get(tid).start()


@app.post("/timer/stop")
def stop_timer(tid: str) -> None:
    timer_registry.get(tid).stop()


@app.get("/timer/read")
def read_timer(tid: str) -> dict[str, float]:
    return {"time": timer_registry.get(tid).read().total_seconds()}


if __name__ == "__main__":
    uvicorn.run(app)
