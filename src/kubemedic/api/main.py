from fastapi import FastAPI

from kubemedic.settings import Settings

settings = Settings()
app = FastAPI(title="KubeMedic", version="0.1.0")

@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/info")
def info() -> dict[str, str]:
    return {
        "name": app.title,
        "version": app.version,
        "operation_mode": settings.operation_mode,
        "decision_provider_mode": settings.decision_provider_mode,
    }