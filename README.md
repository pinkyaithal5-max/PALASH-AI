# Santali dataset integration

## Primary dataset: AdiBhashaa
The prototype is wired for the **AdiBhashaa** Hindi→Tribal parallel benchmark, using its Santali split.

- Source: Hugging Face dataset `misniitdelhi/AdiBhasha`
- Santali split: `data/santali/santali-train.csv`
- Approximate size: 20,001 Hindi–Santali sentence pairs
- Santali script in this release: Ol Chiki
- Domains: education, governance, healthcare, news, social
- License: CC BY-NC-SA 4.0

The dataset is access-controlled on Hugging Face, so the full CSV is **not redistributed inside this ZIP**. Run `scripts/download_adibhasha.py` after accepting the dataset terms to download it into this folder.

The app can also import a CSV from the Translate screen. Expected columns are:
- `hindi`
- `santali`

Optional columns such as `row_id`, `domain`, `source`, or `license` are preserved by the importer but are not required for lookup.

## Important
Do not claim that an AI-generated translation is "verified" merely because it came from a model. For classroom deployment, the team should have a Santali speaker/teacher review the education-specific phrases used in the demo.
