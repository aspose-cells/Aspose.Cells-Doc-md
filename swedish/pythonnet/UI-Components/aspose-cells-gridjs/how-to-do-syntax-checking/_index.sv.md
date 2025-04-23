---
title: Syntaxkontroll & stavningskorrigering för GridJs  
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Den här artikeln beskriver hur man lägger till syntaxkontroll & stavningskorrigering för GridJs.
keywords: GridJs, syntaxkontroll, stavningskorrigering, syntax, stavning, grammatikgranskning, grammatik
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# För att utföra syntaxkontroll & stavningskorrigering på användarens inmatning, är stegen
## Sätt laddningsalternativ.
till exempel:
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
## Sätt action URL för syntaxkontroll & stavningskorrigering.
till exempel:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Efter att en användare skriver in textinnehåll i en cell, kommer syntaxkontrollen att utlösas automatiskt av kalkylplatsapplikationen 

## Implementera syntaxkontroll och stavningsrättning på serversidan.
till exempel:
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





