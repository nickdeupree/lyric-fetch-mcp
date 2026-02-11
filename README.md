# lyric-fetch-mcp

A small MCP (Model Context Protocol) server that fetches song lyrics and artist/album song lists using the Genius API via `lyricsgenius` and exposes them as FastMCP tools.

## Overview ✅

- **Purpose:** Provide simple, reusable tools for retrieving song lyrics and lists of songs by artist/album for LLMs or other tooling that can call MCP tools.
- **Tools exposed:** `get_song_lyrics(song_title, artist_name)`, `get_artist_songs(artist_name, max_songs=5)`, `get_album_songs(album_title, artist_name)`
- **Server framework:** Uses `fastmcp` to register the tools and run the MCP server.

## Installation (after publishing to `uv`) 🔧

Once you publish this package to a registry that `uv` can reach (e.g., PyPI or a private index), users can install and run it locally with `uv`:

- Install the published package:

  - `uv add lyric-fetch-mcp`

- Run the installed tool directly (ephemeral environment):

  - `GENIUS_ACCESS_TOKEN="<your_token>" uvx lyric-fetch-mcp`

- Or add it as a dependency to your `uv` project and run:

  - `uv add lyric-fetch-mcp`
  - `uv run -- lyric-fetch-mcp`

> Note: `uvx` runs a tool in an ephemeral environment created by `uv` (similar to `pipx`).

## Running locally (developer)

- One-off run with an env var:

  - `GENIUS_ACCESS_TOKEN="your_token_here" python -m lyric_fetch_mcp.server`

- Install locally for development and run the script:

  - `python -m pip install -e .`
  - `lyric-fetch-mcp`  (after install)

## Environment

- Requires a valid `GENIUS_ACCESS_TOKEN` environment variable.
- For production/CI, store the token in your CI/host secret manager (GitHub Secrets, Docker secrets, etc.).

## CLI examples

- Fetch lyrics quickly from the shell (one-line):

  - `GENIUS_ACCESS_TOKEN="your_token" python -c 'from lyric_fetch_mcp.server import get_song_lyrics; print(get_song_lyrics("Sofia","Clairo"))'`

## Contributing & Publishing

- The project uses `uv_build` as the PEP 517 backend — build with `uv build` and publish with `uv publish`.
- Please follow the repository's contribution guidelines and add tests for any new behavior.

## License

- MIT — see `LICENSE` for details.
