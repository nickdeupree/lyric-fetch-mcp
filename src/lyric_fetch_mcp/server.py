import os
from fastmcp import FastMCP
from lyricsgenius import Genius

mcp = FastMCP("Lyric-Fetch")

token = os.getenv("GENIUS_ACCESS_TOKEN")
genius = Genius(token)

@mcp.tool()
def get_song_lyrics(song_title: str, artist_name: str) -> str:
    """
        Fetches the lyrics of a song given its title and artist name.
        :param song_title: The title of the song.
        :param artist_name: The name of the artist.
    """
    if not genius:
        return "GENIUS_ACCESS_TOKEN environment variable not set."
    try:
        song = genius.search_song(song_title, artist_name)
        if song and song.lyrics:
            return song.lyrics
        else:
            return "Lyrics not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

@mcp.tool()
def get_artist_songs(artist_name: str, max_songs: int = 5, include_features: bool = False) -> str:
    """
        Fetches a list of songs by a given artist.
        :param artist_name: The name of the artist.
        :param max_songs: The maximum number of songs to fetch (default is 5).
        :param include_features: Whether to include featured songs (default is False).
    """
    if not genius:
        return "GENIUS_ACCESS_TOKEN environment variable not set."
    try:
        artist = genius.search_artist(artist_name, max_songs=max_songs, include_features=include_features)
        if artist and artist.songs:
            song_list = [f"Song: {song.title}, Album: ({song.album['name']})" for song in artist.songs]
            return "\n".join(song_list)
        else:
            return "No songs found for this artist."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
@mcp.tool()
def get_album_songs(album_title: str, artist_name: str) -> list:
    """
        Fetches a list of songs from a specific album by a given artist.
        :param album_title: The title of the album.
        :param artist_name: The name of the artist.
    """
    if not genius:
        return "GENIUS_ACCESS_TOKEN environment variable not set."
    try:
        album = genius.search_album(album_title, artist_name)
        print(album)
        if album and album.tracks:
            song_list = [f"{track[0]}: {track[1].title}" for track in album.tracks]
            return "\n".join(song_list)
        else:
            return "No songs found for this album."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def main() -> None:
    """Run the MCP server."""
    mcp.run()

if __name__ == "__main__":
    main()

