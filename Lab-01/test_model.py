
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def test_iris_model_pipeline():
    # Load the dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the data reproducibly
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Train the model
    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Generate predictions
    predictions = model.predict(X_test)

    # Automated checks
    assert len(predictions) == len(y_test)
    assert set(predictions).issubset(set(y))
    assert accuracy_score(y_test, predictions) >= 0.80
