import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

DATA_PATH = "data/premier_league_standings_2022_2025.csv"

_model = None
_feature_columns = None
_team_encoder = None


def _feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Encode teams numerically
    global _team_encoder
    if _team_encoder is None:
        _team_encoder = {team: idx for idx, team in enumerate(df["Team"].unique())}

    df["TeamCode"] = df["Team"].map(_team_encoder)

    # Derived metrics 
    df["PointsPerMatch"] = df["Points"] / df["Matches"]
    df["GoalRatio"] = df["GoalsFor"] / (df["GoalsAgainst"] + 1)
    df["AttackRate"] = df["GoalsFor"] / df["Matches"]
    df["DefenseRate"] = df["GoalsAgainst"] / df["Matches"]

    return df


def _prepare_training_data(df: pd.DataFrame):
    # Sort to create next-season target
    df = df.sort_values(["Team", "Season"])

    # Target: next season points
    df["PointsNext"] = df.groupby("Team")["Points"].shift(-1)

    # Drop rows without target
    df = df[df["PointsNext"].notnull()].copy()

    df = _feature_engineering(df)

    X = df[
        [
            "Points",
            "GoalDiff",
            "GoalsFor",
            "GoalsAgainst",
            "TeamCode",
            "AttackRate",
            "DefenseRate",
            "PointsPerMatch",
            "GoalRatio",
        ]
    ]

    y = df["PointsNext"]

    return X, y


def train_model():
    global _model, _feature_columns

    df = pd.read_csv(DATA_PATH)

    X, y = _prepare_training_data(df)
    _feature_columns = X.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=400,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print(f"Model trained | MAE: {mae:.2f} points")

    _model = model
    return mae


def predict(features: dict):
    if _model is None:
        raise RuntimeError("Model not trained")

    df = pd.DataFrame([features])

    # Encode team
    if "Team" not in df:
        raise ValueError("Team name is required for prediction")

    df["TeamCode"] = df["Team"].map(_team_encoder)

    if df["TeamCode"].isnull().any():
        raise ValueError("Unknown team name")

    # Feature engineering
    df["PointsPerMatch"] = df["Points"] / df["Matches"]
    df["GoalRatio"] = df["GoalsFor"] / (df["GoalsAgainst"] + 1)
    df["AttackRate"] = df["GoalsFor"] / df["Matches"]
    df["DefenseRate"] = df["GoalsAgainst"] / df["Matches"]

    X = df[_feature_columns]

    prediction = _model.predict(X)[0]

    return {
        "predicted_points_next_season": round(float(prediction), 2)
    }
