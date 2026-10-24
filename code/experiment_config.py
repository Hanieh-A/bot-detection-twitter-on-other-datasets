"""Single source of truth for reproducible experiment settings."""
from pathlib import Path

SEED = 42
OUTER_SPLITS = 5
INNER_SPLITS = 4
RF_PARAMS = {
    "n_estimators": 300,
    "random_state": SEED,
    "n_jobs": -1,
    "class_weight": None,
}
ROOT = Path(__file__).resolve().parents[1]
DATASET1_PATH = ROOT / "datasets" / "dataset1.xlsx"
DATASET2_PATH = ROOT / "datasets" / "all_users_.xlsx"
# OFFICIAL_RESULTS = ROOT / "results_main"
# OFFICIAL_RESULTS = ROOT / "Human_Labels" / "results_main"
OFFICIAL_RESULTS = ROOT / "LLM_Labels" / "results_main"
THRESHOLD_GRID = tuple(round(x / 100, 2) for x in range(5, 96, 5))
