from flask import Flask

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

df = pd.read_csv('data.csv')

X = df.drop('Result', axis=1)
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)


@app.route('/<num>&<age>&<comp>&<hist>&<rent>')
def prediction(num, age, comp, hist, rent):
    d = {
        'NumberOfPeople': [int(num)],
        'AverageAge': [int(age)],
        'NumberOfCompetitors': [int(comp)],
        'IsHistoricalPlace': [int(hist)],
        'AverageRentalPrice': [int(rent)]
    }
    X_input = pd.DataFrame(data=d)

    pred = regressor.predict(X_input)
    result = str(round(pred[0]) % 100)
    return result


if __name__ == '__main__':
    app.run()
