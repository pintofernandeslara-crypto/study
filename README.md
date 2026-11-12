# FHNW Study

Installable study app (summaries, flashcards, quizzes) for FHNW semester 1.
Works on iPhone and Mac: phone layout with a bottom tab bar, Mac layout with a sidebar. Works offline once installed.

- `index.html` — the app
- `data.json` — your study content (rebuilt by the after-class updates)
- `manifest.webmanifest`, `sw.js`, `icons/` — what makes it installable and offline-capable
- `tools/build_data.py` — rebuilds `data.json` from the study hub database export

## Install
- iPhone: open the app's web address in Safari → Share → Add to Home Screen.
- Mac: open it in Safari → File → Add to Dock (or Chrome → install icon in the address bar).

Card progress and quiz scores are saved on each device separately.
