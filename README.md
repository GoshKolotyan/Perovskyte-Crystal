# **Perovskite-Crystal Project**  

This project is part of a **research study** focused on predicting perovskite crystal **energy gaps (Eg)** using machine learning. It includes data processing, exploratory analysis, model selection, training, and large-scale predictions.  

---

## **Setup Instructions**  

### **1. Environment**  
- Dependencies are provided in the `.yml` file.  
- If using Conda, create and activate the environment with:  
  ```bash
  conda env create -f environment.yml
  conda activate <env_name>
  ```

### **2. Data**  
- Download the **two Excel files** from Google Docs.  
- Place them in the `data/` folder.

---

## **Notebook Workflow**  

The **analysis** is organized into a structured workflow inside the `analysis/` directory:  

```
analysis/
├── 1.prepare_data.ipynb             # Cleans and preprocesses raw data  
├── 2.analyse_prepared_data.ipynb    # Explores data distributions and dependencies  
├── 3.model_selection.ipynb          # Tests multiple models and selects the best  
├── 4.train.ipynb                    # Trains the selected model(s), computes feature importance  
├── 5.prepare_data_predict.ipynb     # Prepares a parameter grid for large-scale predictions  
├── 6.predict.ipynb                   # Applies trained models to predict Eg values  
└── 7.analyse_predictions.ipynb      # Compares multiple models and selects the best region  
```

---

## **Notebook Overview**  

1️⃣ **Prepare Data** (`1.prepare_data.ipynb`)  
   - Cleans and processes raw Excel files.  
   - Saves a prepared dataset in `data/`.  

2️⃣ **Analyze Prepared Data** (`2.analyse_prepared_data.ipynb`)  
   - Explores distributions of key parameters.  
   - Examines dependencies of `rA` (`xA, yA, zA`), `rC` (`xC, yC, zC`), and `Eg` (`rA, rC, TF, OF`).  
   - Includes comments with initial insights.  

3️⃣ **Model Selection** (`3.model_selection.ipynb`)  
   - Trains multiple machine learning models.  
   - Selects top-performing models based on evaluation metrics.  

4️⃣ **Train Model** (`4.train.ipynb`)  
   - Trains a **Random Forest** or another selected model.  
   - Performs **train-test split** (ensuring a specific row remains in the test set).  
   - Computes **feature importance** via permutation importance.  
   - Analyzes prediction errors. *(Final `Eg` dependency analysis will be completed after data correction.)*  

5️⃣ **Prepare Data for Prediction** (`5.prepare_data_predict.ipynb`)  
   - Generates a full **grid** of parameter values for large-scale predictions.  

6️⃣ **Run Predictions** (`6.predict.ipynb`)  
   - Uses trained models to **predict Eg** values for all grid points.  
   - Saves predictions in the `predictions/` folder.  

7️⃣ **Analyze Predictions** (`7.analyse_predictions.ipynb`)  
   - Compares results from multiple models.  
   - Selects the **best region** in the parameter space.  
   - Outputs a summary file with optimal conditions.  

---

## **Research Context**  
This project is part of a **scientific research paper** aimed at understanding and predicting the energy gaps of perovskite crystals using **machine learning techniques**.  

For further details, please refer to the accompanying **research paper**.  
