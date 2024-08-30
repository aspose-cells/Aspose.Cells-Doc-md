---
title: show formula explanation for GridJs  
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: This article describes how to show formula explanation for GridJs.
keywords: GridJs,formula,formula explanation,show formula explanation,formula interpreter
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---

 
# To display formula explanation when hovering over a specific cell that contains a formula ,the steps are
## Set load options.
for example:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Set action URL for showFormulaExplain.
for example:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
When the user moves the mouse over a cell that contains a formula, the action of display formula explanation will be triggered automatically by the spreadsheet application 
 

## Implement  show  formula explanation  in serverside.
for example:
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
![todo:the screen of show formula explanation](gridjs_show_formula_explanation.png)



 
