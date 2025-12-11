---
title: Show Formula Explanation for GridJs  
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: This article describes how to show formula explanation for GridJs.
keywords: GridJs, formula, formula explanation, show formula explanation, formula interpreter
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# To display formula explanation when hovering over a specific cell that contains a formula, the steps are

## Set load options.

For example:

```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```

## Set action URL for showFormulaExplain.

For example:

```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```

When the user moves the mouse over a cell that contains a formula, the action of displaying the formula explanation will be triggered automatically by the spreadsheet application.

## Implement show formula explanation on the server side.

For example:

```python
# The logic for formula explanation here can be implemented through a third‑party library or custom logic.
# Implement your logic to get the detailed explanation for the formula
def get_formula_explain(formula, locale):  
    # Replace your logic here     
    return text  
  
@app.route('/GridJs2/FormulaExplain', methods=['POST'])  
def formula_explain():  
    formula = request.form.get('v')  
    locale = request.form.get('locale')  
    # Here the formula is the formula in the cell, e.g., "=SUM(B1:B10)"
    # Check if the formula is null or empty  
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

![TODO: the screen of showing formula explanation](gridjs_show_formula_explanation.png)
