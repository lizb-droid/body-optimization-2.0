# Body Optimization 2.0 — Design

The design of the workout app in `app/`. Dark, full-screen, built for one thumb at the gym. Patterns are adapted from Ladder (guided, timed sessions) in Liz's own palette.

The values here match `app/index.html`. When one changes, update the other.

---

## Principles

- **The clock runs the session.** Every set, rest and switch has a fixed time, so a workout takes what it says it takes.
- **One thing on screen at a time.** Each screen answers "what am I doing now?" and nothing else.
- **Times shown are real.** Every duration is computed from the session timer, never estimated separately.
- **Consistent controls.** Every button and link looks and reads the same way (see Buttons and links).

---

## Color

| Token | Value | Use |
|---|---|---|
| `--pink` | `#FF9BD7` | Main accent: active states, work timer, highlights, primary buttons |
| `--pink-on` | `#5c1038` | Text on pink buttons |
| `--pink-m` | `rgba(255,155,215,.15)` | Pink tint for selected rows and chips |
| `--ind` | `#4D5FFF` | Completed (checkmarks, "Completed" button), rest timer |
| `#9aa5ff` | light indigo | "Up next" text and labels on dark |
| `--yel` | `#DADF0A` | Finisher: timer, section line, labels |
| `--coral` | `#FF6230` | Race days |
| `--dk0` | `#0f0f0f` | App background |
| `--dk1` / `--dk2` | `#141414` / `#1c1c1c` | Raised surfaces, sheets |
| `#000` | black | Workout overview background |

Timer colors by step: **work** pink, **rest** and **warm-up** indigo, **finisher** yellow, **set up / switch** light gray.

Text on dark: white for primary, `#aaa`–`#999` for secondary, `#666`–`#777` for hints.

---

## Type

| Role | Font | Weight | Where |
|---|---|---|---|
| Display | Archivo, expanded (width 112–125%) | 800 | Day card names (uppercase), section titles, set titles |
| Numbers | Barlow Condensed | 800 | Countdown timers, reps, weight |
| Clock | Barlow Condensed | 500 | Elapsed time and % at the top of a session (24px) |
| Body | Roboto | 400–600 | Everything else |

Google Fonts: `Roboto:wght@400;500;600`, `Archivo:wdth,wght@125,800`, `Barlow+Condensed:wght@500;700;800`.

Key sizes:

| Element | Size |
|---|---|
| Day card name | up to 50px, shrinks so the longest word fits |
| Section title (session) | 38px |
| Set title ("6x Barbell Back Squat") | 28–36px |
| Countdown | 52–68px |
| Body text | 15–17px |
| Buttons and links | 16px (`--cta-size`) |

---

## Buttons and links

- **One style:** 16px, regular weight (`--cta-size`, `--cta-weight: 400`), set in one place.
- **Sentence case:** "Start workout", "Track results", "Skip section". Only proper names and abbreviations keep capitals ("Add PR").
- **Primary button:** full-width pink pill, 54–60px tall. "Completed" state is indigo with white text.
- **Secondary:** outlined pill or plain text link.
- Pink for the active or highlighted choice; light gray for the rest.

---

## Layout

- Phone first, 390px reference width, 16–20px side margins.
- Safe areas respected at the top (notch) and bottom (home bar).
- Floating bars at the bottom: rounded 22px, 68px tall, thin white border at 12%, dark background at 86% with blur.

---

## Screens

### Home
- **Header:** "Week 10" title, Beta tag, block and dates underneath, **Save** on the right.
- **Week strip:** Mon–Sun, date under each day. Done days show an indigo circle with a white check; today is bold; the day in view has a soft gray highlight. Swipes left and right between weeks.
- **Day cards:** one large card per day, swipeable across the whole program, with the neighbouring cards peeking at the edges. Day tag top left ("Today" in pink), indigo check top right when done, workout name large at the bottom with "48 min · Shoulders + Chest" under it. Placeholder background until photos exist (`DAY_IMAGES` in the app).
- **Main menu:** floating bar (see Layout) with Workout, Macros, Progress; icon beside the label; active tab pink.

### Workout overview (tap a day card)
- Full-screen, black. Top: close button, total time centered, sound button on the right.
- Day, workout name, focus.
- Sections: **Warm Up**, **Strength**, **Superset A/B/C**, **Finisher**. Each header shows its real duration. Sections with more than one item have a 2px line down the left (pink, yellow for the finisher).
- Rows: movement name, a chip with sets × reps, rest time, and "Last 135 lb".
- Bottom: **Start workout** (or **Resume workout**). Link: "Track results without the timer".

### Guided session

**Top of every session screen:** elapsed time and % complete, **Skip section** on the right, and a timeline with one segment per section, sized by its duration, filling in pink with a dot at the current position.

**Section preview** (start of each section): section title, a chip with its length, and its movements listed as "4x Barbell Back Squat / 6 reps · 4:00 rest". The highlight steps down the list while the coach reads each movement. Length: warm-up 15–30s, sections with a barbell lift 60s, dumbbell supersets 40s, finisher 30s.

**Work set:** "Set 1 of 4" in pink, then the set title with the reps in pink ("6x Barbell Back Squat"). Bottom row: reps on the left, the arc timer in the middle, weight on the right (a round + button when there's no weight yet). Tapping reps or weight opens a picker: reps ±1; weight ±2.5 and ±5.

**Rest / set up / switch:** the next set in a bordered card at the top ("Set 2 of 4 · 6x Barbell Back Squat") with the weight on its right. The arc timer is in exactly the same place as during work, in indigo, labelled "rest", "set up" or "switch".

**Warm-up move:** "Warm-up · 2 of 8", the move name, its time. Each-side moves are separate Left and Right steps.

**Finisher:** "Finisher · Round 1 of 5", the format, the list of moves, yellow timer.

**Arc timer:** a 240° dashed arc that fills as the step's time passes, countdown in the center, a small uppercase label under it.

**Bottom bar:** **Journal** (personal records and weight log) on the left, **Track results** (log sets) on the right. Visible on every session screen, including when paused.

**Gestures:** tap to pause; double-tap to replay the current step; swipe left for the next section, right for the previous one.

**Paused:** dark overlay, "Paused", a large Play button, **Previous** and **Next** buttons (with "Swipe" hints), **Replay** (double tap), **End workout**. X returns to the workout. Sound & coach button top right.

**Leaving:** "Leave this session?" sheet with **Keep going** and **Leave session**. Leaving goes home and saves your place.

### Journal sheet (Track results)
- Slides up; closes by sliding down or with the pink X.
- One card per exercise: name, sets × reps chip, last weight; a row per set with a numbered circle, weight, reps, and last time. Tap the circle to log the set with what's shown; it turns indigo with a check.
- Footer: "% Journal completion", sets and reps.
- Opened from the overview: also a **Complete workout** button.

### Sound & coach sheet
- Coach voice / Sounds only / Muted.
- 10-second sound: Rising chime, Boxing bell, Coach whistle, Soft marimba, Digital beep-beep, Ding-dong (tap to hear).
- Coach voice list, Premium and Enhanced voices first.

---

## Sound

- One chime at 10 seconds left on any step longer than 15 seconds.
- A short beep and a vibration when a step changes.
- The coach's lines are in `app/COACH-SCRIPT.md`.

---

## Still to design

- End-of-workout summary
- Macros and Progress pages (still light, from the original app)
- Exercise and day-card photos
