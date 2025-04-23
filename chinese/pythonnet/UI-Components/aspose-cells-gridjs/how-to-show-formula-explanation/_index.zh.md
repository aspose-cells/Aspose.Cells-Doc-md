---
title: 显示GridJs的公式说明  
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: 本文介绍了如何为GridJs显示公式说明。
keywords: GridJs,公式,公式说明,显示公式说明,公式解释器
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# 在悬停包含公式的特定单元格时显示公式说明的步骤为
## 设置加载选项。
例如：
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## 设置显示公式说明的操作URL。
例如：
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
当用户将鼠标移动到包含公式的单元格时，显示公式说明的操作将由电子表格应用程序自动触发 


## 在服务器端实现显示公式说明。
例如：
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
![待办：显示公式说明的屏幕](gridjs_show_formula_explanation.png)




