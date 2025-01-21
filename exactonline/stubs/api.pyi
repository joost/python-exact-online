from typing import Any, Dict, Optional, Tuple
import logging

class Config:
    def __init__(self, cache_handler: Optional[Any] = None, logger: Optional[logging.Logger] = None) -> None: ...
    def configureLogger(self, name: str, level: int = logging.DEBUG, format: str = '%(asctime)s %(levelname)s %(message)s') -> logging.Logger: ...
    def setLogLevel(self, level: int) -> None: ...

class ExactOnlineAPI:
    def __init__(self, client_id: str, client_secret: str, stall_if_rate_limit_exceeded: bool = True, config: Config = Config()) -> None: ...
    def checkDivision(self) -> None: ...
    def get(self, url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Tuple[int, Dict[str, str], Any]: ...
    def post(self, url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, files: Optional[Dict[str, Any]] = None) -> Tuple[int, Dict[str, str], Any]: ...
    def put(self, url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Tuple[int, Dict[str, str], Any]: ...
    def delete(self, url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Tuple[int, Dict[str, str], Any]: ...