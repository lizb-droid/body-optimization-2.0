# Monthly Review — July 2026

**Cirque Snowbird DNF (Jul 11) → Phase 4 Rebuild for Cirque Alta (Aug 15)**

---

## Data Coverage

Six weekly reports cover the month: Jun 26 (pre-taper, no data), Jun 29 (Wk10, peak week), Jul 6 (Wk11, taper), Jul 13 (Wk12, race + Phase 4 pivot), Jul 27 (Wk14, mid-rebuild). Week 13 (Jul 20) has no report — a real gap, noted factually.

---

## The Month's Arc

**Jun 26–Jul 11 — Taper into a DNF.** Peak week (Jun 29) went well: 7/7 sessions, no GI issues on a 1,163ft trail run. A Jul 1 family emergency produced the worst-fueled day in the program's history (88g protein/1,379 kcal), but recovery was fast — race week (Jul 7–12) became the best nutrition week of the entire 12-week program. The race itself: **DNF, missed the 2-hour cutoff by ~10 minutes** at 8,000–11,000 ft in 90–95°F heat. Splits were progressive (23:06 → 27:49 → 37:15), tracking the steepening grade — clean pacing/fueling against a genuine altitude-heat ceiling, not an error.

**Jul 13 — same-day pivot.** A 7-point program overhaul was designed and approved the day of the debrief, targeting the exact deficit the race exposed: step-ups replacing walking lunges, Alta trail runs as the standing Saturday session, Wednesdays repurposed into climbing intervals, Bird Dog + Pallof Hold added for terrain stability, daily pelvic-floor rehab, Leki poles queued. Execution that day was strong.

**Jul 27 — the fixes are the ones slipping.** Both Saturday Alta runs since (Jul 18, 25) unconfirmed. The Jul 22 Wednesday climbing interval unconfirmed. Nutrition crashing specifically on Wednesdays (Jul 15 and Jul 22 identical: 98g protein/1,323 kcal) — the same day carrying the hardest new stimulus. A sleep problem diagnosed in concrete terms on Jul 13 (bedtime 60–90 min past target) is flagged again, unresolved, two weeks later.

**Other open threads:** ferritin test and NAC/OB clearance (both flagged urgent Jul 13) — no follow-up by Jul 27. Body comp held a stable 150–152 lb band all month (glycogen/water, not a concern).

---

## August Priorities

1. Actually execute the Jul 13 sleep fix (phone charger out) — it's a repeat only because it was never done.
2. Tuesday-night prep for Wednesday meals — landed twice now, same day as the hardest new training.
3. Run at Alta on non-race days, stacking with Saturdays; log every session, including a same-day note when one is skipped.
4. Close ferritin + NAC/OB clearance.
5. See app/program updates below.

---

## Proposed Program & App Updates — Ready to Apply

Two separate documents needed fixes this month; both are addressed below.

**`program/program-revisions.md`** — already corrected and pushed: race names fixed (Snowbird=Jul 11, Alta=Aug 15), Jul 13 Phase 4 items changed from "pending approval" to "approved/implemented," Saturday Alta and Wednesday interval entries now note their unconfirmed sessions honestly.

**`app/liz-program.jsx`** — this is the live app source, and it has NOT been touched since the original 17-week plan was written before the DNF. It still has the Alta/Snowbird names backwards *and* the old walking-lunges exercise. Concrete edits for the developer:

### 1. Race name swap (Alta ↔ Snowbird)

The app was built with Alta scheduled first; in reality Snowbird happened Jul 11 (DNF) and Alta is the upcoming Aug 15 race. Fix these fields:

| Location | Current | Change to |
|---|---|---|
| `PHASES` array, `p3` | `label: "Phase 3 · Cirque Alta"` (weeks 9–11) | `"Phase 3 · Cirque Snowbird"` |
| `PHASES` array, `p4` | `label: "Phase 4 · Snowbird"` (weeks 12–16) | `"Phase 4 · Rebuild for Cirque Alta"` |
| Week 12 object (`w12*`) | `phase: "Phase 3 · Cirque Alta"`, `title: "Week 12 — Cirque Alta"` | `"Phase 3 · Cirque Snowbird"`, `"Week 12 — Cirque Snowbird"` |
| `w12wed.info` | `"...Cirque Alta is Sunday July 11."` | `"...Cirque Snowbird is Saturday July 11."` (also corrects the weekday — Jul 11, 2026 is a Saturday; worth the developer double-checking why the race is currently placed under `w12sun`) |
| Race-day session (currently under `w12sun`) | `"⛰ CIRQUE ALTA — RACE DAY"` | `"⛰ CIRQUE SNOWBIRD — RACE DAY"` |
| Weeks 13–16 `phase` field (4 objects) | `"Phase 4 · Rebuild for Snowbird"` | `"Phase 4 · Rebuild for Cirque Alta"` |
| `w13` focus text | `"...You just raced Cirque Alta"` | `"...You just raced Cirque Snowbird"` |
| Week 17 object (`w17*`) | `phase: "Phase 4 · Cirque Snowbird"`, `title: "Week 17 — Cirque Snowbird"` | `"Phase 4 · Cirque Alta"`, `"Week 17 — Cirque Alta"` |
| `w17wed.info` | `"...Cirque Snowbird is Saturday August 15."` | `"...Cirque Alta is Saturday August 15."` |
| `w17sat.session` | `"⛰ CIRQUE SNOWBIRD — RACE DAY"` | `"⛰ CIRQUE ALTA — RACE DAY"` |

Note: the recurring **"Alta Series" / "Snowbird Series" Wednesday tune-up races** (Wk12, 13, 16, 17) are a different, correctly-named local race series and do not need to change — only the `CIRQUE ALTA` / `CIRQUE SNOWBIRD` goal-race labels and their surrounding phase text.

### 2. Walking Lunges → Step-up with Knee Drive (already "approved & implemented" Jul 13, never patched into the app)

`Step-up with Knee Drive` already exists in `WORKOUTS.lowerB` / `lowerBLight` and in `REST_TIMES` (90s) — no new lookup entry needed, just reuse it in the Lower A variants:

| Array | Current entry | Change to |
|---|---|---|
| `WORKOUTS.lowerA` | `["Walking Lunges","3×12 ea"]` | `["Step-up with Knee Drive","3×10 ea"]` |
| `WORKOUTS.lowerAPower` | `["Walking Lunges","3×10 ea"]` | `["Step-up with Knee Drive","3×10 ea"]` |
| `WORKOUTS.lowerALight` | `["Walking Lunges","2×10 ea"]` | `["Step-up with Knee Drive","2×10 ea"]` |

(These three arrays are shared across every week that references `lowerA`/`lowerAPower`/`lowerALight`, so one edit each fixes it program-wide. The now-unused `"Walking Lunges":120` line in `REST_TIMES` can be left or removed.)

### 3. Add Bird Dog + Pallof Hold to Lower A (approved Jul 13, not yet in the app)

Add to `WORKOUTS.lowerA`, `lowerAPower`, and `lowerALight` (after Copenhagen Plank):
```
["Bird Dog","3×8 ea"], ["Pallof Hold","3×20s ea"]
```
And add to `REST_TIMES`:
```
"Bird Dog":45,"Pallof Hold":45
```
(45s matches the existing rest time for Dead Bug / Copenhagen Plank — same stability-work category.)

### 4. Explicit Alta labeling for the two remaining build Saturdays

| Day | Current | Change to |
|---|---|---|
| `w15sat` (Aug 2) | `session:"Trail 65–70 min + full fuel"`, `info:"Practice exact Cirque Snowbird fueling."` | `session:"Alta Trail — 65 min, race-pace uphill sections"`, `info:"Fuel exactly as Cirque Alta race day. Race-pace effort on the steep sections for 15–20 min."` |
| `w16sat` (Aug 9) | `session:"Trail 60–65 min moderate"`, `info:"Moderate effort. Don't empty the tank."` | `session:"Alta Trail — FINAL altitude session, 60–65 min moderate"`, `info:"Last altitude-adaptation stimulus before Cirque Alta. Don't empty the tank this close to race day."` |

### Not an action item, for context

There's no remaining "non-race Wednesday" left on the calendar between now and Cirque Alta (Wk15 = Brighton race, Wk16 = Alta Series race, Wk17 = shakeout) — so the "run at Alta on non-race days" idea has nowhere left to apply this block. It's still worth keeping as a standing rule for future blocks.

---

*Monthly Data Analyst — generated July 2026. Sources: tracking/weekly-review-2026-06-26.md, tracking/week-2026-06-29.md, tracking/week-2026-07-06.md, tracking/weekly-review-2026-07-13.md, tracking/weekly-review-2026-07-27.md, app/liz-program.jsx. Week of Jul 20 has no report in either the local or GitHub archive.*
