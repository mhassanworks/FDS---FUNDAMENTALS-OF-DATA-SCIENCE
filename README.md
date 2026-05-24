<div align="center">

```
███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝
█████╗  ██║  ██║███████╗
██╔══╝  ██║  ██║╚════██║
██║     ██████╔╝███████║
╚═╝     ╚═════╝ ╚══════╝

███████╗██╗   ██╗███╗   ██╗██████╗  █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗ █████╗ ██╗     ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║     ██╔════╝
█████╗  ██║   ██║██╔██╗ ██║██║  ██║███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ███████║██║     ███████╗
██╔══╝  ██║   ██║██║╚██╗██║██║  ██║██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║     ╚════██║
██║     ╚██████╔╝██║ ╚████║██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ██║  ██║███████╗███████║
╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝

        ██████╗ ███████╗    ██████╗  █████╗ ████████╗ █████╗     ███████╗ ██████╗██╗███████╗███╗   ██╗ ██████╗███████╗
        ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝████╗  ██║██╔════╝██╔════╝
        ██║  ██║███████╗    ██║  ██║███████║   ██║   ███████║    ███████╗██║     ██║█████╗  ██╔██╗ ██║██║     █████╗
        ██║  ██║╚════██║    ██║  ██║██╔══██║   ██║   ██╔══██║    ╚════██║██║     ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝
        ██████╔╝███████║    ██████╔╝██║  ██║   ██║   ██║  ██║    ███████║╚██████╗██║███████╗██║ ╚████║╚██████╗███████╗
        ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
```

# 📊 Fundamentals of Data Science

### *Statistics · NumPy · Pandas · Visualization · Regression · Correlation — All in One Place*

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)](https://matplotlib.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

> *"Data is the new oil — but only if you know how to refine it."*

<br/>

</div>

---

## 📌 Table of Contents

| # | Section |
|---|---------|
| 01 | [Repository Overview](#-repository-overview) |
| 02 | [Data Science Pipeline Map](#️-data-science-pipeline-map) |
| 03 | [Module Index by Topic](#-module-index-by-topic) |
| 04 | [Complete File Map](#-complete-file-map) |
| 05 | [Concept Deep Dives](#-concept-deep-dives) |
| 06 | [Quick Formula Reference](#-quick-formula-reference) |
| 07 | [Getting Started](#-getting-started) |
| 08 | [Roadmap](#-roadmap) |
| 09 | [Contributing](#-contributing) |
| 10 | [Author](#-author) |

---

## 🚀 Repository Overview

**Fundamentals of Data Science** is a hands-on Python implementation repository covering the core statistical and computational concepts every data scientist must master — from raw data loading with Pandas to visualizing distributions and fitting regression models.

Each file explores one concept in isolation, making it easy to study, run, and extend independently.

### What This Repository Covers

| Domain | Scope |
|--------|-------|
| **Descriptive Statistics** | Central tendency (mean, median, mode), variability (variance, std dev, range) |
| **Distributions** | Frequency tables, histograms, normal curve, probability density |
| **Correlation** | Pearson correlation, scatter plots, relationship strength |
| **Regression** | Linear regression, line of best fit, prediction |
| **Data Manipulation** | NumPy arrays, Pandas DataFrames, data cleaning |
| **Visualization** | Matplotlib plots, scatter plots, curve plotting |

---

## 🏗️ Data Science Pipeline Map

```
DATA SCIENCE WORKFLOW                    IMPLEMENTATIONS IN THIS REPO
──────────────────────────────────────────────────────────────────────────────

┌──────────────────────────┐
│   1. DATA COLLECTION     │            Numpy.py          ← raw array creation
│      & LOADING           │            Pandas data       ← structured DataFrame
└──────────┬───────────────┘              frame.py          loading & inspection
           │
           ▼
┌──────────────────────────┐
│   2. DESCRIPTIVE         │            Average.py        ← mean, median, mode
│      STATISTICS          │            Variability.py    ← variance, std dev,
│                          │                                range, IQR
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   3. DISTRIBUTIONS &     │            Frequency.py      ← frequency tables,
│      FREQUENCIES         │                                relative frequency
│                          │            Normal Curve.py   ← Gaussian distribution,
│                          │                                PDF plotting
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   4. RELATIONSHIPS       │            Correlation.py    ← Pearson r, strength
│      & CORRELATION       │            Scatter.py        ← scatter plot, visual
│                          │                                correlation
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   5. MODELLING &         │            Regression.py     ← linear regression,
│      PREDICTION          │                                slope, intercept,
│                          │                                prediction
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   6. VISUALIZATION       │            Matplotlib.py     ← line plots, bar charts,
│                          │                                histograms, subplots
└──────────────────────────┘

Library Stack:
  NumPy   → numerical arrays, mathematical operations, broadcasting
  Pandas  → DataFrames, Series, CSV I/O, groupby, filtering
  Matplotlib → 2D plotting, figure/axes API, styling
  SciPy / math → statistical functions (used internally)
```

---

## 📦 Module Index by Topic

### 🔷 Data Manipulation & Core Libraries

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Numpy.py` | NumPy arrays and operations | `np.array()`, `np.zeros()`, `np.linspace()`, broadcasting, vectorized math, slicing |
| `Pandas data frame.py` | Pandas DataFrames for structured data | `pd.DataFrame()`, `pd.read_csv()`, `.head()`, `.describe()`, `.dropna()`, indexing |

> **Why NumPy?** Python lists are slow for math. NumPy stores data in contiguous memory blocks and applies operations to entire arrays at once — often 10–100× faster than a Python loop.

---

### 🔷 Descriptive Statistics

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Average.py` | Measures of central tendency | Mean, median, mode — when each is the right measure to use |
| `Variability.py` | Measures of spread | Variance, standard deviation, range, interquartile range (IQR), coefficient of variation |

> **Central tendency tells you where data clusters. Variability tells you how spread out it is. You need both to understand a dataset.**

---

### 🔷 Distributions & Frequencies

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Frequency.py` | Building frequency distributions | Absolute frequency, relative frequency, cumulative frequency, class intervals |
| `Normal Curve.py` | Plotting the Gaussian distribution | Normal PDF, mean ± std dev bands, 68-95-99.7 rule, `scipy.stats.norm` |

---

### 🔷 Correlation & Relationships

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Correlation.py` | Measuring linear relationship strength | Pearson correlation coefficient r, interpretation, `np.corrcoef()` |
| `Scatter.py` | Visualizing bivariate relationships | Scatter plot, trend direction, outlier detection, `plt.scatter()` |

---

### 🔷 Regression & Prediction

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Regression.py` | Linear regression from scratch and with libraries | Slope, intercept, line of best fit, R² score, prediction, `np.polyfit()` |

---

### 🔷 Visualization

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Matplotlib.py` | Comprehensive Matplotlib usage | `plt.plot()`, `plt.bar()`, `plt.hist()`, `plt.subplot()`, labels, legends, styling |

---

## 📂 Complete File Map

```
FDS---FUNDAMENTALS-OF-DATA-SCIENCE/
│
├── 🧮  DATA MANIPULATION
│   ├── Numpy.py                    ← array creation, math ops, broadcasting, slicing
│   └── Pandas data frame.py        ← DataFrames, CSV loading, filtering, aggregation
│
├── 📏  DESCRIPTIVE STATISTICS
│   ├── Average.py                  ← mean, median, mode — central tendency
│   └── Variability.py              ← variance, std dev, range, IQR
│
├── 📈  DISTRIBUTIONS
│   ├── Frequency.py                ← frequency tables, relative & cumulative freq
│   └── Normal Curve.py             ← Gaussian PDF, 68-95-99.7 rule, bell curve plot
│
├── 🔗  CORRELATION
│   ├── Correlation.py              ← Pearson r, strength interpretation
│   └── Scatter.py                  ← scatter plot, bivariate visualization
│
├── 📉  REGRESSION
│   └── Regression.py               ← linear regression, slope/intercept, R², prediction
│
├── 🎨  VISUALIZATION
│   └── Matplotlib.py               ← line, bar, histogram, subplots, full styling
│
└── 📄  README.md
```

---

## 🔬 Concept Deep Dives

<details>
<summary><strong>🔹 Mean vs Median vs Mode — Choosing the Right Average</strong></summary>

<br/>

All three measure the "center" of a dataset — but they react very differently to outliers.

```
Dataset: [10, 12, 13, 14, 15, 15, 200]

Mean   = (10+12+13+14+15+15+200) / 7 = 279 / 7 ≈ 39.9   ← pulled by 200
Median = middle value when sorted = 14                    ← robust to 200
Mode   = 15 (appears twice)                               ← most frequent

When the outlier (200) is removed:
  Dataset: [10, 12, 13, 14, 15, 15]
  Mean   = 13.2   ← now close to median
  Median = 13.5

Conclusion:
  Use MEAN   when data is symmetric, no extreme outliers (exam scores, heights)
  Use MEDIAN when data is skewed or has outliers (income, house prices)
  Use MODE   when data is categorical (most popular shoe size, most common grade)
```

**Skewness and the mean-median relationship:**
```
Left-skewed (negative):   Mean < Median < Mode
Symmetric (normal):       Mean ≈ Median ≈ Mode
Right-skewed (positive):  Mode < Median < Mean
                                        ↑
                             Income distributions
                             are typically right-skewed
```

</details>

<details>
<summary><strong>🔹 Variance & Standard Deviation — Measuring Spread</strong></summary>

<br/>

Variance measures how far values are from the mean on average (squared). Standard deviation is its square root — back in the original unit.

```
Dataset: [2, 4, 4, 4, 5, 5, 7, 9]

Step 1 — Mean:
  x̄ = (2+4+4+4+5+5+7+9) / 8 = 40 / 8 = 5

Step 2 — Squared deviations from mean:
  (2-5)² = 9
  (4-5)² = 1  × 3 occurrences = 3
  (5-5)² = 0  × 2 occurrences = 0
  (7-5)² = 4
  (9-5)² = 16

Step 3 — Variance (population):
  σ² = (9 + 1 + 1 + 1 + 0 + 0 + 4 + 16) / 8 = 32 / 8 = 4.0

Step 4 — Standard Deviation:
  σ = √4.0 = 2.0

Interpretation: on average, values are 2.0 units away from the mean of 5.

Population vs Sample:
  Population variance: divide by N       → σ²  (used when you have all data)
  Sample variance:     divide by (N-1)   → s²  (used when you have a sample)
  The (N-1) correction (Bessel's) avoids underestimating true variance.
```

**Coefficient of Variation (CV):**
```
CV = (σ / x̄) × 100%

Lets you compare spread between datasets with different units or scales.
  Dataset A: mean=50, σ=5  → CV = 10%   (relatively low spread)
  Dataset B: mean=5,  σ=5  → CV = 100%  (extremely high spread)
```

</details>

<details>
<summary><strong>🔹 Normal Distribution — The Bell Curve</strong></summary>

<br/>

The normal (Gaussian) distribution is the most important distribution in statistics. It appears naturally in heights, test scores, measurement errors, and many natural phenomena.

```
Probability Density Function:
                     1
  f(x) = ─────────────────── · e^(-(x-μ)²/2σ²)
           σ · √(2π)

Where: μ = mean (center of the bell)
       σ = standard deviation (width of the bell)

The 68-95-99.7 Rule (Empirical Rule):
──────────────────────────────────────────────────────────
         │        ←─────────── 99.7% ───────────→        │
         │          ←──────── 95% ────────→              │
         │               ←── 68% ──→                     │
         │                                               │
         │          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                    │
         │        ▄▄               ▄▄                    │
         │      ▄▄                   ▄▄                  │
         │    ▄▄                       ▄▄                │
──────────────────────────────────────────────────────────
       μ-3σ  μ-2σ   μ-σ     μ    μ+σ   μ+2σ  μ+3σ

  μ ± 1σ  → 68.27% of data
  μ ± 2σ  → 95.45% of data
  μ ± 3σ  → 99.73% of data

Example — IQ scores (μ=100, σ=15):
  68% of people score between 85–115
  95% of people score between 70–130
  99.7% of people score between 55–145
  A score of 145 is extremely rare (top 0.15%)
```

**Standard Normal (Z-score):**
```
Z = (X - μ) / σ

Converts any normal distribution to mean=0, std=1.
Lets you look up probabilities in a Z-table.

Example: X = 130, μ = 100, σ = 15
  Z = (130 - 100) / 15 = 2.0
  P(X ≤ 130) = P(Z ≤ 2.0) ≈ 97.7%
```

</details>

<details>
<summary><strong>🔹 Pearson Correlation — Measuring Linear Relationships</strong></summary>

<br/>

The Pearson correlation coefficient r quantifies the strength and direction of the linear relationship between two variables.

```
Formula:
         Σ[(xᵢ - x̄)(yᵢ - ȳ)]
  r = ───────────────────────────────
       √[Σ(xᵢ-x̄)²] · √[Σ(yᵢ-ȳ)²]

Range: -1 ≤ r ≤ +1

Interpretation:
  r = +1.0   Perfect positive linear relationship
  r = +0.8   Strong positive
  r = +0.5   Moderate positive
  r = 0.0    No linear relationship
  r = -0.5   Moderate negative
  r = -0.8   Strong negative
  r = -1.0   Perfect negative linear relationship

Visual guide:

  r ≈ +0.9          r ≈ 0.0           r ≈ -0.9
  y ↑               y ↑               y ↑
    │  ·  ·           │ · ·  ·           │·
    │ ·  ·            │·  · ·  ·         │ ·  ·
    │·  ·             │   · · ·           │   · ·
    │·                │ ·   ·  ·          │     · ·
    └───────→ x       └───────→ x        └───────→ x
    As x rises,       No pattern          As x rises,
    y rises too                           y falls

⚠️ Correlation ≠ Causation
  Ice cream sales and drowning rates are positively correlated.
  Cause: both are driven by a third variable — hot summer weather.
```

</details>

<details>
<summary><strong>🔹 Linear Regression — Fitting the Line of Best Fit</strong></summary>

<br/>

Linear regression finds the straight line through a scatter plot that minimizes the total squared vertical distance from each point to the line (Ordinary Least Squares).

```
Model:   ŷ = mx + b

Where:   ŷ  = predicted y value
         m  = slope     (how much y changes per unit of x)
         b  = intercept (value of ŷ when x = 0)

Formulas (derived from minimizing Σ(yᵢ - ŷᵢ)²):
         Σ[(xᵢ - x̄)(yᵢ - ȳ)]          Σ(xᵢ-x̄)(yᵢ-ȳ)
  m = ──────────────────────── = ──────────────────────
              Σ(xᵢ - x̄)²                Σ(xᵢ-x̄)²

  b = ȳ - m·x̄

Example:
  Hours studied: [1, 2, 3, 4, 5]
  Exam scores:   [50, 55, 65, 70, 80]

  x̄ = 3,  ȳ = 64
  Σ(xᵢ-x̄)(yᵢ-ȳ) = (-2)(-14) + (-1)(-9) + (0)(1) + (1)(6) + (2)(16) = 75
  Σ(xᵢ-x̄)²       = 4 + 1 + 0 + 1 + 4 = 10

  m = 75 / 10 = 7.5
  b = 64 - 7.5 × 3 = 64 - 22.5 = 41.5

  Line of best fit: ŷ = 7.5x + 41.5

  Prediction: student studies 6 hours →
    ŷ = 7.5(6) + 41.5 = 45 + 41.5 = 86.5

R² (Coefficient of Determination):
  R² = 1 - (Σ residuals²) / (Σ(yᵢ - ȳ)²)

  R² = 1.0 → perfect fit (all points on the line)
  R² = 0.85 → model explains 85% of variance in y
  R² = 0.0 → model explains nothing
```

</details>

<details>
<summary><strong>🔹 Frequency Distributions — Organizing Raw Data</strong></summary>

<br/>

A frequency distribution organizes raw data into a structured table showing how often values (or ranges of values) occur.

```
Raw data — exam scores (n=20):
  [72, 85, 91, 67, 78, 88, 92, 75, 83, 69,
   95, 74, 82, 88, 71, 79, 90, 66, 84, 77]

Step 1 — Choose class width:
  Range = 95 - 66 = 29
  Classes = 5  →  width = 29/5 ≈ 6  →  use 10 for clean intervals

Step 2 — Build frequency table:

  Class        Tally    Freq (f)   Rel. Freq    Cum. Freq
  ─────────────────────────────────────────────────────────
  60 – 69      |||       3         3/20 = 15%     3  (15%)
  70 – 79      |||||||   7         7/20 = 35%    10  (50%)
  80 – 89      |||||||   7         7/20 = 35%    17  (85%)
  90 – 99      |||       3         3/20 = 15%    20 (100%)
  ─────────────────────────────────────────────────────────
  Total                 20        100%

Reading the table:
  50% of students scored 79 or below (cumulative frequency)
  The middle two intervals (70–89) contain 70% of all scores
  Distribution appears roughly symmetric around 79–80
```

</details>

---

## 📐 Quick Formula Reference

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CENTRAL TENDENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mean (μ)          μ = Σxᵢ / n
Median            Middle value (sorted); avg of two middle if even n
Mode              Most frequently occurring value

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VARIABILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Range             max(x) - min(x)
Population Var    σ²  = Σ(xᵢ - μ)² / N
Sample Var        s²  = Σ(xᵢ - x̄)² / (n-1)
Std Deviation     σ   = √σ²
IQR               Q3 - Q1
Z-score           Z   = (x - μ) / σ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CORRELATION & REGRESSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pearson r         r   = Σ[(xᵢ-x̄)(yᵢ-ȳ)] / (√Σ(xᵢ-x̄)² · √Σ(yᵢ-ȳ)²)
Slope             m   = Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)²
Intercept         b   = ȳ - m·x̄
Prediction        ŷ   = mx + b
R-squared         R²  = 1 - SSresiduals / SStotal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NORMAL DISTRIBUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PDF               f(x) = (1/σ√2π) · e^(-(x-μ)²/2σ²)
68-95-99.7 Rule   μ±1σ → 68%,  μ±2σ → 95%,  μ±3σ → 99.7%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PYTHON QUICK REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
np.mean(x)        Arithmetic mean
np.median(x)      Median
np.std(x)         Standard deviation (population, ddof=0)
np.std(x,ddof=1)  Standard deviation (sample)
np.var(x)         Variance
np.corrcoef(x,y)  Pearson correlation matrix
np.polyfit(x,y,1) Slope and intercept of linear regression
np.polyval(p,x)   Evaluate polynomial (use with polyfit output)
pd.DataFrame.describe()  Count, mean, std, min, quartiles, max
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.x required
python3 --version

# Install required libraries
pip install numpy pandas matplotlib scipy

# Optional: Jupyter for interactive exploration
pip install jupyter
jupyter notebook
```

### Clone the Repository

```bash
git clone https://github.com/mhassanworks/FDS---FUNDAMENTALS-OF-DATA-SCIENCE.git
cd FDS---FUNDAMENTALS-OF-DATA-SCIENCE
```

### Run Any Module

```bash
# Core libraries
python3 Numpy.py
python3 "Pandas data frame.py"

# Statistics
python3 Average.py
python3 Variability.py

# Distributions
python3 Frequency.py
python3 "Normal Curve.py"

# Relationships
python3 Correlation.py
python3 Scatter.py

# Modelling
python3 Regression.py

# Visualization
python3 Matplotlib.py
```

### Recommended Learning Order

| Step | File | What You'll Learn |
|------|------|-------------------|
| 1 | `Numpy.py` | Arrays, vectorized operations — the foundation |
| 2 | `Pandas data frame.py` | Working with real structured data |
| 3 | `Average.py` | Central tendency — describing your data's center |
| 4 | `Variability.py` | Spread — how much data varies around the center |
| 5 | `Frequency.py` | Organizing and grouping data into distributions |
| 6 | `Normal Curve.py` | The most important distribution in statistics |
| 7 | `Matplotlib.py` | Visualizing everything you've computed |
| 8 | `Scatter.py` | Spotting relationships between two variables |
| 9 | `Correlation.py` | Quantifying relationship strength |
| 10 | `Regression.py` | Building a predictive model |

---

## 🔮 Roadmap

### 🔜 Upcoming Implementations

- [ ] **Probability Basics** — Sample spaces, events, conditional probability, Bayes' theorem
- [ ] **Hypothesis Testing** — Null/alternative hypothesis, p-value, t-test, chi-square test
- [ ] **Confidence Intervals** — Estimating population parameters from sample data
- [ ] **Multiple Regression** — Regression with more than one predictor variable
- [ ] **Logistic Regression** — Classification, sigmoid function, decision boundary
- [ ] **Data Cleaning** — Handling missing values, outliers, duplicates with Pandas

### 📅 Advanced Topics Planned

- [ ] **Seaborn Visualization** — Statistical plots, heatmaps, pairplots
- [ ] **Principal Component Analysis (PCA)** — Dimensionality reduction
- [ ] **Clustering (K-Means)** — Unsupervised learning basics
- [ ] **Time Series Analysis** — Trends, seasonality, rolling averages
- [ ] **Feature Engineering** — Encoding, scaling, transformation techniques
- [ ] **Scikit-learn Introduction** — Train/test split, cross-validation, model evaluation

---

## 🤝 Contributing

Contributions of new data science implementations, statistical concepts, or visualization examples are welcome.

### Contribution Workflow

```bash
# 1. Fork the repository

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/FDS---FUNDAMENTALS-OF-DATA-SCIENCE.git
cd FDS---FUNDAMENTALS-OF-DATA-SCIENCE

# 3. Create a descriptive branch
git checkout -b feature/add-hypothesis-testing

# 4. Add your file with this header template:
```

```python
"""
Module      : Hypothesis Testing
Topic       : Inferential Statistics
Description : Demonstrates one-sample and two-sample t-tests, p-value
              interpretation, and the decision rule for rejecting H₀.
Dependencies: numpy, scipy.stats, matplotlib

Concepts:
    - Null hypothesis (H₀) vs Alternative hypothesis (H₁)
    - p-value: probability of observing results at least this extreme
      assuming H₀ is true
    - Significance level α (commonly 0.05)
    - Decision: reject H₀ if p < α

Example:
    H₀: mean exam score = 70
    H₁: mean exam score ≠ 70
    Sample: [72, 74, 68, 75, 71, 73, 69, 76]
"""
```

```bash
# 5. Commit with a meaningful message
git commit -m "feat: Add hypothesis testing with t-test and p-value interpretation"

# 6. Push and open a Pull Request
git push origin feature/add-hypothesis-testing
```

### Contribution Standards

- Every module must include the **header docstring** shown above
- Scripts must run with a clear printed output — no silent execution
- Use `matplotlib.pyplot.show()` for any plots (or save with `savefig()`)
- Comments must explain the *statistical intuition*, not just the code syntax

---

## ⚙️ Tech Stack

| Technology | Role |
|------------|------|
| **Python 3.x** | Primary language for all implementations |
| **NumPy** | Numerical arrays, mathematical operations, linear algebra |
| **Pandas** | Data loading, cleaning, manipulation, and aggregation |
| **Matplotlib** | 2D data visualization and plotting |
| **SciPy** | Advanced statistical functions and distributions |

---

## 📜 License

Open-source under the **MIT License**. See [`LICENSE`](LICENSE) for full terms.

---

## 👨‍💻 Author

<div align="center">

### Mohammad Hassan

*Data science learner · Python practitioner · CS student*

[![GitHub](https://img.shields.io/badge/GitHub-mhassanworks-181717?style=for-the-badge&logo=github)](https://github.com/mhassanworks)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mohammad%20Hassan-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mohammad-hassan-b756352a9)

</div>

---

<div align="center">

## ⭐ Support This Repository

*If this helped you understand data science fundamentals — leave a star. It helps others find this resource.*

[![Star this repo](https://img.shields.io/github/stars/mhassanworks/FDS---FUNDAMENTALS-OF-DATA-SCIENCE?style=social)](https://github.com/mhassanworks/FDS---FUNDAMENTALS-OF-DATA-SCIENCE)

<br/>

```
Data loaded · Statistics computed · Insights visualized
```

<br/>

**© 2024 Mohammad Hassan · MIT License**

</div>
