import re
from sklearn.externals import joblib
from validators.url import url as urlcheck
import modifiedScript
import threading

class FindLinks:
	def __init__(self):
		self.classifier = joblib.load('final_models/rf_final.pkl')
		self.links=dict()

	def find(self,header):
		header=header.replace("=\n","")
		link_list = re.findall(r'(https?://[a-zA-Z./?#_&%$@!=0-9-]+)', header)
		for i in range(len(link_list)):
			if link_list[i][-1] is '.':
				link_list[i]=link_list[i][:-1]

		domains=[]
		
		link_list= list(set(link_list))		
		if len(link_list)<8:
			for link in link_list:
				if not urlcheck(link):
					link_list.remove(link)
			domains=link_list.copy()
		
		else:
			for link in link_list:
				domain=link.split("//")[0] + "//" + link.split("//")[-1].split("/")[0]
				if urlcheck(domain):
					domains.append(domain)

		domains= list(set(domains))

		threads=[]
		for domain in domains:
			thread = threading.Thread(target=self.run, args=([domain]))
			#thread.daemon=True
			thread.start()
			threads.append(thread)

		i=1
		for thread in threads:
			thread.join()
			i=i+1

		return self.links

		

	def run(self,url):
		features = modifiedScript.main(url)
		prediction = str(self.classifier.predict(features[0])[0])
		self.links[url]=prediction





