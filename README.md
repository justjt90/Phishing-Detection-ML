1. Introduction

In this modern world everyone is accessing the internet for different purpose. As the internet
grew; there are some problems like stealing data, hacking and fake web pages came into being.
To get rid of these phishing websites ‘phishing website detection website’ is very useful. It helps
users to understand what phishing is and how to stay safe while surfing the internet, because
people use their personal information like credentials and bank account details.
This project has three main parts. In the first part it has ‘URL detection’ method. In this
part what it does is when we access to the webpage, we don’t know that the web page we are
accessing is safe or not. So, in this first part when you copy the URL and search it tells you
weather the URL is phishing or not. In the second part ‘Mail phishing’ it tells user to copy the
email header and paste in to the given header to analyze it. Then it displays the result. In the last
part called ‘Wiki’ it tells you about the basic types of phishing and gives the basic idea of what is
phishing for the new user who doesn’t have any prior knowledge. So, it is very useful nowadays
because we have to do most of the things on the internet, so it should be safe and this project
achieve this goal.

Basic steps for phishing:

• Planning: attacker decides which business or organization to target and how to get email
ids of the customers for that organization. They often use the mass-mailing technique.

• Setup: Once they know which business to spoof and what their customers are, they find a
way to deliver the message with the spoof links or documents with company’s logo to get
trust from customers.

• Attack: This is the most familiar step for everyone; in this step phisher sends a phony
message that seems like from reputable source.

• Fraud: The data or information phisher gathered; they use it to fraud like transfer money
from other account or make illegal purchase.

2. Scope of The Project

Phishing is a considerable problem which differs from the other security threats such as
intrusions and Malware which are based on the technical security holes of the network systems.
The weakness point of any network system is its Users. Phishing attacks are targeting these users
depending on the trikes of social engineering. There are many possible ways to do phishing
but unfortunately, we have some techniques available nowadays can stop spear and email
phishing and therefore we need to build a system which can help us to stop phishing attacks. One
real example is the Google mail phishing attack happened some years ago and many users lost
their trust on Google. So, to avoid all these big threats, we need to think possible ways to avoid
large scale attacks to protect users. The scope for the phishing in this project is to save maximum
users on the web and the one who work on emails. The motto of the PHISHING DETECTION
project is when user is about to enter any information such as personal info or bank information
we recommend them to search that link or analyze the header of that email in the web detect site
first and if it shows the result is legitimate then they are safe to give the information over the
internet. The scopes of the project are as follows:

Phishing Detection
• To develop a system which can cover the large scope of safe surfing on the internet with
using URL detection method; URL is the most common type user interact with possible
viruses and attacks

• To begin the awareness of current threat and possible future fraud methods for all users
which can educate them about how to stay away from attacks and spam websites and not
to become them bate

• A good practical solution for big companies to keep their customer safe and win their trust
and give satisfied services.

• Mail header analyzing system introduced for big organizations and people as a good filter
to avoid scam happened through emails and links which lead them to fake web page.

• A very quick and user-friendly system to check and proceed with safety to save time,
money, energy and peace of mind.

CODE:

The back end has many parts and the programs have been written in the python language. The
list below will help understanding the role of each coding file.
1. Dataset: the folder contains the dataset for the project. The file name is phish coop; it has
been collected from the open machine learning dataset called UCI repository. the link for
the dataset is: https://archive.ics.uci.edu/ml/datasets/Phishing+Websites

2. Phishing features: In this PDF file it contains the 20 different techniques to check whether
the URL is phishing or not. The paper has been published by ResearchGate publication.
The link for the paper used for the project is below.

a. https://www.researchgate.net/publication/277476345_Phishing_Websites_Features

3. Models: In this folder there are three python files. Logistic Regression, Random Forest
and Support Vector Machine. All these three are machine learning algorithms to check
which algorithm will works the best and which algorithm gives the best accuracy.

4. Chrome-driver: Chrome-driver is a WebDriver (used for automation and testing) for
Chromium/Chrome. Used along with the Selenium module from Python, it covers a
myriad of our objectives such as finding backlinks for a website or finding features from a
mail header.

5. Index.py: This python file contains the endpoints of the Flask API which are consumed at
the frontend. https://documenter.getpostman.com/view/1034072/S17oxAFE

6. links.py: This python file is used to find the number of backlinks for a website using
Chrome Driver and this website. https://www.semrush.com/analytics/backlinks/

7. locator.py: This python file serves the purpose of finding public server location(s) for a
given domain. The ‘DNS’ package from python finds multiple external IP addresses for a
domain and the ‘geolite2’ package finds the world map coordinates for a given IP
address.

8. mail.py: This python file finds multiple features of a mail header using Selenium and
Chrome Driver. The websites used for this purpose are -:
a. https://toolbox.googleapps.com/apps/messageheader/
b. https://www.iptrackeronline.com/email-header-analysis.php

9. mail_Links.py: This python file analyzes the links to external websites found in a message
header. For each link, we use the URL phishing module of our application to predict
whether it is a legitimate or a phishing link.

10. modifiedScript.py: This python file is used to find the URL FEATURES of a given URL
as described below.

