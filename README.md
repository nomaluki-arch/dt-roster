# Dragon Traveler Roster Codex

A static site. It reads two data files sitting next to it: tier-lists.json and
characters.json. Nothing is baked into the page.

## What's in this package
- index.html                          -> the whole app
- tier-lists.json                     -> tier data (complete)
- .github/workflows/update-data.yml   -> OPTIONAL: refreshes the data daily
- README.md                           -> this file

characters.json is NOT included. It's a large file (every unit's factions + classes)
and has to come from dtwiki directly. Two ways to get it in, below.

## Fastest way to a fully working site (5 min, no Action)
The site needs three files in the repo: index.html, tier-lists.json, characters.json.
This package has the first two; you add the third once:

1. Open  https://dtwiki.org/data/enUS/characters.json  in your browser.
2. Save it (Cmd+S / Ctrl+S) as exactly  characters.json  (raw JSON - if the dialog
   wants .txt or .html, change it back to .json).
3. In your repo: "Add file" -> "Upload files" -> drag in index.html, tier-lists.json,
   and characters.json -> "Commit changes".
4. Settings -> Pages -> Source "Deploy from a branch" -> main -> / (root) -> Save.
5. Open your Pages URL (hard-refresh: Cmd+Shift+R). Full roster, factions, classes, matrix.

## Optional: make it auto-update daily (the Action)
The web uploader hides dot-folders, so DON'T rely on dragging .github in - add the
workflow file directly on GitHub instead:

1. In your repo: "Add file" -> "Create new file".
2. In the filename box, type exactly:  .github/workflows/update-data.yml
   (typing the "/" characters creates the folders for you.)
3. Open update-data.yml from this package in a text editor, copy all of it, paste it
   into the GitHub editor, then "Commit changes".
4. Settings -> Actions -> General -> Workflow permissions -> "Read and write" -> Save.
5. Actions tab -> "Update Dragon Traveler data" -> "Run workflow".

From then on it refreshes tier-lists.json and characters.json every day on its own, so
new characters appear with no work from you.

Each visitor's owned marks and invest flags are saved in their own browser.
