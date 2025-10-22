# Premier League Points Prediction (2025/26 Season)

A machine learning project to predict the next season points for Premier League teams using historical data (2022–2025). The system predicts the full league table, including top 3 teams and relegation zone, and provides team-wise insights.

---

##  Features

- Data preprocessing and cleaning of historical Premier League data.
- Feature engineering:
  - Attack Rate (Goals For / Matches)
  - Defense Rate (Goals Against / Matches)
  - Points per Match
  - Goal Ratio (Goals For / Goals Against)
- Implemented machine learning models:
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
- Model selection using **GridSearchCV** and evaluation with RMSE and R² scores.
- Predicts next season points and league positions.
- Provides insights into feature importance for better understanding of team performance.

---

##  Dataset

The dataset contains Premier League standings for 2022–2025, including:

- `Team` — Name of the team  
- `Season` — Season year  
- `Matches` — Number of matches played  
- `GoalsFor` — Goals scored  
- `GoalsAgainst` — Goals conceded  
- `Points` — Total points earned  
- `GoalDiff` — Goal difference  

**Note:** The target variable is `PointsNext` (points for the next season).

## Predicted 2025/26 League Table Highlights

Top 3 Teams:

1. Liverpool – 82.0 points

2. Man City – 74.8 points

3. Arsenal – 68.9 points

Relegation Zone:

18. Southampton – 7.9 points

19. Leicester City – 14.7 points

20. Wolverhampton – 41.1 points

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/GUNTIKALYAN/Premier_league_2025_2026_prediction.git
```

```bash
cd Premier_league_2025_2026_prediction
```
