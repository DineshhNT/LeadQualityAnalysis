-----

## `README.md` Content

````markdown
# Lead Quality Analysis Case Study

This repository contains the Python analysis script and output visuals for the Lead Quality Analyst Case Study submitted by Dinesh N T.

The analysis focuses on evaluating lead quality trends over time, identifying key drivers of high-quality leads across various marketing segments (widgets, partners, campaigns), and calculating potential uplift to justify a higher Cost Per Lead (CPL).

## 📊 Key Findings Summary

The full analysis and business recommendations are detailed in the final report, but key findings demonstrated by the code outputs include:

* **Stable Trend:** Lead quality showed a slight downward trend over time, but it was **not statistically significant** (p-value: 0.278).
* **Segment Performance:** Widgets like **CreditSolutions**, **White**, and **BlueMeter** consistently delivered the highest average quality scores.
* **Optimization Potential:** A "what-if" analysis showed that focusing solely on the top 3 widgets could increase the average lead quality from **~5.2 to ~5.81**, providing data to justify a CPL increase for optimized traffic.

---

## 💻 Repository Contents

| File/Folder | Description |
| :--- | :--- |
| `analyst_case_study.py` | The main Python script containing data loading, quality scoring logic, segment analysis, and chart generation. |
| `Analyst case study dataset 1.xls` | **(Note: This file should be included or linked if allowed by the prompt constraints)** The original input dataset used for the analysis. |
| `analyzed_leads.csv` | The output dataset after quality scores and derived metrics were calculated by the script. |
| `/outputs` (folder) | Contains all generated PNG visuals, including: `quality_by_widgetname.png`, `quality_by_partner.png`, `lead_quality_over_time.png`, etc. |
| `README.md` | This file. |

---

## 🚀 How to Run the Code

To replicate the analysis and generate the charts locally, please follow these steps:

### 1. Requirements

The script requires a standard Python environment with the following libraries:

```bash
pandas
numpy
matplotlib
seaborn
scipy
````

You can install these dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### 2\. Execution

1.  Ensure the input file, `Analyst case study dataset 1.xls`, is in the same directory as the script.
2.  Execute the Python script from your terminal:

<!-- end list -->

```bash
python analyst_case_study.py
```

### 3\. Outputs

Upon successful execution, the following files will be created or updated:

  * `analyzed_leads.csv` (new data file with the `QualityScore` column)
  * `lead_quality_over_time.png`
  * `quality_by_widgetname.png`
  * `quality_by_partner.png`
  * ...and all other segment analysis charts.

-----
