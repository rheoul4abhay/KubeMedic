from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="KUBEMEDIC_")

    operation_mode: Literal["observe_only"] = "observe_only"
    decision_provider_mode: Literal["rules_only"] = "rules_only"