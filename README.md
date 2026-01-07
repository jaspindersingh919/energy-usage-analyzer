# NB Power Electricity Demand Analysis

## Project Overview
This project analyzes **hourly electricity system data from NB Power** to understand
electricity usage patterns, peak demand periods, and New Brunswick’s role as a power
importer or exporter during **December 2025**.

The goal of this project is to demonstrate practical skills in **time-series data
analysis, visualization, and energy system reasoning** using real utility data.
The analysis focuses on identifying peak demand behavior and understanding how
interprovincial and international power flows impact system demand.

---

## Dataset
- **Source:** NB Power System Information Archive  
- **Region:** New Brunswick, Canada  
- **Time Resolution:** Hourly  
- **Time Period:** December 2025 (744 hours)

### Key Variables
- **NB_LOAD** – Electricity consumed within New Brunswick (MW)
- **NB_DEMAND** – Total system demand including exports and system obligations (MW)
- **ISO_NE** – Power flow between New Brunswick and ISO New England (MW)
- **NMISA** – Power flow between New Brunswick and Northern Maine (MW)
- **QUEBEC** – Power flow between New Brunswick and Quebec (MW)
- **NOVA_SCOTIA** – Power flow between New Brunswick and Nova Scotia (MW)
- **PEI** – Power flow between New Brunswick and Prince Edward Island (MW)

Positive values represent power flowing **into** New Brunswick, while negative values
represent power flowing **out of** the province.

---

## Analysis Performed
- Parsed and processed hourly time-series data using Pandas
- Engineered time-based features (hour of day, date, day of week)
- Identified **peak load and peak demand hours**
- Computed summary statistics for system load and demand
- Compared internal electricity consumption with total system demand
- Calculated **net import/export power flow** using intertie data
- Created visualizations to highlight daily, weekly, and system-level trends

---

## Key Findings
- Peak electricity load and demand occurred on **December 9th at 8:00 AM**, consistent
  with winter morning heating and increased commercial activity
- Average electricity load during December was approximately **2.1 GW**, with notable
  hourly variability
- **NB Demand consistently exceeded NB Load**, reflecting exports and system obligations
- Distinct weekday versus weekend usage patterns were observed
- New Brunswick alternated between being a **net importer and a net exporter** depending
  on system conditions and demand levels

---

## Visualizations
The project generates the following charts:
- NB Load vs NB Demand over time
- Average NB Load by hour of day
- Average NB Load by day of week
- Net power import/export over time

All charts are saved to the `output/` directory when the script is executed.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

---

## Project Structure
energy-usage-analyzer/
│
├── data/
│   └── nb_power_dec_2025.csv
│
├── src/
│   └── analyzer.py
│
├── output/
│   └── (generated charts)
│
└── README.md
