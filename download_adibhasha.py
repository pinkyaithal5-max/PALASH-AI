"""Download the Santali split of AdiBhashaa into data/santhali/.

Prerequisite:
    pip install datasets huggingface_hub

You must accept the dataset's access conditions on Hugging Face and authenticate
with `huggingface-cli login` (or `hf auth login`) before running this script.
"""
from pathlib import Path
import csv

OUT = Path(__file__).resolve().parents[1] / "data" / "santhali" / "santali-train.csv"

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    raise SystemExit("Install dependency first: pip install huggingface_hub")

print("Downloading the Santali CSV from AdiBhashaa...")
source = hf_hub_download(
    repo_id="misniitdelhi/AdiBhasha",
    filename="data/santali/santali-train.csv",
    repo_type="dataset",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
import shutil
shutil.copy2(source, OUT)

print(f"Saved dataset to {OUT}")
