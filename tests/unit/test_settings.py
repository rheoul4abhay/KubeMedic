import pytest
from pydantic import ValidationError

from kubemedic.settings import Settings


def test_settings_use_safe_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KUBEMEDIC_OPERATION_MODE", raising=False)
    monkeypatch.delenv("KUBEMEDIC_DECISION_PROVIDER_MODE", raising=False)

    settings = Settings()

    assert settings.operation_mode == "observe_only"
    assert settings.decision_provider_mode == "rules_only"


@pytest.mark.parametrize(
    "values", [{"operation_mode": "automatic"}, {"decision_provider_mode": "automatic"}]
)
def test_settings_with_unsupported_modes(values: dict[str, str]) -> None:
    with pytest.raises(ValidationError):
        Settings.model_validate(values)