---
title: visa formel förklaring för GridJs  
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Den här artikeln beskriver hur man visar formelförklaring för GridJs.
keywords: GridJs, formel, formelförklaring, visa formelförklaring, formel tolk
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# För att visa formelförklaring vid hovring över en specifik cell som innehåller en formel, är stegen
## Sätt laddningsalternativ.
till exempel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Sätt action URL för showFormulaExplain.
till exempel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
När användaren för musen över en cell som innehåller en formel, kommer åtgärden för att visa formelförklaring att aktiveras automatiskt av kalkylarksapplikationen 


## Implementera show formelförklaring på serversidan.
till exempel:
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
![todo: skärmen för att visa formelförklaring](gridjs_show_formula_explanation.png)




