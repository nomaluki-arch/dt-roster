# Dragon Traveler Roster Helper

A static site. It reads two data files sitting next to it: tier-lists.json and
characters.json. Nothing is baked into the page.

## What's in this package
- index.html                          -> the whole app
- tier-lists.json                     -> tier data (complete)
- .github/workflows/update-data.yml   -> OPTIONAL: refreshes the data daily
- README.md                           -> this file

characters.json is NOT included (it's large). The Factions tab and effect popovers also use
wyrms.json and status-effects.json. All three come from dtwiki - fetched automatically by the
Action, or added manually as below.

## Manual data files (if not using the Action)
Open each URL in your browser, save it with the exact filename, and upload it to the repo:
- https://dtwiki.org/data/enUS/characters.json      -> characters.json   (roster, factions, classes, kits)
- https://dtwiki.org/data/enUS/wyrms.json            -> wyrms.json        (faction dragons + evolutions)
- https://dtwiki.org/data/enUS/status-effects.json   -> status-effects.json (effect glossary)

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
