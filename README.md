# Body Optimization 2.0

Liz's workout app, with the program, profile, nutrition guides and tracking it's built on.

This is the next version of [body-optimization](https://github.com/lizb-droid/body-optimization). That repository and its app stay as they are; this one is where new work happens.

**App on your phone:** https://lizb-droid.github.io/body-optimization-2.0/app/
(Works once GitHub Pages is on: repository Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`.)

## What's here

```
body-optimization-2.0/
├── app/          ← the workout app (single-file web app)
│   ├── index.html        home, workout overview, guided session, journal, macros, progress
│   ├── COACH-SCRIPT.md   every line the coach says, ready to rewrite
│   ├── audio/coach/      the coach's recorded lines (Heart voice)
│   ├── manifest.json     home-screen app settings
│   ├── icons/
│   └── data/             backup.json lands here when you tap Save
├── .claude/agents/ ← coach and nutritionist agents
├── design/
│   └── DESIGN.md ← the 2.0 design: colors, type, buttons, every screen
├── profile/      ← athlete profile
├── program/      ← 12-week hypertrophy program and revisions
├── references/   ← original program, nutrition, race and cycle guides
├── tracking/     ← daily log template, weekly and monthly reviews
└── tools/        ← keep the app in step with the script (see below)
```

## The app

- **Home:** swipeable day cards with a week strip; completed days get a checkmark.
- **Workout overview:** the whole session at a glance, with the real time for each section.
- **Guided session:** each section opens with a preview that walks through its movements, then every set, rest and switch runs on one clock. Tap to pause, swipe for the next or previous section, double-tap to replay.
- **Logging:** reps and weight beside the timer (weight in 2.5 lb steps); a set is logged when its timer finishes. Track results opens the journal; Journal opens personal records.
- **Coach voice and sounds:** the coach talks you through the warm-up, each section and every set in a recorded natural voice (Kokoro "Heart", free and open source), with a coach whistle at 10 seconds left. A line without a recording falls back to the phone's voice.

Data stays on the phone and backs up to `app/data/backup.json` here when you tap Save. On first open the app copies your history from the original app, read-only; it never writes to the original repository.

## After changing the coach script or the program

Two steps bring the app up to date (in Claude Code, ask: "sync the coach script and re-record the coach voice"):

1. `python3 tools/sync-coach-script.py` copies `app/COACH-SCRIPT.md` into the app.
2. `python3 tools/record-coach-voice.py` records any new lines and removes ones no longer used. First run downloads the free voice model (about 90 MB, kept out of git); needs `pip install kokoro-onnx soundfile`, ffmpeg, Node and Playwright.

## Next up

- Fix the Save button so backups go to this repository
- End-of-workout summary, and dark Macros and Progress pages
