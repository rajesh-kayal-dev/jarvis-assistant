
import webbrowser


class BrowserService:
    WEBSITES = {
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com",
    }

    def open_website(self, name: str) -> bool:
        url = self.WEBSITES.get(name.lower().strip())

        if not url:
            return False

        return webbrowser.open(url)
