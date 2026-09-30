# PALASH AI — SIH Prototype

A self-contained PWA prototype for the Smart India Hackathon problem statement on AI-assisted vernacular pedagogy and real-time translation for mother-tongue primary education.

## Included modules
- Teacher Dashboard
- Curriculum Translator
- Live Classroom voice interaction demo
- Bilingual worksheet generator
- Visual flashcards
- Offline-first service worker cache

## Run
Open `index.html` in a browser. For full PWA/offline behavior, serve the folder over localhost, e.g. `python -m http.server 8000`, then open `http://localhost:8000`.

## Important prototype note
The target-language strings are deliberately marked as requiring linguist-validated Santhali content. Do not present placeholder strings as authoritative translations. Replace them with verified language-pack entries before the SIH demo.

## Next engineering step
Replace the local demo translation dictionary and browser speech layer with the selected ASR/NMT/TTS implementation, then package the same UI into Android using Capacitor or a native Android/Flutter shell.

## Add the full Santali dataset

The prototype is configured for the AdiBhashaa Santali split (about 20,001 Hindi–Santali pairs). The source repository is licensed CC BY-NC-SA 4.0 and requires accepting its access conditions before the files can be downloaded. See `data/santhali/README.md`.

On a machine with Python and internet access:

```bash
pip install huggingface_hub
hf auth login
python scripts/download_adibhasha.py
```

Then serve the project locally:

```bash
python -m http.server 8000
```

Open `http://localhost:8000`. The app will automatically load `data/santhali/santali-train.csv`. You can also use **Import CSV** in the Translator screen.

### What this changes
- Exact Hindi→Santali dataset lookup instead of the old placeholder translation box.
- Dataset row count shown in the app.
- CSV import for judges/development machines.
- No fabricated Santali translations are inserted by the prototype.
