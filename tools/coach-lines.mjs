// Prints every line the coach can say (JSON array), by loading the app in a headless browser
// and calling coachAllLines(). Used by tools/record-coach-voice.py.
//
// Needs Playwright. Set PLAYWRIGHT_MODULE to its path if it isn't installed in this folder,
// and CHROMIUM_PATH to a Chromium binary if Playwright's own browser isn't installed.
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const pw = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
const chromium = pw.chromium || pw.default.chromium;
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage();
await page.route(/^https?:/, r => r.abort());
await page.goto(pathToFileURL(path.join(root, 'app', 'index.html')).href);
const lines = await page.evaluate(() => coachAllLines());
await browser.close();
process.stdout.write(JSON.stringify(lines));
