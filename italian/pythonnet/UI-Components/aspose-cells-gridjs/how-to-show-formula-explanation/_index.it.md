---
title: mostra la spiegazione della formula per GridJs  
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Questo articolo descrive come mostrare la spiegazione della formula per GridJs.
keywords: GridJs, formula, spiegazione della formula, mostra spiegazione della formula, interprete di formule
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Per mostrare la spiegazione della formula al passaggio del mouse su una cella specifica che contiene una formula, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Imposta l'URL dell'azione per mostrareSpiegazioneFormula.
ad esempio:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Quando l'utente sposta il mouse sopra una cella che contiene una formula, l'azione di visualizzazione della spiegazione della formula verrà attivata automaticamente dall'applicazione del foglio di calcolo 


## Implementa la visualizzazione della spiegazione della formula lato server.
ad esempio:
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
![todo:la schermata di mostrare la spiegazione della formula](gridjs_show_formula_explanation.png)




