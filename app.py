from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load('./model.pkl')

@app.route('/')
def hello():
    return 'Home Page for Prediction of Species Type'


@app.route('/predict',methods=["GET", "POST"])
def predict():
    print("START")
    sepalLength = float(request.args.get("sepalLength"))
    print(sepalLength)
    sepalWidth  = float(request.args.get("sepalWidth"))
    print(sepalWidth)
    petalLength = float(request.args.get("petalLength"))
    print(petalLength)
    petalWidth  = float(request.args.get("petalWidth"))
    print(petalWidth)

    results = model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])

    print('PREDICTION IS: ', results[0])

    return results[0]


if __name__ == "__main__":
  app.run(host ='0.0.0.0')

