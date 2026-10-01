from fastapi.testclient import TestClient

from kubemedic.api.main import app


def test_healthz_returns_ok() -> None:
    with TestClient(app) as client:
        response = client.get("/healthz")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def test_info_reports_safe_configurations() -> None:
    with TestClient(app) as client:
        response = client.get("/info")
        
    assert response.status_code == 200
    assert response.json() == {
        "name": "KubeMedic",
        "version": "0.1.0",
        "operation_mode": "observe_only",
        "decision_provider_mode": "rules_only",
    }