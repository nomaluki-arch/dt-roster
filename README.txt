Dragon Traveler Roster - run it on your desktop
===============================================

You need Python 3. It's already installed on macOS.

EASIEST (macOS): double-click  run.command
  - First time only: if macOS says it can't verify the developer, right-click
    run.command -> Open -> Open. (You only do this once.)
  - A Terminal window opens, the data downloads, and your browser opens the site.
  - To stop: press Ctrl+C in that Terminal window, or just close it.

ANY OS (also the reliable fallback):
  1. Open a Terminal.
  2. Go into this folder:  drag the folder onto the Terminal window, then press Enter,
     or type  cd  and the folder path.
  3. Run:  python3 serve.py
  4. Your browser opens at http://localhost:8000  (if not, open that address yourself).
  5. Stop with Ctrl+C.

What it does
  Every time you run it, it downloads the latest tier-lists.json and characters.json
  from dtwiki (the full files) into this folder, then serves the page so it can read
  them. Nothing is stored inside the page - it always reflects those two files.
  Your owned marks and invest flags are saved by your browser.

No internet? It serves whatever tier-lists.json / characters.json are already here.

Windows note: same steps as "ANY OS". If  python3  isn't found, install Python 3 from
python.org and tick "Add Python to PATH", then use  python serve.py .
