# <<<<<<< feature/summary-mean
# Branch 1: Analyzes sales data with MEAN aggregation, sorts by Month

import pandas as pd

REPORT_TITLE = "Monthly Sales Report - Average Analysis"
AGGREGATION = "mean"

df = pd.DataFrame({
    "Month":  ["Jan", "Feb", "Mar", "Apr", "May", "Jan", "Feb", "Mar"],
    "Region": ["North", "North", "South", "South", "North", "South", "North", "South"],
    "Sales":  [120, 150, 90, 200, 175, 130, 160, 95]
})

# Aggregate using MEAN
summary = df.groupby("Month")["Sales"].mean().reset_index()
summary.columns = ["Month", "Agg_Sales"]
summary = summary.sort_values("Month")

# Performance label based on MEAN threshold
summary["Performance"] = summary["Agg_Sales"].apply(
    lambda x: "Good" if x >= 130 else "Needs Improvement"
)

print(f"\n{'='*45}")
print(f"  {REPORT_TITLE}")
print(f"{'='*45}")
print(summary.to_string(index=False))
print(f"\nOverall Mean Sales: {summary['Agg_Sales'].mean():.2f}")
# >>>>>>> feature/summary-mean