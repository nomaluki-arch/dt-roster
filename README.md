# Dragon Traveler Roster Codex

A collection tracker + tier-list dashboard. It's a single static page that reads its
data from two JSON files next to it; a scheduled GitHub Action refreshes those files so
new characters appear on their own. No data is baked into the page.

## Files
- `index.html` — the whole app (no build step). Reads `./tier-lists.json` and `./characters.json`.
- `tier-lists.json` — seed data so the site works immediately; the Action keeps it fresh.
- `.github/workflows/update-data.yml` — downloads fresh data daily and commits it.
- (`characters.json` is created by the Action on its first run — it holds every unit's
  faction and class, which is what powers the faction/class filters and the matrix.)

## Setup (about 5 minutes)
1. Create a **public** repo and upload these files, keeping the folder layout — the
   workflow must stay at `.github/workflows/update-data.yml`.
2. **Settings -> Actions -> General -> Workflow permissions** -> choose
   **Read and write permissions** -> Save. (Without this the Action can't commit the data.)
3. **Settings -> Pages** -> Source *Deploy from a branch* -> Branch `main` -> `/ (root)`
   -> Save. After a minute it shows your site URL.
4. **Actions** tab -> enable workflows if asked -> **Update Dragon Traveler data** ->
   **Run workflow**. In ~30s it commits `tier-lists.json` and a full `characters.json`.
5. Open your Pages URL. Every unit now has its faction and class.

From then on it refreshes daily on its own. Your owned marks and invest flags are stored
in your browser, per device.

## Manual data update (if you'd rather not use the Action)
Open `https://dtwiki.org/data/enUS/characters.json` in your browser, save it as
`characters.json`, and upload it to the repo. Same for
`https://dtwiki.org/data/global/tier-lists.json`. The page always reads whatever is in
these two files.

## Change the update time
Edit the `cron` line in `update-data.yml` (UTC).
