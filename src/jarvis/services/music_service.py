
import webbrowser

from jarvis.data.music_library import MUSIC_LIBRARY


class MusicService:
    def play(self, song_name: str) -> bool:
        song_name = song_name.strip().lower()
        url = MUSIC_LIBRARY.get(song_name)

        if not url:
            return False

        return webbrowser.open(url)
