---
title: Syntaxprüfung & Rechtschreibkorrektur für GridJs  
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Dieser Artikel beschreibt, wie man Syntaxprüfung & Rechtschreibkorrektur für GridJs hinzufügt.
keywords: GridJs, Syntaxprüfung, Rechtschreibkorrektur, Syntax, Rechtschreibung, Grammatikprüfung, Grammatik
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# Um Syntaxprüfung & Rechtschreibkorrektur bei Benutzereingaben durchzuführen, sind die Schritte
## Ladeoptionen festlegen.
zum Beispiel:
```javascript
 const option = {
     ...
     //set showCheckSyntaxButton to true
    showCheckSyntaxButton:true,
    //set checkSyntax to true
    checkSyntax:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Aktions-URL für Syntaxprüfung & Rechtschreibkorrektur festlegen.
zum Beispiel:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Nachdem ein Benutzer Textinhalt in eine Zelle eingegeben hat, wird die Syntaxprüfung automatisch vom Tabellenkalkulationsprogramm ausgelöst 

## Syntaxprüfung & Rechtschreibkorrektur serverseitig implementieren.
zum Beispiel:
```python
# The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
def correct_syntax(text, locale):  
# replace your logic  here     
    return text  

@app.route('/GridJs2/CheckSyntax', methods=['POST'])  
def check_syntax():  
    text = request.form.get('v')  
    locale = request.form.get('locale')  

    if not text:  
        return jsonify({  
            'Success': False,  
            'v': ''  
        }), 200  

    corrected_content = correct_syntax(text, locale)  

    return jsonify({  
        'Success': True,  
        'v': corrected_content  
    }), 200  
```





