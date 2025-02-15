from typing import Any, Dict, Optional
from requests_oauthlib import OAuth2Session

class AuthHandler:
    def __init__(self, api: Any, clientId: str, clientSecret: str) -> None: ...
    def getCacheKey(self) -> str: ...
    def initParams(self) -> None: ...
    def isTokenDueRenewal(self) -> bool: ...
    def getAuthURL(self, redirectUri: str) -> str: ...
    def tokenToDict(self) -> Dict[str, Any]: ...
    def tokenSaver(self, oauth: OAuth2Session) -> str: ...
    def retrieveToken(self, response: str, state: Optional[str] = None, redirectUri: Optional[str] = None) -> str: ...
    def acquireNewToken(self) -> str: ...
    def getToken(self) -> str: ...
    def setTokenHeader(self, token: str) -> None: ...
    def checkHeaderTokens(self) -> None: ...