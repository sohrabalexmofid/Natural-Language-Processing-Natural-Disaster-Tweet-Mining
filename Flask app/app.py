from flask import Flask, request, jsonify
import distilbert_model as model

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Congratulations! server is working'

@app.route('/get_sentiment', methods = ['post'])
def get_sentiment():
	tx = request.get_json(force= True)
	text = tx['text']

	sent= model.get_prediction(text)

	return jsonify(results= sent)


if __name__== '__main__':
	app.run(host= '0.0.0.0', port= 5000, debug = True, use_reloader= False)