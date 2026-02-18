"""HTTP client wrapper for cc_browser daemon."""

import httpx
from typing import Optional
from pydantic import BaseModel


class BrowserError(Exception):
    """Error from cc_browser daemon."""
    pass


class BrowserClient:
    """HTTP client for cc_browser daemon.

    Communicates with the cc_browser daemon on localhost:9280.
    """

    def __init__(self, port: int = 9280, timeout: float = 30.0):
        self.base_url = f"http://localhost:{port}"
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def _post(self, endpoint: str, data: Optional[dict] = None) -> dict:
        """Send POST request to daemon."""
        try:
            response = self._client.post(
                f"{self.base_url}{endpoint}",
                json=data or {}
            )
            result = response.json()

            if not result.get("success", False):
                raise BrowserError(result.get("error", "Unknown error"))

            return result
        except httpx.ConnectError:
            raise BrowserError(
                "Cannot connect to cc_browser daemon. "
                "Start it with: cc-browser daemon"
            )
        except httpx.TimeoutException:
            raise BrowserError(f"Request timed out after {self.timeout}s")

    def _get(self, endpoint: str) -> dict:
        """Send GET request to daemon."""
        try:
            response = self._client.get(f"{self.base_url}{endpoint}")
            result = response.json()

            if not result.get("success", False):
                raise BrowserError(result.get("error", "Unknown error"))

            return result
        except httpx.ConnectError:
            raise BrowserError(
                "Cannot connect to cc_browser daemon. "
                "Start it with: cc-browser daemon"
            )
        except httpx.TimeoutException:
            raise BrowserError(f"Request timed out after {self.timeout}s")

    def status(self) -> dict:
        """Get daemon and browser status."""
        return self._get("/")

    def start(self, profile_dir: Optional[str] = None, headless: bool = False) -> dict:
        """Launch browser."""
        data = {"headless": headless}
        if profile_dir:
            data["profileDir"] = profile_dir
        return self._post("/start", data)

    def stop(self) -> dict:
        """Close browser."""
        return self._post("/stop")

    def navigate(self, url: str) -> dict:
        """Navigate to URL."""
        return self._post("/navigate", {"url": url})

    def reload(self) -> dict:
        """Reload current page."""
        return self._post("/reload")

    def back(self) -> dict:
        """Go back."""
        return self._post("/back")

    def forward(self) -> dict:
        """Go forward."""
        return self._post("/forward")

    def snapshot(self, interactive: bool = True) -> dict:
        """Get page snapshot with element refs."""
        return self._post("/snapshot", {"interactive": interactive})

    def info(self) -> dict:
        """Get current page info (URL, title)."""
        return self._post("/info")

    def text(self, selector: Optional[str] = None) -> dict:
        """Get page text content."""
        data = {}
        if selector:
            data["selector"] = selector
        return self._post("/text", data)

    def html(self, selector: Optional[str] = None) -> dict:
        """Get page HTML."""
        data = {}
        if selector:
            data["selector"] = selector
        return self._post("/html", data)

    def click(self, ref: str) -> dict:
        """Click element by ref."""
        return self._post("/click", {"ref": ref})

    def type(self, ref: str, text: str) -> dict:
        """Type text into element."""
        return self._post("/type", {"ref": ref, "text": text})

    def press(self, key: str) -> dict:
        """Press keyboard key."""
        return self._post("/press", {"key": key})

    def hover(self, ref: str) -> dict:
        """Hover over element."""
        return self._post("/hover", {"ref": ref})

    def select(self, ref: str, value: str) -> dict:
        """Select dropdown option."""
        return self._post("/select", {"ref": ref, "value": value})

    def scroll(self, direction: str = "down", ref: Optional[str] = None) -> dict:
        """Scroll page or element."""
        data = {"direction": direction}
        if ref:
            data["ref"] = ref
        return self._post("/scroll", data)

    def screenshot(self, full_page: bool = False) -> dict:
        """Take screenshot (returns base64)."""
        return self._post("/screenshot", {"fullPage": full_page})

    def wait_for_text(self, text: str, timeout: int = 5000) -> dict:
        """Wait for text to appear."""
        return self._post("/wait", {"text": text, "timeout": timeout})

    def wait(self, ms: int) -> dict:
        """Wait for specified time."""
        return self._post("/wait", {"time": ms})

    def evaluate(self, js: str) -> dict:
        """Execute JavaScript."""
        return self._post("/evaluate", {"js": js})

    def fill(self, fields: list) -> dict:
        """Fill multiple form fields."""
        return self._post("/fill", {"fields": fields})

    def upload(self, ref: str, path: str) -> dict:
        """Upload file."""
        return self._post("/upload", {"ref": ref, "path": path})

    def tabs(self) -> dict:
        """List all tabs."""
        return self._post("/tabs")

    def tabs_open(self, url: Optional[str] = None) -> dict:
        """Open new tab."""
        data = {}
        if url:
            data["url"] = url
        return self._post("/tabs/open", data)

    def tabs_close(self, tab_id: str) -> dict:
        """Close tab."""
        return self._post("/tabs/close", {"tab": tab_id})

    def tabs_focus(self, tab_id: str) -> dict:
        """Focus tab."""
        return self._post("/tabs/focus", {"tab": tab_id})

    def close(self):
        """Close HTTP client."""
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# Convenience function for quick operations
def get_client(port: int = 9280) -> BrowserClient:
    """Get a browser client instance."""
    return BrowserClient(port=port)
