---
title: Formel Erklärung für GridJs anzeigen  
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Dieser Artikel beschreibt, wie man die Formel Erklärung für GridJs anzeigt.
keywords: GridJs,Formel,Formel Erklärung,Formel Erklärung anzeigen,Formel Interpreter
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Um die Formel-Erklärung anzuzeigen, wenn man über eine bestimmte Zelle mit einer Formel fährt, sind die Schritte
## Ladeoptionen festlegen.
zum Beispiel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Aktions-URL für showFormulaExplain festlegen.
zum Beispiel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Wenn der Benutzer die Maus über eine Zelle mit einer Formel bewegt, wird die Aktion der Anzeige der Formel-Erklärung automatisch vom Tabellenkalkulationsprogramm ausgelöst 


## Implementieren Sie die Anzeige der Formel-Erklärung serverseitig.
zum Beispiel:
```python
# The logic for formula explanation here can be implemented through a third-party library or custom logic.
# Implement your logic to get the detail explanation for the formula
def get_formula_explain(formula, locale):  
# replace your logic here     
    return text  

@app.route('/GridJs2/FormulaExplain', methods=['POST'])  
def formula_explain():  
    formula = request.form.get('v')  
    locale = request.form.get('locale')  
# here the formula is the formula in the cell ,etc "=SUM(B1:B10)"
# check if the formula is null or empty  
    if not formula:  
        return jsonify({  
            'Success': False,  
            'v': ''  
        }), 200  

    formula_explain = get_formula_explain(formula, locale)  

    return jsonify({  
        'Success': True,  
        'v': formula_explain  
    }), 200  
```
![todo:der Bildschirm der Formel-Erklärung](gridjs_show_formula_explanation.png)




