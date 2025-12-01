---
title: syntax checking & spell correction for GridJs  
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: This article describes how to add syntax  checking & spell correction for GridJs.
keywords: GridJs,syntax checking,spell correction,syntax,spell,Grammar Checking,Grammar
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

 
# To perform syntax checking  & spell correction on user input ,the steps are
## Set load options.
for example:
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
## Set action URL for syntax  checking & spell correction.
for example:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
After a user enters text content in a cell, the action of syntax checking wil be triggered automatically by the spreadsheet application 

## Implement syntax  checking & spell correction  in serverside.
for example:
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




 
