"""Download the Santali split of AdiBhashaa into data/santhali/.

Prerequisite:
    pip install huggingface_hub

You must accept the dataset's access conditions on Hugging Face and authenticate
with `huggingface-cli login` (or `hf auth login`) before running this script.
"""
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
OUT = BASE_DIR / "data" / "santhali" / "santali-train.csv"

try:
    from huggingface_hub import hf_hub_download
except ImportError as exc:
    raise SystemExit("Install dependency first: pip install huggingface_hub") from exc

print("Downloading the Santali CSV from AdiBhasha...")
source = hf_hub_download(
    repo_id="misniitdelhi/AdiBhasha",
    filename="data/santali/santali-train.csv",
    repo_type="dataset",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(source, OUT)

print(f"Saved dataset to {OUT}")
