#!/usr/bin/env python3
"""Dragon Traveler Roster — local launcher.

Each run: downloads the latest tier-lists.json and characters.json into this folder
(full files, no size limit — this runs on your machine), then serves the folder over
http so index.html can read them, and opens your browser. Ctrl+C to stop.
"""

import functools
import http.server
import os
import socketserver
import threading
import urllib.request
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

SOURCES = {
    "tier-lists.json": "https://dtwiki.org/data/global/tier-lists.json",
    "characters.json": "https://dtwiki.org/data/enUS/characters.json",
    "wyrms.json": "https://dtwiki.org/data/enUS/wyrms.json",
    "status-effects.json": "https://dtwiki.org/data/enUS/status-effects.json",
    "gear.json": "https://dtwiki.org/data/enUS/gear.json",
}


def refresh():
    print("Refreshing data files...")
    for fname, url in SOURCES.items():
        try:
            req = urllib.request.Request(url, headers={"User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(fname, "wb") as f:
                f.write(data)
            print(f"  {fname}: {len(data):,} bytes")
        except Exception as e:  # offline / blocked -> keep any existing copy
            have = os.path.exists(fname)
            print(f"  {fname}: download failed ({e}); "
                  + ("using existing copy." if have else "no local copy yet."))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()


def serve():
    handler = functools.partial(NoCacheHandler, directory=HERE)
    for port in range(8000, 8010):
        try:
            httpd = socketserver.TCPServer(("", port), handler)
            break
        except OSError:
            continue
    else:
        print("Couldn't find a free port between 8000-8009.")
        return
    url = f"http://localhost:{port}/"
    print(f"\nServing at {url}\nPress Ctrl+C to stop.\n")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    refresh()
    serve()
