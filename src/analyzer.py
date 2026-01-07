import pandas as pd
import matplotlib.pyplot as plt

# Load NB Power dataset
file_path = "C:/Users/jaspi/Desktop/Energy usage analyzer/data/nb_power_dec_2025.csv"
df = pd.read_csv(file_path)

# Convert HOUR to datetime
df["HOUR"] = pd.to_datetime(df["HOUR"])

# Create time-based features
df["date"] = df["HOUR"].dt.date
df["hour_of_day"] = df["HOUR"].dt.hour
df["day_of_week"] = df["HOUR"].dt.day_name()

# -----------------------------
# STEP 3: Peak & Summary Stats
# -----------------------------

# Peak load hour
peak_load_row = df.loc[df["NB_LOAD"].idxmax()]

# Peak demand hour
peak_demand_row = df.loc[df["NB_DEMAND"].idxmax()]

# Summary statistics
summary = df[["NB_LOAD", "NB_DEMAND"]].describe()

print("\n=== PEAK LOAD HOUR ===")
print(peak_load_row[["HOUR", "NB_LOAD"]])

print("\n=== PEAK DEMAND HOUR ===")
print(peak_demand_row[["HOUR", "NB_DEMAND"]])

print("\n=== SUMMARY STATISTICS ===")
print(summary)


# -----------------------------
# STEP 4: VISUALIZATIONS
# -----------------------------

# NB Load vs NB Demand over time
plt.figure()
plt.plot(df["HOUR"], df["NB_LOAD"], label="NB Load")
plt.plot(df["HOUR"], df["NB_DEMAND"], label="NB Demand")
plt.xlabel("Time")
plt.ylabel("Power (MW)")
plt.title("NB Load vs NB Demand (December 2025)")
plt.legend()
plt.tight_layout()
plt.show()

# Average NB Load by Hour of Day
hourly_avg = df.groupby("hour_of_day")["NB_LOAD"].mean()

plt.figure()
plt.plot(hourly_avg.index, hourly_avg.values)
plt.xlabel("Hour of Day")
plt.ylabel("Average Load (MW)")
plt.title("Average NB Load by Hour of Day")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# Average NB Load by Day of Week
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daily_avg = df.groupby("day_of_week")["NB_LOAD"].mean().reindex(day_order)

plt.figure()
plt.plot(daily_avg.index, daily_avg.values)
plt.xlabel("Day of Week")
plt.ylabel("Average Load (MW)")
plt.title("Average NB Load by Day of Week")
plt.tight_layout()
plt.show()


# -----------------------------
# STEP 5: NET IMPORT / EXPORT
# -----------------------------

# Calculate net flow (positive = imports, negative = exports)
df["net_flow"] = (
    df["ISO_NE"]
    + df["NMISA"]
    + df["QUEBEC"]
    + df["NOVA_SCOTIA"]
    + df["PEI"]
)

# Count import vs export hours
import_hours = (df["net_flow"] > 0).sum()
export_hours = (df["net_flow"] < 0).sum()

print("\n=== NET FLOW SUMMARY ===")
print(f"Import hours: {import_hours}")
print(f"Export hours: {export_hours}")

# Plot net flow over time
plt.figure()
plt.plot(df["HOUR"], df["net_flow"])
plt.axhline(0)
plt.xlabel("Time")
plt.ylabel("Net Power Flow (MW)")
plt.title("NB Net Import / Export (December 2025)")
plt.tight_layout()
plt.show()
