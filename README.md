# Predicting Cutaneous Leishmaniasis Treatment Response with Machine Learning

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Result](https://img.shields.io/badge/precision-92%25-2dd4bf?style=flat-square&labelColor=0d1117)

Code for my undergraduate thesis in Systems Engineering & Computer Science (Pontificia Universidad Javeriana Cali), developed with **CIDEIM** (Centro Internacional de Entrenamiento e Investigaciones Médicas) while I worked there as a Machine Learning Research Assistant (2020–2022).

## The problem

Cutaneous leishmaniasis is a neglected tropical disease, and not every patient responds to first-line treatment. Knowing in advance which patients are likely to fail lets clinicians adjust the therapy sooner. The goal was a supervised model that predicts treatment response from the patient's clinical data.

The hard part is the data: clinical datasets are **small and imbalanced** (far fewer treatment failures than successes). A model that ignores this learns to predict "success" for everyone.

## Approach

1. **Cleaning and preprocessing**: dropping variables that don't apply clinically, translating and renaming fields, handling missing values and encoding.
2. **Baseline models** trained on the original data, without augmentation.
3. **Synthetic data augmentation** to rebalance the classes, comparing six techniques:
   - SMOTE · Borderline-SMOTE · ADASYN
   - Gaussian Mixture Models (GMM)
   - Genetic algorithm
   - Generative adversarial networks (GAN)
4. **Ensemble techniques** on top of the best datasets, compared on precision, recall and F1.
5. The whole pipeline was repeated on a **second dataset** that CIDEIM provided in the final months of the research.

**Result:** the final model reached **92% precision**. The work was published as a co-authored research article and the thesis received an **excellence award**.

## Repository structure

```
Thesis_Scripts/
├── dataset-1/                       # initial CIDEIM dataset (most of the research)
│   ├── 1-without_data_augmentation/ # cleaning, exploration, baseline experiments
│   └── 2-with_data_augmentation/    # SMOTE, Borderline-SMOTE, ADASYN, GMM, GENETIC, GAN + results
└── dataset-2/                       # same pipeline adapted to the second dataset
EntregaTesis/                        # final notebooks (preprocessing, ensembles) and thesis PDF
tesis-leishmaniasis/                 # supporting code
```

Each `1-without_data_augmentation` and `2-with_data_augmentation` folder has its own README explaining the order and purpose of each notebook.

## Related

- [**LeishPredict-web**](https://github.com/2203juan/LeishPredict-web): Flask web app that serves the model.

## Author

**Juan José Hoyos Urcué** · [Website](https://2203juan.github.io/my-site/) · [LinkedIn](https://www.linkedin.com/in/hoyosjuan)
