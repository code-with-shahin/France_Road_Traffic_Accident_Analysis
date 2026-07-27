# France Road Traffic Accident Analysis (2021–2024)

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Python](https://img.shields.io/badge/Python-Data%20Preparation-blue)
![SQL](https://img.shields.io/badge/SQL-Data%20Modeling-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

An end-to-end data analytics project that analyzes **road traffic accidents resulting in personal injury in France between 2021 and 2024**. The project transforms raw government accident data into an interactive **Power BI dashboard** to uncover accident trends, identify high-risk groups, evaluate environmental factors, and support data-driven road safety decisions.

The project follows modern analytics best practices, including **data cleaning, dimensional modelling, Power Query transformations, DAX calculations, and interactive dashboard design**.

---

# Table of Contents

- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Dataset](#dataset)
- [Data Model](#data-model)
- [Project Workflow](#project-workflow)
- [Dashboard Features](#dashboard-features)
- [Key Performance Indicators](#key-performance-indicators)
- [Key Insights](#key-insights)
- [Tools & Technologies](#tools--technologies)
- [Project Contribution](#project-contribution)
- [Repository Structure](#repository-structure)
- [Future Improvements](#future-improvements)
- [Dashboard Preview](#dashboard-preview)
- [Author](#author)

---

# Project Overview

Road traffic accidents remain one of the leading causes of injury and fatalities worldwide. Understanding when, where, and why accidents occur is essential for improving road safety and supporting evidence-based policy decisions.

This project analyzes official French road traffic accident data from **2021–2024** to identify accident patterns across different demographic groups, environmental conditions, road characteristics, and geographical locations.

The final deliverable is an interactive Power BI dashboard that enables users to explore accident data through dynamic visualizations and key performance indicators.

---

# Project Objectives

The analysis aims to answer the following business questions:

- How have road traffic accidents changed between 2021 and 2024?
- Which demographic groups are most frequently involved in accidents?
- How do weather and lighting conditions influence accident occurrence?
- Which road characteristics are associated with more severe accidents?
- Where are accident hotspots located across France?
- How can interactive dashboards support road safety analysis and decision-making?

---

# Dataset

The project uses the official French road traffic accident datasets containing **personal injury accidents** recorded between **2021 and 2024**.

The analysis combines four annual datasets containing detailed information about:

- Accident characteristics
- Road users
- Vehicles involved
- Accident locations

### Main Data Tables

- Characteristics
- Users
- Vehicles
- Locations

---

# Data Model

To improve reporting performance and simplify analysis, the data was transformed into a **Star Schema**.

### Fact Table

- Fact_Users

### Dimension Tables

- Dim_Date
- Dim_Vehicles
- Dim_Locations
- Dim_Weather

The dimensional model enables efficient filtering, reusable DAX measures, and scalable dashboard development.

---

# Project Workflow

## 1. Data Exploration

- Load annual datasets
- Inspect data structure and column types
- Identify missing values
- Explore relationships between tables

---

## 2. Data Preparation

Data preprocessing included:

- Cleaning missing values
- Removing duplicate records
- Correcting data types
- Creating calculated columns
- Standardizing categorical values
- Power Query transformations
- Building relationships
- Creating a dedicated Date table

---

## 3. Data Modeling

- Design a Star Schema
- Create dimension tables
- Establish one-to-many relationships
- Optimize the semantic model for reporting

---

## 4. Dashboard Development

Power BI was used to build an interactive dashboard featuring:

- Executive KPI cards
- Trend analysis
- Geographic mapping
- Demographic insights
- Environmental analysis
- Road infrastructure analysis
- Interactive slicers and drill-down functionality

---

# Dashboard Features

The dashboard provides multiple analytical views.

## Accident Overview

- Total accidents
- Total road users involved
- Fatal accidents
- Serious injuries

---

## Temporal Analysis

- Accidents by Year
- Monthly accident trends
- Seasonal patterns
- Lighting and Atmospheric conditions

---

## Users Analysis

- Age distribution
- Gender distribution
- User categories
- Safety equipment usage

---

## Geographical Analysis

- Road category
- Speed limit
- Road surface conditions
- Interactive accident map

---

# Key Performance Indicators

The dashboard includes several DAX measures, including:

- Total Accidents
- Total Users Involved
- Total Vehicles Involved
- Average Age
- Fatal Accident Count
- Serious Injury Count
- Accident Rate
- Year-over-Year Growth
- Percentage of Severe Accidents
- Accidents per 1,000 Users

---

# Key Insights

The analysis revealed several important patterns:

- Accident frequency fluctuates throughout the year, with clear seasonal trends (more accidents in Summer compared to Winter).
- Poor lighting conditions are associated with a higher proportion of severe accidents (fewer fatal accidents at night with street lighting).
- Young drivers (20-25 year-olds) and road users account for a significant share of reported accidents.
- Urban areas experience considerably higher accident volumes than rural regions.
- Weather conditions influence both accident frequency and injury severity (more fatal accidents in foggy and stormy weather).
- Geographic analysis highlights departments with consistently higher accident concentrations (Paris and Marseille), helping identify potential road safety hotspots.

The dashboard enables the audience to identify quickly:

- High-risk demographic groups
- Accident hotspots
- Seasonal accident trends
- Environmental risk factors
- Areas requiring targeted road safety interventions

---

# Tools & Technologies

- Microsoft Power BI Desktop
- Power Query
- DAX
- Python
- SQL
- Microsoft Excel
- Data Modelling
- Star Schema

---

# Project Contribution

This project demonstrates the complete business intelligence workflow, from raw data preparation to interactive reporting.

Key contributions include:

- Designing an optimized Star Schema data model
- Cleaning and transforming large multi-year datasets using Power Query
- Developing reusable DAX measures and KPIs
- Creating interactive Power BI dashboards
- Designing clear analytical storytelling for business users
- Translating complex accident data into actionable insights

The primary focus was on transforming raw transportation data into an intuitive reporting solution that supports road safety analysis and informed decision-making.

---

# Repository Structure

```text
France_Road_Traffic_Accident_Analysis/
│
├── Datasets/
│   ├── Raw Data/
│   └── Clean Data/
│
├── Images/
│   ├── dashboard_overview.png
│   ├── temporal_analysis.png
│   ├── users_analysis.png
│   └── geographical_analysis.png
│
├── SQL/
│   └── France_SQL.sql
│
├── PowerBI/
│   ├── Calendar DAX.txt
│   └── France.pbix *(Available upon request; omitted because the file exceeds GitHub's 25 MB limit.)*
│
└── README.md
```

---

# Future Improvements

Potential future enhancements include:

- Predict accident severity using Machine Learning
- Integrate real-time weather data through APIs
- Implement accident forecasting models
- Perform GIS-based hotspot analysis
- Develop a real-time monitoring dashboard
- Add advanced drill-through reports and mobile-optimised layouts

---

# Dashboard Preview

## Executive Dashboard

<img width="1364" height="789" alt="2026-07-20 22_54_23-France" src="https://github.com/user-attachments/assets/555e1477-7979-4287-832a-af0fa4ec27d1" />

---

## Temporal Analysis

<img width="1442" height="800" alt="tempo" src="https://github.com/user-attachments/assets/820f4091-6a0e-48bd-b7ca-98f9a8ed2b80" />

---

## User Analysis

<img width="1444" height="800" alt="user" src="https://github.com/user-attachments/assets/52f25b84-83dc-4b9f-a30a-ea5d7ef399cf" />

---

## Geographic Analysis

<img width="1444" height="798" alt="geo" src="https://github.com/user-attachments/assets/e3c09165-4d5d-463f-b8b6-1faecd81978e" />

---

# Author

## Shahin Amirov

**Microsoft Certified: Power BI Data Analyst Associate (PL-300)**

Data Analyst | Power BI | SQL | Python

🔗 LinkedIn:  
https://www.linkedin.com/in/shahin-amirov/

💻 GitHub:  
https://github.com/code-with-shahin/

---

## Support

If you found this project interesting or useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome!
