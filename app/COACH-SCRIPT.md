# Coach script

Everything the coach says during a guided session. Rewrite any line in your own words and leave the ones you like. Once it is final, it gets wired into the app.

The coach should sound like a person standing next to you: setting up your space, reminding you to brace, telling you what to watch for. Not talking the whole time. The most talking happens at the start of the session and at the start of each movement. During sets, lines stay short.

Words in `{curly brackets}` get filled in automatically. Keep them where you want the number or name to be spoken. Lines you can hear mid-set are one idea each, mostly under 12 words.

| Placeholder | Becomes |
|---|---|
| `{session}` | Workout name, e.g. "Push. Shoulders and chest" |
| `{minutes}` | Total minutes, e.g. "48" |
| `{section}` | Section name, e.g. "Superset A" |
| `{exercise}` | Exercise name |
| `{reps}` | Reps or time, e.g. "8 to 12 reps", "20 second hold" |
| `{set}` / `{sets}` | Current set number / total sets |
| `{round}` / `{rounds}` | Current round / total rounds |
| `{rest}` | Rest length, e.g. "2 minutes" |
| `{seconds}` | Warm-up move length |
| `{side}` | "left" or "right" |
| `{cue}` | That exercise's coaching cue (from the cue list further down) |
| `{setup}` | **New.** That exercise's setup and bracing line (from the setup list further down) |

**New for the app (needs a code change):** the `{setup}` placeholder, the session briefings, the "Before we start" block, the rotating variants (rotate through them so it never sounds the same twice), and the deload lines (need a flag for deload weeks).

## Before we start (plays first, every session)

- **Space check:** Set up your space. Bar, plates, bench, dumbbells. Water within reach.
- **Fuel check:** Pre-workout fuel in? Training fasted costs you. Eat first if you haven't.
- **Body check:** Quick scan. Anything sharp? Any pelvic floor pressure? Tell me now, we adjust.
- **Mindset:** This is week {week} of the plan. Trust it. Let's go.

(`{week}` is optional. If the app can't fill it, drop the last line.)

## Session briefing (right after "Before we start", one per session)

Each one covers: what today is, what matters most, what to watch for. Read it all, then the session starts.

- **Lower A, glutes:** Lower A. Glutes first. Today is heavy. Back Squat, then Hip Thrust. Set the rack so the bar sits at mid-chest. Bench ready for thrusts, pad on the bar. Brace on every rep: big breath into your belly, ribs down, glutes tight. Any pelvic floor pressure or leaking? Stop that movement. Let's build.
- **Upper A, chest and back:** Upper A. Chest and back. Bench and row carry the day. Set the bench and bar before the clock starts. Shoulders down and back on every press. Pull the shoulder blades together before every row. Band pull-aparts first, wake up the back of the shoulders.
- **Lower B, quads and hamstrings:** Lower B. Quads and hamstrings. Thrusters first, so build into them with lighter sets. Heels on plates for the cyclist squat. GHD and sliders within reach. Brace hard and drive through the whole foot. Quality over speed.
- **Upper B, shoulders and chest:** Upper B. Shoulders and chest. Push press is the star. Clear your overhead space. Ribs down, glutes tight, no leaning back. Everything overhead stays stacked. Band pull-aparts before we press.
- **Full body, pull and glutes:** Saturday. Full body. Pull first, then glutes. Row, pullover, then a light hip thrust. Keep the thrust easy. Your legs ran yesterday. Flat back, brace, own the tempo.
- **Trail run (if guided):** Friday. Trail run. Zone 2. Walk the climbs, run the flats and downhills. Conversation pace, always. Quads sore from Wednesday? Walk the downs. Saturday needs your legs.
- **Deload week (adds to the briefing):** Deload week. Lighter on purpose. Same weights as last week. Fewer sets. Stop with reps in the tank. This is where the fatigue clears and the next block hits harder.

## Start and finish

- **Session starts:** {session}. {minutes} minutes. Earn it.
- **Session complete (rotate):**
  - Done. {minutes} minutes. That's the plan working.
  - Session complete. {minutes} minutes. Log it, then eat within thirty minutes.
  - That's it. {minutes} minutes. Protein and carbs now, hydrate, then go live your day.

## Section preview (start of each section, runs down each movement)

This is where the coach talks the most: what's coming and how to set up.

- **Section intro:** {section}.
- **Each strength lift:** {exercise}. {sets} sets of {reps}. {setup} {cue}
- **Each superset movement:** {exercise}. {rounds} rounds of {reps}. {setup}
- **Each warm-up movement:** {exercise}. {seconds} seconds.
- **Each finisher movement:** {exercise}, {reps}.

## Warm-up

- **Each move:** {exercise}. {seconds} seconds. Easy and smooth.
- **Each-side move:** {exercise}, {side} side. {seconds} seconds. Easy and smooth.

## Strength sets (rotate the variants)

- **First set:**
  - Set 1. {reps}. Brace. Make it clean.
  - Set 1. {reps}. Breathe in, ribs down, go.
  - Set 1. {reps}. Move it with intent.
- **Middle sets:**
  - Set {set}. Reset your brace. Go.
  - Set {set}. Same quality as set 1. Go.
  - Set {set}. Own it.
- **Last set:**
  - Last set. Leave nothing. {reps}.
  - Last set. Brace and finish strong. {reps}.
  - Last set. Make it the best one.
- **Rest:** Rest, {rest}. Set {set} next.
- **Rest (mid-lift coaching, use occasionally):**
  - Shake it out. Breathe slow. Nothing to rush.
  - Check your setup. Same position every set.
  - How did that feel? Log your weight.
- **Rest before the last set:** Rest, {rest}. Last set next. Make it count.
- **Extra line on the very first rest:** Log your weight. Breathe.
- **Set up for the next lift:** Next up, {exercise}. {sets} sets of {reps}. {setup} {cue} Get set up.

## Supersets

- **First round:** Round 1. {exercise}, {reps}. Go.
- **Middle rounds:** Round {round}. {exercise}, {reps}. Stay tight.
- **Last round:** Last round. {exercise}, {reps}. Finish it.
- **Second exercise in the round:** {exercise}, {reps}. Go.
- **Switch between exercises:** Switch. {exercise}.
- **Rest between rounds:** Rest, {rest}. Round {round} next.
- **Effort reminder (last round of accessories, occasionally):** Last round. Stop one or two reps shy of failure.

## Finisher

- **Interval, first round:** Round 1 of {rounds}. Go!
- **Interval, middle rounds:** Round {round}. Keep it moving!
- **Interval, last round:** Last round. Empty the tank!
- **AMRAP / for time:** Go! Finish strong.
- **Halfway (long finishers):** Halfway there. Keep moving.

## Timer

- **10 seconds left (rest):** 10 seconds. Get ready.
- **10 seconds left (set up):** 10 seconds.

## Setup lines (`{setup}`)

Read during the section preview and when you set up for a lift. Space, equipment, bracing, body position. Two or three short sentences. Moves with no equipment setup are left blank on purpose.

- **Arnold Press:** Sit tall, ribs down. Dumbbells at your chest, palms facing you.
- **Band Pull-Apart:** Hold the band at chest height. Arms straight.
- **Barbell Back Squat:** Bar at mid-chest in the rack. Hands tight, bar on your upper back. Big breath into your belly, ribs down, glutes tight.
- **Barbell Bench Press:** Eyes under the bar. Shoulder blades pinched and down. Feet planted.
- **Barbell Bent Over Row:** Hinge to about 45 degrees. Flat back. Brace like someone's about to poke your stomach.
- **Barbell Cyclist Squat:** Heels on plates. Bar in the front rack, elbows high. Big breath, ribs down.
- **Barbell Hip Thrust:** Upper back on the bench, pad on the bar. Feet flat, chin tucked. Ribs down.
- **Bird Dog:** Hands under shoulders, knees under hips. Neutral spine.
- **Bulgarian Split Squat:** Back foot on the bench, front foot a long step out. Dumbbells at your sides.
- **Chest-Supported DB Row:** Incline bench, chest on the pad. Let the arms hang.
- **DB Floor Press:** Lie on the floor, knees bent. Elbows will touch down at the bottom.
- **DB High Pull:** Dumbbells in front of your thighs. Soft knees, tall chest.
- **DB Lateral Raise:** Slight bend in the elbow. Ribs down. Stay tall, no leaning.
- **DB Pullover:** Lie along the bench, one dumbbell held over your chest. Ribs down.
- **DB Rear Delt Fly:** Hinge forward, flat back. Dumbbells hang under your shoulders.
- **DB Row tripod:** One hand and one knee braced. Flat back, hips square.
- **DB Shoulder Press:** Sit or stand tall. Dumbbells at shoulder height. Ribs down, glutes tight.
- **DB Snatch:** Dumbbell between your feet. Hips back, chest up.
- **DB Squeeze Press:** Lie back, dumbbells together over your chest. Press them into each other.
- **DB Thrusters:** Dumbbells at your shoulders. Feet shoulder width. Brace first.
- **DB Z Press:** Sit on the floor, legs straight. Tall spine. Dumbbells at your shoulders.
- **Deficit Reverse Lunge:** Front foot on a plate. Dumbbells at your sides. Stand tall.
- **Dips:** Set your station. Shoulders down. Slight lean forward for chest.
- **Farmer Carry:** Heavy dumbbells at your sides. Stand tall, ribs stacked.
- **GHD Hip Extension:** Hips just past the pad. Feet locked. Start with a neutral spine.
- **Incline DB Curl:** Bench at about 60 degrees. Arms hang straight down.
- **KB Swing:** Bell a foot in front of you. Hips back. Flat back.
- **Lateral Lunge:** Wide stance, toes forward. Dumbbell held at your chest.
- **Overhead Tricep Extension:** One dumbbell, both hands, overhead. Ribs down.
- **Pallof Hold:** Band anchored at chest height. Stand sideways, feet wide. Hold the band at your chest.
- **Push Press + Push Jerk:** Clear your overhead space. Bar in the rack position. Ribs down, glutes tight.
- **Push-up:** Hands under shoulders. Body in one line.
- **Row:** Feet strapped in. Sit tall. Handle in both hands.
- **Seated Rear Delt Fly:** Sit tall, chest on your thighs. Dumbbells under your knees.
- **Single-leg DB RDL:** Dumbbell in the hand opposite your standing leg. Soft knee. Tall chest.
- **Slider Hamstring Curl:** Lie on your back. Heels on sliders or towels. Hips up.
- **Spider Curl:** Chest on an incline bench. Arms hang straight down.
- **Suitcase Carry:** One dumbbell at your side. Stand tall, ribs stacked.
- **Thrusters:** Bar in the front rack, elbows high. Feet shoulder width. Brace first.
- **Turkish Get-Up:** Lie on your back. Arm straight up. Eyes on the hand.
- **Walking Lunge:** Dumbbells at your sides. Tall chest. Long steps.
- **Weighted Copenhagen Plank:** Top foot on the bench. Forearm down. Hips high.
- **Weighted Dead Bug:** Flat on your back. Ribs down, low back glued to the floor. Light dumbbell in the extended arm.

## Exercise cues (`{cue}`)

Read during the section preview and when you set up for a lift. What to feel, what to avoid, what to remember.

- **Arnold Press:** Rotate smoothly. Palms face you at the bottom, forward at the top.
- **Band Pull-Apart:** Squeeze the shoulder blades. No shrugging.
- **Barbell Back Squat:** Knees track over toes. Drive the floor away. Heaviest lower-body lift, so take the full rest.
- **Barbell Bench Press:** Bar to the lower chest. Elbows about 45 degrees. Drive through the feet.
- **Barbell Bent Over Row:** Row to the lower ribs. Squeeze the blades. Chest stays up.
- **Barbell Cyclist Squat:** Upright torso. Knees forward. Elbows up. Different angle from Monday's squat.
- **Barbell Hip Thrust:** Squeeze and hold two seconds at the top. Ribs down. Your number one movement.
- **Bird Dog:** Opposite arm and leg. Hips level. Slow and controlled.
- **Bulgarian Split Squat:** Drop straight down. Front heel stays planted. Drive through it.
- **Chest-Supported DB Row:** Elbows to the hips. Squeeze the lats. Zero lower back involvement.
- **DB Floor Press:** Elbows touch down, then press. Chest-dominant, no bench needed.
- **DB High Pull:** Pull to the chin, elbows high. Controlled tempo. No need to explode.
- **DB Lateral Raise:** Lead with the elbows. Stop at shoulder height. No swinging.
- **DB Pullover:** Slow arc, from above the chest to behind the head. Feel the lats and rib cage stretch. Start at 45 pounds.
- **DB Rear Delt Fly:** Soft elbows. Squeeze the back of the shoulder. No momentum.
- **DB Row tripod:** Pull the elbow to the hip. Hips stay square.
- **DB Shoulder Press:** Press straight up. Ribs stay down. Don't arch.
- **DB Snatch:** Hips drive it. Punch overhead and lock out.
- **DB Squeeze Press:** Squeeze the dumbbells together the whole time. Constant tension.
- **DB Thrusters:** Squat deep. Drive up and press in one motion.
- **DB Z Press:** Tall spine. No leaning back. Core carries the press.
- **Deficit Reverse Lunge:** Step back controlled. Front heel stays down. Torso tall.
- **Dips:** Bodyweight to start. Add weight once reps feel easy. Shoulders stay down.
- **Farmer Carry:** Tall posture. Ribs down. Short, quick steps.
- **GHD Hip Extension:** Squeeze the glutes at the top. Don't over-arch the lower back.
- **Incline DB Curl:** Elbows back. Slow lowering. Feel the stretch.
- **KB Swing:** Hips, not arms. Snap the hips and let the bell float.
- **Lateral Lunge:** Sit back into the hip. Toes forward. Chest up.
- **Overhead Tricep Extension:** Elbows forward. Full stretch, full lockout.
- **Pallof Hold:** Don't rotate. Band tension, not load. Core control.
- **Push Press + Push Jerk:** Dip straight down. Drive. Lock out stacked over your ears. Push jerk should feel easier than the press.
- **Push-up:** Chest to the floor. Body in one line.
- **Row:** Legs first, then back, then arms.
- **Seated Rear Delt Fly:** Lead with the elbows. Squeeze. No momentum.
- **Single-leg DB RDL:** Hinge, don't squat. Hips square. Flat back. Balance trains the stabilizers.
- **Slider Hamstring Curl:** Hips stay high. Slow on the way out. Pull the heels in with the hamstrings.
- **Spider Curl:** Chest stays on the bench. Squeeze at the top.
- **Suitcase Carry:** Don't lean. Resist the drop. Core stays tight.
- **Thrusters:** Build into it with lighter sets first. Squat deep, drive up, press through the top.
- **Turkish Get-Up:** Slow. One piece at a time. Eyes on the hand.
- **Walking Lunge:** Long step. Back knee kisses the floor.
- **Weighted Copenhagen Plank:** Hips high. Resist the drop. Slow and steady. Stop if you feel any pubic bone discomfort.
- **Weighted Dead Bug:** Slow. Exhale as you reach. Ribs don't flare. Core-safe, higher demand.

## Warm-up moves (optional, adds a line after the name)

- **World's Greatest Stretch:** Reach up and rotate. Open the hips.
- **Glute Bridge March:** Hips stay level. Squeeze each rep.
- **Hip Circles:** Big, slow circles.
- **Posterior Hip Capsule Stretch:** Sink back. Breathe into the hip.
- **Squat to Stand:** Fold down, chest up, stand tall.
- **Cat Cow:** Move with your breath.
- **Child's Pose Thread the Needle:** Reach through. Open the upper back.
- **Scapular Push-up:** Arms straight. Shoulder blades do the work.
- **Push-up to Down Dog:** Flow it. Press the floor away.
- **Band Pull-Apart:** Wake up the back of the shoulders.
