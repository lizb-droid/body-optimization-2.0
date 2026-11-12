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
│   ├── manifest.json     home-screen app settings
│   ├── icons/
│   └── data/             backup.json lands here when you tap Save
├── design/
│   └── DESIGN.md ← the 2.0 design: colors, type, buttons, every screen
├── profile/      ← athlete profile
├── program/      ← 12-week hypertrophy program and revisions
├── references/   ← original program, nutrition, race and cycle guides
└── tracking/     ← daily log template, weekly and monthly reviews
```

## The app

- **Home:** swipeable day cards with a week strip; completed days get a checkmark.
- **Workout overview:** the whole session at a glance, with the real time for each section.
- **Guided session:** each section opens with a preview that walks through its movements, then every set, rest and switch runs on one clock. Tap to pause, swipe for the next or previous section, double-tap to replay.
- **Logging:** reps and weight beside the timer (weight in 2.5 lb steps); a set is logged when its timer finishes. Track results opens the journal; Journal opens personal records.
- **Coach voice and sounds:** spoken coaching, a 10-second warning sound, and a choice of voice.

Data stays on the phone and backs up to `app/data/backup.json` here when you tap Save. On first open the app copies your history from the original app, read-only; it never writes to the original repository.

## Next up

- New coach and nutritionist
- Wire Liz's coach script into the app (`app/COACH-SCRIPT.md`)
- Natural coach voice
- End-of-workout summary, and dark Macros and Progress pages
