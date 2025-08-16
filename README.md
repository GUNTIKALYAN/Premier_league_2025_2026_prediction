## Premier League 2025/26 Prediction

This project predicts the top 3 and bottom 3 teams in the Premier League for the 2025/26 season using machine learning models like Random Forest and XGBoost.

The dataset includes past season statistics such as matches played, wins, draws, losses, goals scored, goals conceded, and total points.

## Features

Data preprocessing and cleaning from historical Premier League tables.

Exploratory data analysis and visualization of team performance.

Model training using:

Random Forest Classifier

XGBoost Classifier

Evaluation of models using accuracy, precision, recall, and F1-score.

Prediction of top 3 and bottom 3 teams for the upcoming season.


## Project Structure

```bash
├── premier_league.ipynb   # Main Jupyter Notebook
├── data/                  # CSV files of past PL seasons (not included in repo)
├── README.md              # Project documentation
```

## Clone
```bash
git clone https://github.com/yourusername/premier_league_prediction.git
cd premier_league_prediction
pip install -r requirements.txt
```

## requirements.txt

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```
## Output

```bash
PREDICTED TOP 3 FOR 2025/26:
🥇 1. Liverpool       - 82.0 points
🥈 2. Man City        - 74.8 points
🥉 3. Arsenal         - 68.9 points
```

```bash
  PREDICTED RELEGATION ZONE:
18. Southampton     - 7.9 points
19. Leicester City  - 14.7 points
20. Wolverhampton   - 41.1 points
```
