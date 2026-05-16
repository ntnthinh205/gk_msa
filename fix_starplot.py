import json

with open("multivariate_statistics.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell["cell_type"] == "code":
        src = "".join(cell["source"])
        if "Star Plot Overlay" in src and "mins_val = X_sample.min(axis=0)" in src:
            src = src.replace("mins_val = X_sample.min(axis=0)", "mins_val = population_df[score_cols].values.min(axis=0)")
            src = src.replace("maxs_val = X_sample.max(axis=0)", "maxs_val = population_df[score_cols].values.max(axis=0)")
            cell["source"] = [l + "\n" for l in src.splitlines()]
            cell["source"][-1] = cell["source"][-1].rstrip()

with open("multivariate_statistics.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
