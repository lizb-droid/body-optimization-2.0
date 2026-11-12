#!/usr/bin/env node
/**
 * Record missing coach voice lines using kokoro-js (Node.js).
 * Uses the same FNV-1a hash as the app to name MP3 files.
 * Skips lines that already have an MP3. Deletes unused MP3s.
 *
 * Usage: node tools/record-coach-voice-node.mjs
 * Needs: kokoro-js (npm i kokoro-js), ffmpeg
 */
import { KokoroTTS } from 'kokoro-js';
import { execSync } from 'child_process';
import { existsSync, mkdirSync, readdirSync, unlinkSync, writeFileSync } from 'fs';
import { join, dirname, resolve } from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

// kokoro-js resolves voice files via import.meta.dirname inside the library.
// Monkey-patch the global __dirname-equivalent by setting env so the path resolves correctly.
const require = createRequire(import.meta.url);
const kokoroJsDir = dirname(require.resolve('kokoro-js'));
// The voices are at <kokoro-js-root>/voices/ — set this for internal path resolution
process.env.KOKORO_VOICES_PATH = join(kokoroJsDir, 'voices');

const __dir = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dir, '..');
const OUT = join(ROOT, 'app', 'audio', 'coach');
const VOICE = 'af_heart';

function fnv1a(text) {
  let h = 0x811c9dc5;
  for (const c of new TextEncoder().encode(text)) {
    h ^= c;
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h.toString(16).padStart(8, '0');
}

async function coachLines() {
  const { execSync } = await import('child_process');
  const out = execSync(`node ${join(__dir, 'coach-lines.mjs')}`, { encoding: 'utf8' });
  return JSON.parse(out);
}

mkdirSync(OUT, { recursive: true });

console.log('Loading Kokoro TTS model (first run downloads ~350MB)…');
const tts = await KokoroTTS.from_pretrained('onnx-community/Kokoro-82M-v1.0-ONNX', {
  dtype: 'q8',
  device: 'cpu',
});

const lines = await coachLines();
const wanted = new Map(lines.map(t => [fnv1a(t), t]));

const existing = new Set(readdirSync(OUT).filter(f => f.endsWith('.mp3')).map(f => f.replace('.mp3', '')));
const todo = [...wanted.entries()].filter(([h]) => !existing.has(h));

console.log(`${lines.length} coach lines, ${todo.length} to record`);

let i = 0;
for (const [h, text] of todo) {
  const wavPath = `/tmp/kokoro-${h}.wav`;
  const mp3Path = join(OUT, `${h}.mp3`);

  const audio = await tts.generate(text, { voice: VOICE });
  await audio.save(wavPath);

  execSync(`ffmpeg -loglevel error -y -i "${wavPath}" -ac 1 -b:a 32k "${mp3Path}"`);
  try { unlinkSync(wavPath); } catch {}

  i++;
  if (i % 10 === 0 || i === todo.length) {
    process.stdout.write(`\r  recorded ${i}/${todo.length}  `);
  }
}
if (todo.length) console.log('\nDone recording.');

// Clean up unused MP3s
const allMp3s = readdirSync(OUT).filter(f => f.endsWith('.mp3'));
let removed = 0;
for (const f of allMp3s) {
  if (!wanted.has(f.replace('.mp3', ''))) {
    unlinkSync(join(OUT, f));
    removed++;
  }
}

// Write index
writeFileSync(join(OUT, 'lines.json'), JSON.stringify(Object.fromEntries([...wanted].sort()), null, 1));
console.log(`Done. Removed ${removed} unused recordings.`);
