WordRef


All information extracted credits to WordReference.com

This is a flask app, to run the app you would need to have python3 and flask installed.

Also, would need the following python modules:

- requests
- bs4
- lxml

To run app: 
    
    Clone repo
    
    Go to directory 
    
    python WordRefScrape.py
    
    Open browser and go to localhost (prob 5000)
    

Use `/api/resources/wordref?word=` in url and fill in word that you want to search for

Currently app only works from french to english


ex: 'http://localhost:5000/api/resources/wordref?word=bonjour'

