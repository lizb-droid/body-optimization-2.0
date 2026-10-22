#!/usr/bin/env python3
"""Record every coach line with the free Kokoro "Heart" voice.

Writes one MP3 per line to app/audio/coach/<hash>.mp3 (hash = FNV-1a of the
exact line, matching csHash() in the app), skips lines already recorded, and
deletes recordings no longer used. Run after editing COACH-SCRIPT.md (and
syncing it with tools/sync-coach-script.py) or the program:

    python3 tools/record-coach-voice.py

Needs: Python packages kokoro-onnx and soundfile, ffmpeg, Node, and Playwright
(see tools/coach-lines.mjs). The voice model (Kokoro-82M, Apache-2.0) is
downloaded from npm on first run into tools/.voice-cache and checked against
its published SHA-256.
"""
import hashlib
import io
import json
import os
import pathlib
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "app" / "audio" / "coach"
CACHE = ROOT / "tools" / ".voice-cache"
VOICE = "af_heart"
SPEED = 1.0
MODEL_SHA256 = "fbae9257e1e05ffc727e951ef9b9c98418e6d79f1c9b6b13bd59f5c9028a1478"
MODEL_PKG = "https://registry.npmjs.org/kokoro-q8-shards/-/kokoro-q8-shards-1.0.0.tgz"
VOICES_PKG = "https://registry.npmjs.org/kokoro-js/-/kokoro-js-1.2.1.tgz"


def fnv1a(text):
    h = 0x811C9DC5
    for b in text.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return f"{h:08x}"


def fetch_tgz(url):
    with urllib.request.urlopen(url) as r:
        return tarfile.open(fileobj=io.BytesIO(r.read()), mode="r:gz")


def ensure_model():
    CACHE.mkdir(parents=True, exist_ok=True)
    model, voices = CACHE / "kokoro-q8.onnx", CACHE / f"{VOICE}.npz"
    if not model.exists():
        print("Downloading the voice model (about 90 MB, first run only)…")
        tgz = fetch_tgz(MODEL_PKG)
        parts = sorted((m for m in tgz.getmembers() if m.name.endswith(".bin")), key=lambda m: m.name)
        data = b"".join(tgz.extractfile(m).read() for m in parts)
        if hashlib.sha256(data).hexdigest() != MODEL_SHA256:
            sys.exit("Voice model checksum doesn't match; not using it.")
        model.write_bytes(data)
    if not voices.exists():
        import numpy as np
        tgz = fetch_tgz(VOICES_PKG)
        raw = tgz.extractfile(f"package/voices/{VOICE}.bin").read()
        np.savez(voices, **{VOICE: np.frombuffer(raw, dtype=np.float32).reshape(-1, 1, 256)})
    return model, voices


def coach_lines():
    out = subprocess.run(["node", str(ROOT / "tools" / "coach-lines.mjs")],
                         check=True, capture_output=True, text=True, env=os.environ)
    return json.loads(out.stdout)


def main():
    try:
        import soundfile as sf
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit("Install the recorder first:  pip install kokoro-onnx soundfile")
    model, voices = ensure_model()
    lines = coach_lines()
    OUT.mkdir(parents=True, exist_ok=True)
    wanted = {fnv1a(t): t for t in lines}
    todo = [(h, t) for h, t in wanted.items() if not (OUT / f"{h}.mp3").exists()]
    print(f"{len(lines)} coach lines, {len(todo)} to record")
    if todo:
        kokoro = Kokoro(str(model), str(voices))
        with tempfile.TemporaryDirectory() as tmp:
            for i, (h, text) in enumerate(todo, 1):
                audio, rate = kokoro.create(text, voice=VOICE, speed=SPEED, lang="en-us")
                wav = pathlib.Path(tmp) / f"{h}.wav"
                sf.write(wav, audio, rate)
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav),
                                "-ac", "1", "-b:a", "32k", str(OUT / f"{h}.mp3")], check=True)
                if i % 25 == 0 or i == len(todo):
                    print(f"  recorded {i}/{len(todo)}")
    removed = 0
    for f in OUT.glob("*.mp3"):
        if f.stem not in wanted:
            f.unlink()
            removed += 1
    (OUT / "lines.json").write_text(json.dumps(dict(sorted(wanted.items())), ensure_ascii=False, indent=1))
    print(f"Done. Removed {removed} unused recordings.")


if __name__ == "__main__":
    main()
