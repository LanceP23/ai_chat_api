import mlflow 
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd 
import mlflow.pyfunc

df = pd.read_csv('./data/engineers.csv')
X = df[['years_experience', 'age']]
y = df['salary']

run_id ="1d33e37cec5943078aececc34c41c22b"
model_uri = f"runs:/{run_id}/salary_model"

loaded_model = mlflow.pyfunc.load_model(model_uri)
test_input = pd.DataFrame([[7, 30]], columns=['years_experience', 'age'])
result = loaded_model.predict(test_input)
print(f"Predicted salary for 7 years exp, age 30: {result[0]}")
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state =42)

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)


    mlflow.log_metric("mae", mae)
    mlflow.sklearn.log_model(model, "salary_model")

    print(f"MAE: {mae}")
    print(f"Run ID: {mlflow.active_run().info.run_id}")

