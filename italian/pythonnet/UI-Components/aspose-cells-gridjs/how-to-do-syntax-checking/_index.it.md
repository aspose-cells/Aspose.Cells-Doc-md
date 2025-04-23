---
title: controllo della sintassi & correzione ortografica per GridJs  
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Questo articolo descrive come aggiungere controllo della sintassi & correzione ortografica a GridJs.
keywords: GridJs,controllo della sintassi,correzione ortografica,sintassi,ortografia,Controllo grammaticale,Controllo grammaticale
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# Per eseguire il controllo della sintassi e la correzione ortografica sull'input dell'utente, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
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
## Imposta l'URL dell'azione per il controllo della sintassi e la correzione ortografica.
ad esempio:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Dopo che un utente inserisce il contenuto di testo in una cella, l'azione di controllo della sintassi verrà attivata automaticamente dall'applicazione del foglio di calcolo 

## Implementa il controllo della sintassi e la correzione ortografica lato server.
ad esempio:
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





