# Leishmaniasis treatment outcome prediction based on metabolomics

Here are all the scripts and models used in the exploratory project for the
leishmaniasis treatment outcome prediction using machine learning based on
patients metabolomic information.

## Project structure

```
./
├── data_exploration.ipynb
├── data_sets
│   ├── ds1.csv
│   ├── ds2.csv
│   ├── ds3.csv
│   ├── Supplementary_Dataset_S1.xlsx
│   ├── Supplementary_Dataset_S2.xlsx
│   └── Supplementary_Dataset_S3.xlsx
├── notebooks
│   ├── helpers
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── preprocessing.py
│   │   └── sets.py
│   ├── JaverianaML
│   │   ├── data_util.py
│   │   ├── model_util.py
│   │   ├── plots_util.py
│   │   └── preprocessing_util.py
│   ├── models_post
│   │   ├── models_CIDEIM.ipynb
│   │   ├── models_f_classif.ipynb
│   │   ├── models_full_dataset.ipynb
│   │   ├── models_intersection.ipynb
│   │   └── models_rfe.ipynb
│   ├── models_pre
│   │   ├── models_CIDEIM.ipynb
│   │   ├── models_f_classif.ipynb
│   │   ├── models_full_dataset.ipynb
│   │   ├── models_intersection.ipynb
│   │   └── models_rfe.ipynb
│   ├── subset_metrics
│   │   ├── subsets_metrics_post.ipynb
│   │   └── subsets_metrics_pre.ipynb
│   └── subsets
│       ├── post_subsets.ipynb
│       └── pre_subsets.ipynb
└── README.md
```

- **data_sets:** Datasets with only the metabolomic information about the patients
- **notebooks:** Jupyter notebooks with the scripts that make the exploration
- **notebooks/helpers:** Variables of metabolites subsets and auxiliary functions for preprocessing and metrics display
- **notebooks/JaverianaML:** Wrappers of common data science functions
- **notebooks/models_post:** Scripts with the exploration of post-treatment dataset
- **notebooks/models_pre:** Scripts with the exploration of pre-treatment dataset
- **notebooks/subset_metrics:** Scripts with first look at subsets performance
- **notebooks/subsets:** Scripts with the extraction of metabolites subsets
