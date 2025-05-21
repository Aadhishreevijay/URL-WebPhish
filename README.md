# 🛡️Phishing Website Detection Using URL and Content Analysis

A hybrid machine learning system that combines **URL-based Analysis** using GANs with **content-based Analysis** using ensemble models. 

---

## Project Structure

```
.
├── Datasets/
│   ├── legitimate_sites.csv
│   ├── phishing_sites.csv
│   ├── New_legitimate.csv
│   ├── New_phishing.csv
│   ├── test_data.csv
│   └── url_data.zip
│
├── models/
│   ├── Scrape/
│   │   ├── data_collector.py
│   │   ├── feature_extraction.py
│   │   └── features.py
│   │
│   ├── ensemble/
│   │   ├── random_forest_model.joblib
│   │   ├── xgboost_model.joblib
│   │   ├── neural_network_model.joblib
│   │   └── voting_classifier_soft_model.joblib
│   │
│   └── gans/
│   |   ├── generator_model.h5
│   |   ├── discriminator_model.h5
│   |   └── gan_model.h5
│   └── utils/
│       └── Scaler.pkl
|
├── Combination.ipynb
├── ensemble.ipynb
├── gan_model.ipynb
│
├── LICENSE
└── README.md
```
---

## Datasets Overview

| Filename               | Description                    |
| ---------------------- | ------------------------------ |
| `legitimate_sites.csv` | Original legitimate URLs       |
| `phishing_sites.csv`   | Original phishing URLs         |
| `New_legitimate.csv`   | Legitimate + synthetic samples |
| `New_phishing.csv`     | Phishing + synthetic samples   |
| `test_data.csv`        | Test set for evaluation        |
| `url_data.zip`         | Compressed full URL dataset    |

---

## Models Used

### GAN

* Consists of:

  * `generator_model.h5`
  * `discriminator_model.h5`
  * `gan_model.h5`

### Ensemble

* Includes:

  * Random Forest
  * XGBoost
  * Neural Network
  * Voting Classifier

---



### Clone the Repository:

```bash
git clone https://github.com/Aadhishreevijay/URL-WebPhish
cd URL-WebPhish
````

### Run the following steps in order:

1. Run the scripts to collect and extract content features:

   ```bash
   python data_collector.py
   python feature_extraction.py
   ```

2. Open and run the notebook to train the GAN and generate synthetic URLs:

   * [`gan_model.ipynb`](./gan_model.ipynb)

3. Open and run the ensemble classifier training notebook:

   * [`ensemble.ipynb`](./ensemble.ipynb)

4. Open and run the notebook to combine predictions and evaluate:

   * [`Combination.ipynb`](./Combination.ipynb)

---

## License

This project is licensed under the [MIT License](LICENSE).



