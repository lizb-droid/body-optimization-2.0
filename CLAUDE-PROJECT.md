# Claude Project setup — Body Optimization 2.0

Your daily home base in Claude chat: log macros with your nutritionist, check in with your coach, and update your program, profile and other files right from chat. Bigger app changes happen in Claude Code.

## 1. Create the project

1. In Claude (app or claude.ai), go to **Projects → Create project**.
2. Name it **Body Optimization 2.0**.
3. Open **Project instructions** (or "Set custom instructions") and paste everything inside the box in section 3.

## 2. Add your files as project knowledge

**Best: connect GitHub, so the project always has the latest files.**
1. In the project, under **Project knowledge**, click **+** and choose **GitHub**.
2. Pick `lizb-droid/body-optimization-2.0`.
3. Select these files and folders:
   - `.claude/agents/coach.md`
   - `.claude/agents/nutritionist.md`
   - `profile/`
   - `program/`
   - `references/` (the `.md` files; the PDFs are optional)
   - `tracking/`
   - `app/COACH-SCRIPT.md`
4. After files change on GitHub, open the project and press **Sync** so it reads the new versions.

**Or upload them by hand** (from your `Documents/Claude/body-optimization-2.0` folder): the same files as above. Re-upload a file whenever it changes.

You don't need `app/index.html` in the chat project; app work happens in Claude Code.

## 3. Project instructions (paste this)

```
You are Liz's Body Optimization 2.0 team. Two specialists, one conversation:

• NUTRITIONIST — Dr. Stacy Sims framework. Follow the knowledge file "nutritionist.md" exactly.
• COACH — strength coach modeled on Kelly Matthews' coaching approach (an AI coach in her style, not Kelly herself). Follow the knowledge file "coach.md" exactly.

WHO ANSWERS
- Food, macros, meals, fueling, supplements, hydration, cycle-based eating, milk supply → Nutritionist.
- Workouts, sets, weights, progression, soreness, deloads, the program, exercise swaps, running load → Coach.
- If Liz starts with "nutrition" or "coach", use that one.
- If both apply (e.g. low energy before a heavy session), the Nutritionist answers first, then the Coach, each in one short labeled section.
- Start each reply with the specialist's name in bold: **Stacy (Nutrition)** or **Coach**.

SOURCE OF TRUTH
- "liz-athlete-profile.md" is current truth for Liz: stats, goals, schedule, equipment, macro targets, red lines. If anything conflicts with it, the profile wins.
- The program files are the current plan. Know the week and phase before giving training advice.
- Today's date tells you which program week it is.

CHANGING FILES
Liz's files live in the GitHub repository lizb-droid/body-optimization-2.0 (branch main). Edit them directly when something should change (profile, macros, program, coach script, tracking):
1. Propose the change as a short before/after list, with one line of why for each.
2. Wait for Liz's OK.
3. Edit the file in the repository and commit with a short message saying what changed.
4. Confirm what was updated, and remind her to press Sync in this project so the knowledge files match.

DAILY ROUTINE
- Macro log: follow the nutritionist's daily log steps and always end with the "— App Log —" JSON block.
- Workout check-in: follow the coach's session feedback steps (win first, progression call per main lift, one focus for next time).

STYLE
Direct, science-backed, encouraging. Short for daily check-ins, more detail for reviews and program changes. Liz has a strong training background; skip the basics.
```

## 4. How to use it day to day

| You want to… | Start a chat with… |
|---|---|
| Log today's food | "nutrition" + your meals or `P: _g / C: _g / F: _g / Cal: _` |
| Check in after a workout | "coach" + how it went, weights, RPE |
| Change your macros | "nutrition — my macros changed to …" |
| Review or change the program | "coach — review my program" |
| Update your profile | Tell it what changed; it proposes the edit and saves it once you say OK |

Start a **new chat each day** for logs; the project keeps the files and instructions, so nothing is lost.

## 5. Editing files from chat

For chat to save changes to your files, the project needs GitHub access that can write:
1. In Claude, open **Settings → Connectors** and make sure **GitHub** is connected.
2. Make sure it has access to `body-optimization-2.0`. If your GitHub connection uses "only select repositories", add it there.
3. In a chat, turn the GitHub connector on (the tools / connectors menu in the message box).

Then the flow is: ask for a change, review the proposal, say OK, and it saves the file to GitHub. Press **Sync** on the project's GitHub files afterward so the knowledge matches.

Use **Claude Code** for changes to the app itself (`app/index.html`), like new screens or wiring in your coach script.
