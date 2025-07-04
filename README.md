
# 🌊 Sea Level Predictor

This project analyzes the rise in sea levels from 1880 to 2050 using historical data provided by the EPA (Environmental Protection Agency). It visualizes the data and applies linear regression to project future sea levels.

## 📁 Files Included

- `sea_level_predictor.py` – Main Python script for reading data, performing regression, and plotting.
- `sea_level_plot.png` – Output plot visualizing historical sea level data with fitted trend lines.
- `epa-sea-level.csv` – (Required) Dataset containing year-wise sea level data.

## 📊 What the Plot Shows

- **Blue Dots:** Historical sea level measurements from 1880 onwards.
- **Red Line:** Linear regression line fitted using all data from 1880–2050.
- **(Optional) Green Line:** Trend line using data from the year 2000 onwards to show recent changes (if data from 2000+ is available).

## 🚀 How to Run

### 1. Ensure Required Libraries Are Installed
```bash
pip install pandas matplotlib scipy
```

### 2. Place the CSV Data File
Download and place `epa-sea-level.csv` in the same directory. Make sure it includes the following columns:
- `Year`
- `CSIRO - Adjusted sea level (inches)`

### 3. Run the Script
```bash
python sea_level_predictor.py
```

### 4. Output
- The plot will be saved as `sea_level_plot.png`.
- Console output:
  ```
  Plot saved as 'sea_level_plot.png'
  ```

## 📈 Example Output

The plot clearly shows a rising trend in sea levels, helping to visualize the impact of climate change over time and providing a forecast up to the year 2050.
