from sklearn.externals import joblib
import modifiedScript
from flask import Flask,request,jsonify,send_file
from validators.url import url as urlcheck
import imgkit
from locator import url_locator
from email.parser import Parser
from mail import CheckMail
from mail_links import FindLinks

app = Flask(__name__)



@app.route('/send_file')
def send_shot():
	wkhtmlpath = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe'
	output_path = 'out.jpg'
	options={'quiet':''}
	config = imgkit.config(wkhtmltoimage=wkhtmlpath) #change this path according to your binary installation
	url = request.args["url_ajax"]
	try:
		imgkit.from_url(url,output_path, config=config,options=options)
		return send_file(output_path)
	except Exception as e:
		try:
			domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
			imgkit.from_url(domain,output_path, config=config,options=options)
			return send_file(output_path)
		except Exception as e:
			return send_file("error.jpg")
	return send_file("error.jpg")



@app.route('/send_location')
def send_location():
	try:
		output_path = 'out.jpg'
		url = request.args["url_ajax"]
		locations = url_locator.find_location(url)
		latitude=[str(i[0]) for i in locations]
		longitude=[str(i[1]) for i in locations]
		city=[str(i[2]) for i in locations]
		country=[str(i[3]) for i in locations]
		for location in locations:
			return jsonify(
				{
				"latitude":latitude,
				"longitude":longitude,
				"city":city,
				"country":country
				})
		return jsonify({"latitude":"null"})
	except Exception as e:
		return jsonify({"latitude":"null"})




@app.route('/send_result', methods=['POST'])
def call_model():
	try:
		classifier = joblib.load('final_models/rf_final.pkl')
		url = request.get_json()["url_ajax"]

		#validate url
		if not urlcheck(url):
			return jsonify({"prediction":"Invalid"})

		#checking and predicting
		features = modifiedScript.main(url)
		prediction = classifier.predict(features[0])
		return jsonify({
			"prediction":str(prediction[0]),
			"url_having_ip":str(features[1][0]),
			"url_length":str(features[1][1]),
			"url_short":str(features[1][2]),
			"having_at_symbol":str(features[1][3]),
			"doubleSlash":str(features[1][4]),
			"prefix_suffix":str(features[1][5]),
			"sub_domain":str(features[1][6]),
			"SSLfinal_State":str(features[1][7]),
			"domain_registration":str(features[1][8]),
			"https_token":str(features[1][9]),
			"request_url":str(features[1][10]),
			"url_of_anchor":str(features[1][11]),
			"Links_in_tags":str(features[1][12]),
			"email_submit":str(features[1][13]),
			"redirect":str(features[1][14]),
			"iframe":str(features[1][15]),
			"age_of_domain":str(features[1][16]),
			"web_traffic":str(features[1][17]),
			"google_index":str(features[1][18]),
			"links_pointing":str(features[1][19])
		})

	except Exception as e:
		print(e)
		return jsonify({"prediction":str(e)})


@app.route('/send_header', methods=['POST'])
def mail_header():
	try:
		header = request.get_json()["header_ajax"]
		parser = Parser()
		if parser.parsestr(header)['from'] is None:
			return jsonify({"header":"Invalid"})


		features = CheckMail.run(header)
		return jsonify({
			"header":"valid",
			"time":str(features["time"]),
			"SPF":str(features["SPF:"]),
			"DKIM":str(features["DKIM:"]),
			"DMARC":str(features["DMARC:"]),
			"IP":str(features["IP"]),
			"Hostname":str(features["Hostname"]),
			"Organization":str(features["Organization"]),
			"Country":str(features["Country"]),
			"City":str(features["City"]),
			"Latitude":str(features["Latitude"]),
			"Longitude":str(features["Longitude"])
		})

	except Exception as e:
		print(e)
		return jsonify({"header":"Invalid"})




@app.route('/mail_links', methods=['POST'])
def mail_links():
	try:
		header = request.get_json()["header_ajax"]
		parser = Parser()

		links_dict = FindLinks().find(header)
		links=[]
		predictions=[]
		for key,value in links_dict.items():
			links.append(str(key))
			predictions.append(str(value))

		return jsonify({
			"links":links,
			"predictions":predictions
		})

	except Exception as e:
		print(e)
		return jsonify({"header":"Invalid"})


@app.after_request
def add_headers(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	return response

if __name__ == "__main__":
	app.run(debug="on")

