# Coach script

Everything the coach says during a guided session. The coach is quiet on purpose: a warm intro, a short setup line before the hard exercises, and a few words at the moments that matter. No set-by-set talking, no countdowns (the app already beeps at 10 seconds). Rewrite any line in your own words.

Words in `{curly brackets}` get filled in automatically. Keep them where you want the number or name to be spoken.

| Placeholder | Becomes |
|---|---|
| `{session}` | Workout name, e.g. "Lower A. Glutes" |
| `{minutes}` | Total minutes, e.g. "58" |
| `{exercise}` | Exercise name |
| `{sets}` | Total sets |
| `{reps}` | Reps or time, e.g. "8 to 12 reps", "20 second hold" |
| `{rounds}` / `{round}` | Finisher total rounds / current round |
| `{sprints}` | Friday sprint count for the week |
| `{side}` | "left" or "right" |
| `{seconds}` | Warm-up move length |
| `{cue}` | Setup and key point for hard exercises (list further down). Blank means the coach stays silent |
| `{effort}` | How hard it should feel, for main lifts only (lines below, picked by week type) |

**What needs a code change in the app (Claude Code):**
- Remove the "10 seconds left" voice lines. Keep the beep.
- `{cue}` now carries setup and the key point together (the old `{setup}` is merged in). Easy exercises have no cue and are spoken as name, sets and reps only.
- New `{effort}` placeholder, chosen by week type: standard, block-start (weeks 1 and 7), deload (6, 12), test (5, 11).
- Session intros, chosen by session and week type.
- No spoken set numbers, no rest announcements, no round-by-round talk except the lines listed here.
- `{sprints}` and the Friday lines.
- Rotating variants: where a line has several versions, pick one at random so it doesn't repeat.

## When the coach talks (and when it doesn't)

**Talks:** session intro, the setup gap before each exercise (one line), the first rest of a main lift (one check-in), the last set of a main lift, finisher start and last round, Friday sprint starts, and the finish.

**Silent:** set numbers, rest countdowns, middle sets, middle rounds, the 10-second warning, and easy exercises' cues.

## Session intro (plays once, before the warm-up)

- **Lower A, glutes:** Morning. Today's glutes. Squat first, then hip thrusts, then single-leg work. Heavy day, so brace on every rep. {minutes} minutes. Set up the rack and the bench before we start.
- **Upper A, chest and back:** Morning. Chest and back today. Bench first, then rows, then shoulders and arms. Shoulder blades back and down on every press. {minutes} minutes. Set up the bench and the bar first.
- **Lower B, quads and hamstrings:** Morning. Quads and hamstrings. Cyclist squat first, then RDL, split squats and hamstring curls, then a short finisher. {minutes} minutes. Heels on plates for the cyclist squat.
- **Upper B, shoulders and chest:** Morning. Shoulders and chest. Push press leads, so clear your overhead space. Ribs down, glutes tight. {minutes} minutes. Band pull-aparts first.
- **Conditioning (Friday):** Morning. Conditioning day. Short sprints, all out, then easy. You get on the machine once and stay on. Not feeling it? Skipping is allowed. About {minutes} minutes.
- **Full body (Saturday):** Morning. Full body Saturday, glute focus. Hip thrust first, then row, step-ups, curls, hip extension and clamshells. {minutes} minutes. Last session of the week.

**Deload weeks (6 and 12), plays instead of the intro above:**
Deload week. This is supposed to feel easy. Same weights as last week, fewer sets, stop with three or four reps in the tank. You're not losing anything. The fatigue clears and the next block hits harder. {minutes} minutes.

**Max-test weeks (5 and 11), plays instead of the intro above on test days:**
- **Monday, squat:** Max week. Squat day. Warm up slowly, then work up to three attempts. Stop at your last clean rep. Everything after that runs lighter, two sets each, no finisher. {minutes} minutes.
- **Tuesday, bench:** Max week. Bench day. Warm up slowly, work up to three attempts, pause on the chest. Stop at your last clean rep. Accessories run lighter today. {minutes} minutes.
- **Saturday, hip thrust:** Max week. Row first, then we test the hip thrust. Work up in small jumps, two second lockout on every rep. {minutes} minutes.
- **Friday:** Hold back today. This one is about your output, not wrecking yourself.

## Warm-up

- **Section start:** Warm-up. About two minutes.
- **Each move:** {exercise}.
- **Each-side move:** {exercise}, {side} side.
- **Warm-up done:** Warm-up done. Let's lift.

## Exercises (strength work)

The coach speaks once per exercise, during the 2 minute setup gap, so you can hear it while you set up.

- **First exercise of the session:** First up, {exercise}. {sets} sets of {reps}. {cue} {effort}
- **Setup gap before each next exercise:** Next up, {exercise}. {sets} sets of {reps}. {cue}
- **Same line for main lifts, with effort:** Next up, {exercise}. {sets} sets of {reps}. {cue} {effort}
- **Easy exercises (no cue):** Next up, {exercise}. {sets} sets of {reps}.
- **Unilateral work, at the start of each side:** {side} side.

**First rest of a main lift (one check-in, then quiet):**
- Log your weight. Did that feel like RPE 8 — about two reps left? If it was easier, we add next week. If it was a grind, we hold.
- Log it. RPE 8, two reps left, not zero. That's the target.

**Warm-up sets intro (plays once when a barbell lift with warm-up sets starts):**
- Three warm-up sets first, then your working sets.

**Last set of a main lift (rotate):**
- Last set. One or two in the tank. Don't grind it.
- Last one. Make it your best.
- Last set. Brace and finish clean.

**Last set of a main lift on deload weeks:** Last set. Keep it easy.

**Last set of an accessory (optional, off by default, use sparingly):** Last set. Stop one or two shy of failure.

## `{effort}` lines (main lifts only)

- **Standard weeks:** Working weight. RPE 8 — about two reps left on every set.
- **Block start (weeks 1 and 7):** First week at this weight. Aim for RPE 8 — about two reps left in the tank.
- **Deload weeks:** Easy today. RPE 6 — stop with three or four reps left.
- **Max-test lift:** Max day. Work up in small jumps. RPE 10 only on the attempts. Every rep clean.

## Finisher

- **Start:** Finisher. {exercise}. Go.
- **First round:** Round 1 of {rounds}. Go.
- **Middle rounds:** (silent)
- **Last round:** Last round. Empty the tank.
- **For time:** Go. Finish strong.

## Friday conditioning

- **Active prep start:** Active prep. Two rounds. Get your legs ready.
- **Pogo jumps:** {cue}
- **After active prep:** Hop on the machine. Easy for three minutes.
- **Builds:** Three builds. Ten seconds at RPE 7.
- **Before the main set:** Main set. {sprints} sprints, fifteen seconds all out. If a sprint drops more than ten percent below your best, we call it.
- **Each sprint:** Go.
- **Halfway:** Halfway.
- **Last sprint:** Last one. Everything.
- **Cool-down:** Cool down. Five minutes easy. Nice work.
- **Deload Friday:** Easy twenty minutes. Nothing to prove today.

## Finish

- **Normal (rotate):**
  - Done. {minutes} minutes. That's the plan working.
  - Nice work. {minutes} minutes. Log it and eat within thirty minutes.
  - That's it. {minutes} minutes. Protein and carbs now, then go live your day.
- **Deload:** Done. That was the easy week doing its job.
- **Max-test day:** Max day done. Log those numbers.

## Exercise cues (`{cue}`)

Setup and key point together, in one or two short sentences. Only for the hard or technical moves. Blank means the coach says nothing: Arnold Press, DB Squeeze Press, DB Floor Press, DB Shoulder Press, DB Rear Delt Fly, DB Lateral Raise, Incline DB Curl, DB Bicep Curl, Overhead Tricep Extension, Push-up, Walking Lunge.

- **Barbell Back Squat:** Bar at mid-chest in the rack. Big breath, ribs down, brace. Hips back first, then down. Drive the floor away.
- **Barbell Bench Press:** Eyes under the bar. Shoulder blades pinched and down, feet planted. Touch the lower chest and press.
- **Barbell Bent Over Row:** Hinge to about forty-five degrees. Flat back, brace. Pull to your lower ribs.
- **Barbell Hip Thrust:** Upper back on the bench, pad on the bar. Ribs down, chin tucked. Squeeze at the top for two seconds.
- **Barbell Cyclist Squat:** Heels on plates, bar in the front rack, elbows high. Sit straight down and drive up.
- **Barbell RDL:** Hips back, bar close to your legs, slow 3-second lowering. Stop when you feel the full hamstring stretch.
- **Push Press + Push Jerk:** Clear your overhead space. Dip straight down, drive, and lock out over your ears. The jerk reps should feel easier than the press.
- **Single-leg DB RDL:** Hips back, soft knee, flat back. Keep your hips square. Left side, thirty seconds, then right.
- **Curtsy Lunge:** Step back and across behind you. Front knee tracks over the toes. Chest tall.
- **Bulgarian Split Squat:** Back foot on the bench, long step out. Drop straight down, front heel stays planted.
- **Weighted Dead Bug:** Ribs down, low back on the floor. Breathe out as you reach.
- **Chest-Supported DB Row:** Chest on the pad. Go heavy. Elbows to your hips.
- **Dips:** Shoulders down, slight lean forward. Bodyweight first. Add weight when it's easy.
- **Weighted Copenhagen Plank:** Top foot on the bench, hips high. Stop if you feel any pubic bone discomfort.
- **GHD Hip Extension:** Hips just past the pad. Squeeze the glutes at the top. Don't over-arch your lower back.
- **DB Step-Up:** High bench, lean slightly forward, drive through the front heel. Control the way down.
- **Slider Hamstring Curl:** Hips high. Slow 3-second lowering — the eccentric is what makes it hard. Pull the heels in with your hamstrings.
- **Clamshell:** Slow and controlled — feel it in the side of the glute. Once 20 reps feel easy, add weight on the top hip.
- **Bird Dog:** Opposite arm and leg. Keep your hips level.
- **Pallof Hold:** Band at chest height. Don't let it pull you around.
- **KB Swing:** Hips, not arms. Snap the hips and let the bell float.
- **DB Snatch:** Hips drive it. Punch overhead and lock out.
- **Goblet Squat:** Elbows inside the knees. Chest tall.
- **Suitcase Carry:** Stand tall. Don't lean.
- **Pogo Jumps:** Stiff ankles, small and quiet. Land soft. Stop if you feel any leaking or pressure.
- **Skips:** Tall posture, drive the knee up.
- **Twisting Reverse Lunge:** Step back and rotate toward the front leg. Slow and controlled.

## Warm-up moves

Name only, spoken as above. No extra line.

- World's Greatest Stretch
- Glute Bridge March
- Hip Circles
- Posterior Hip Capsule Stretch
- Squat to Stand
- Cat Cow
- Child's Pose Thread the Needle
- Scapular Push-up
- Push-up to Down Dog
- Band Pull-Apart
