# Multi Language Dictionary   

This app performs microsoft translations in multi languages and stocks the SQLITE  

The microsoft-API is required for translation.  

1)get microsoft api-key   
    https://api.cognitive.microsofttranslator.com'  
    
2)rewrite to next code  

dict_page/config.py

```python
######################  

subscription_key = 'your api key'
        
######################  
```


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
    │  config.py   #####<----- this file must be rewritten  
    │  
    ├─migrations  
    │  
    ├─templates  
    │      about.html  
    │      base.html  
    │      content.html       
    │      home.html  
    
    
    
3)   pip install -r requirements.txt  
4)   python manage.py runserver 0.0.0.0:8000   ##<---- your app enviroment  
