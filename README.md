# Perovskite-Crystal: Predicting Energy Gaps Using Machine Learning and DFT

This repository contains the code and workflow from our research paper  
**“Accelerated composition optimization of hybrid perovskites via data-driven materials design, DFT calculations, and synthesis” (Materials & Design, 2025).**

[Published Paper (Elsevier)](https://doi.org/10.1016/j.matdes.2025.114902)

---

## Project Highlights
- Integrates **Density Functional Theory (DFT)** and **experimental datasets** for accurate bandgap (Eg) prediction.  
- Implements **Random Forest** and **Bossting Alogorithms** for regression analysis.  
- Achieves **R² > 0.9** correlation between predicted and calculated bandgaps.  
- Enables **large-scale composition screening** to identify optimal perovskite candidates.  

---

## Setup Instructions

### Environment
```bash
conda env create -f environment.yml
conda activate perovskite-crystal-env
```

### Data
- Dataset includes both **DFT-calculated** and **experimentally measured** bandgaps.  
- Place both Excel data files in the `data/` directory.  
- If dataset is not public, contact the authors for access.  

---

## Workflow Overview

| Step | Notebook | Description |
|------|-----------|-------------|
| 1️⃣ | [1.prepare_data.ipynb](analysis/1.prepare_data.ipynb) | Clean and merge DFT + experimental datasets |
| 2️⃣ | [2.analyse_prepared_data.ipynb](analysis/2.analyse_prepared_data.ipynb) | Explore distributions and feature correlations |
| 3️⃣ | [3.model_selection.ipynb](analysis/3.model_selection.ipynb) | Train and evaluate multiple regression models |
| 4️⃣ | [4.train.ipynb](analysis/4.train.ipynb) | Train final model, compute feature importances |
| 5️⃣ | [5.prepare_data_predict.ipynb](analysis/5.prepare_data_predict.ipynb) | Generate parameter grid for large-scale predictions |
| 6️⃣ | [6.predict.ipynb](analysis/6.predict.ipynb) | Apply trained model for Eg predictions |
| 7️⃣ | [7.analyse_predictions.ipynb](analysis/7.analyse_predictions.ipynb) | Compare predictions and identify optimal compositions |

---

## Model and Features

The models use **physically interpretable descriptors** derived from perovskite geometry and chemistry:  
- **rA, rC:** ionic radii of A- and C-site atoms  
- **TF:** Tolerance Factor  

## Research Context

This study integrates **data-driven machine learning** with **first-principles DFT calculations** to accelerate the discovery of new hybrid perovskites. By bridging experimental and theoretical data, the model provides a pathway toward efficient **composition optimization** for **solar cell and optoelectronic** applications.

---

## Citation

If you use this repository or related datasets, please cite:

> S. Grigoryan, N. Petrosyan, G. Kolotyan, A. Kozmanyan, V. Avetisyan, H. Zakaryan, M. J. Schöning, A. Asatryan, H. Khachatryan,  
> *Accelerated composition optimization of hybrid perovskites via data-driven materials design, DFT calculations and synthesis*,  
> **Materials & Design**, 2025. DOI: [10.1016/j.matdes.2025.114902](https://doi.org/10.1016/j.matdes.2025.114902)

---

## Contact

For research collaborations or questions, please contact:  
📧 **goshkolotyan@gmail.com**  
