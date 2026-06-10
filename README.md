# dataset-label-analyzer

# Dataset Label Analyzer

A simple Streamlit application for analyzing annotation datasets.

## Features

* Upload CSV datasets
* Dataset summary
* Label distribution analysis
* Interactive visualization using Plotly
* Detection of potentially inconsistent labels using RapidFuzz

## Example CSV Format

```csv
filename,label
img1.jpg,car
img2.jpg,car
img3.jpg,bus
img4.jpg,bus
img5.jpg,bus
img6.jpg,truck
img7.jpg,bike
img8.jpg,Car
<img width="65" height="201" alt="image" src="https://github.com/user-attachments/assets/6d74aff6-4a29-4607-9c04-7d77990e1557" />

```

## Installation

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* RapidFuzz

## Motivation

This project was inspired by a common challenge in data annotation workflows: maintaining label consistency and understanding dataset distribution efficiently.

