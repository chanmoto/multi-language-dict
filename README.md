# Multi Language Dictionary   

This app performs GOOGLE translations in 5 languages and stocks the SQLITE  

The GOOGLE-API (for a fee) is required for translation.  

1)get google api  
2)rewrite below code  

dict_page/templates/content.html  
######################  
function translate(lang,elem){  
var uri = 'https://www.googleapis.com/language/translate/v2';    ##<---- get api key  
var q =  inputtxt.value;  
var key='write api key here';    ##<----   here  
######################  

Directory  

C:.  
│  .gitignore  
│  db.sqlite3  
│  manage.py  
│  README.md  
│  requirements.txt  
│  
├─dict_app  
│  │  settings.py  
│  │  urls.py  
│  │  wsgi.py  
│  
└─dict_page  
    │  admin.py  
    │  apps.py  
    │  forms.py  
    │  models.py  
    │  tests.py  
    │  urls.py  
    │  utils.py    
    │  views.py  
    │  
    ├─migrations  
    │  
    ├─templates  
    │      about.html  
    │      base.html  
    │      content.html       #####<----- this file must be rewritten  
    │      home.html  
    
    
    
3)   pip install -r requirements.txt  
4)   python manage.py runserver 0.0.0.0:8000   ##<---- your app enviroment  
