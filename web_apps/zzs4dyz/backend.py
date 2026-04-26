# <<<<<<< feature/summary-sum
# Branch 2: Analyzes sales data with SUM aggregation, sorts by Sales descending

import pandas as pd

REPORT_TITLE = "Monthly Sales Report - Total Analysis"
AGGREGATION = "sum"

df = pd.DataFrame({
    "Month":  ["Jan", "Feb", "Mar", "Apr", "May", "Jan", "Feb", "Mar"],
    "Region": ["North", "North", "South", "South", "North", "South", "North", "South"],
    "Sales":  [120, 150, 90, 200, 175, 130, 160, 95]
})

# Aggregate using SUM
summary = df.groupby("Month")["Sales"].sum().reset_index()
summary.columns = ["Month", "Agg_Sales"]
summary = summary.sort_values("Agg_Sales", ascending=False)  # sorted by Sales, not Month

# Performance label based on SUM threshold
summary["Performance"] = summary["Agg_Sales"].apply(
    lambda x: "Good" if x >= 250 else "Needs Improvement"
)

print(f"\n{'='*45}")
print(f"  {REPORT_TITLE}")
print(f"{'='*45}")
print(summary.to_string(index=False))
print(f"\nOverall Total Sales: {summary['Agg_Sales'].sum():.2f}")
# >>>>>>> feature/summary-sum


print('different commit 1')