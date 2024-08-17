# Titanic and Airplane Crash Survival Model

## Project Overview

This project combines two datasets—the Titanic dataset and the Airplane Crashes and Fatalities dataset—to create a more sophisticated survival prediction model. The goal is to explore survival factors across different modes of transportation, and develop a model that predicts the likelihood of survival based on various features.

## Data

### Titanic Dataset
- **Source**: [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)
- **Description**: The Titanic dataset contains information on passengers aboard the Titanic, including age, gender, passenger class, and whether they survived the disaster.

### Airplane Crashes and Fatalities Dataset
- **Source**: [Kaggle Airplane Crashes Dataset](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908)
- **Description**: This dataset includes records of airplane crashes since 1908, along with details such as the number of fatalities, location, and operator. This data is used to create additional features for the survival model.

## Model

The model uses a combination of features from both the Titanic and Airplane datasets. We trained a Random Forest Classifier, which is an ensemble learning method that combines multiple decision trees to improve prediction accuracy.

### Key Features:
- `Pclass`: Passenger class from the Titanic dataset.
- `Sex`: Gender of the passenger.
- `Age`: Age of the passenger.
- `Survival_Score`: A custom feature derived from the Airplane dataset, representing a safety score based on crash data.

## Results

- **Model Accuracy**: The final model achieved an accuracy of **82%** on the test data. This indicates that the model is fairly reliable in predicting survival based on the combined features from both datasets.
- **Insights**:
  - Gender (`Sex`) and passenger class (`Pclass`) were significant factors in survival prediction.
  - The `Survival_Score` derived from airplane crash data added an interesting dimension to the model, though its impact on accuracy was moderate.

## Instructions

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python libraries: `pandas`, `numpy`, `scikit-learn`, `joblib`, `seaborn`, `matplotlib`

### Steps to Run the Code

1. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/your_username/titanic-airplane-model.git
     ```

2. **Navigate to the Project Directory**:
   - Open the terminal and navigate to the cloned directory:
     ```bash
     cd titanic-airplane-model
     ```

3. **Install the Required Libraries**:
   - Install the necessary Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Open the Jupyter Notebook**:
   - Start Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook file (e.g., `titanic_airplane_model.ipynb`).

5. **Run the Notebook**:
   - Follow the steps in the notebook to load the datasets, preprocess the data, train the model, and evaluate its performance.

6. **(Optional) Deploy the Model**:
   - If you wish to deploy the model, follow the instructions provided in the `deployment` directory.

### Future Work

This project can be extended by:
- Incorporating more advanced machine learning techniques.
- Exploring additional features from the Airplane dataset.
- Deploying the model as a web application.

---

Thank you for exploring this project! If you have any questions or suggestions, feel free to open an issue or contribute to the repository.
