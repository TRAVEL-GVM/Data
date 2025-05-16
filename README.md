# 📦 Data Automation Repository

This repository contains the **data extraction automation infrastructure** using **GitHub Actions** to feed Streamlit applications with regularly updated data from the web.

---

## 🚀 Purpose

To reduce the loading time of Streamlit applications by automatically and periodically extracting external data (e.g., web scraping, APIs) and storing it in the repository.  
Each folder corresponds to an independent project with its own scripts and automation workflows.

---

## 🧰 Repository Structure

Data
  ├── .github/workflows/ # GitHub Actions workflows (.yml files)
  
  ├── Calibration_LDP/ # Python scripts for the LDP calibration project
  
  ├── Data/ # Folder where the extracted data files are saved
  
  ├── EMFs/ # Scripts for EMFs-related data extractions
  
  ├── MarketRisk/ # Scripts for market risk data extraction
  
  └── README.md # Project documentation (this file)
  
---

## ⚙️ How It Works

- Each project folder (e.g., `Calibration_LDP`, `MarketRisk`) contains:
  1. Python scripts that fetch and process data from external sources
  2. Code that saves the cleaned data to the `Data/` folder

- **GitHub Actions** are configured to:
  - Automatically run these scripts on a **fixed schedule**
  - Save the updated data outputs
  - Commit the results directly to the repository

---

## 🧪 Automation with GitHub Actions

The workflows defined in `.github/workflows/` handle task scheduling. Example:

```yaml
on:
  schedule:
    - cron: "0 6 * * *"  # Runs every day at 6:00 AM UTC
```

These automated jobs ensure that the data in the Data/ folder is always up to date, avoiding heavy on-demand loads in real time.

## 📊 Data Usage
Streamlit applications associated with this repository read directly from the Data/ folder, enabling fast loading and consistent access to the most recent available data.

## 📝 Notes
This repository is not intended for direct analysis or visualization.

The goal is to centralize and automate the data collection process for downstream applications.

Workflow failures (e.g., due to connectivity or source changes) can be reviewed in the GitHub Actions logs.

## 👥 Team
This project is part of the TRAVEL-GVM initiative, focused on the automation and modernization of data processes in risk management and statistical modeling.
