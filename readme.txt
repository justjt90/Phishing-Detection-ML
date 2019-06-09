Tested on Python Version 3.5.4
Download the required python packages (flask, selenium, validators, imgkit, geolite2, wkhtmltopdf)
if server(backend on windows), install the wkhtmltopdf binaries and add wkhtmltoimg.exe to environment variables.
selenium requires chrome or chromium to be installed on the backend side.
Execute index.py to start the server on localhost. Read the console output, If the server starts on any port other than 5000, replace 5000 with the current port number in url_ajax.js file in the js folder (in the frontend).