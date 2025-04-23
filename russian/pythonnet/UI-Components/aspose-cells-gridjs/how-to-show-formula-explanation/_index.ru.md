---
title: показать объяснение формулы для GridJs  
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Эта статья описывает, как показывать объяснение формулы для GridJs.
keywords: GridJs, формула, объяснение формулы, показать объяснение формулы, интерпретатор формулы
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Для отображения объяснения формулы при наведении на конкретную ячейку, содержащую формулу, шаги следующие
## Установить параметры загрузки.
например:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Установить URL действия для showFormulaExplain.
например:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
При перемещении мыши по ячейке с формулой, автоматическое срабатывание отображения объяснения формулы осуществляется приложением электронной таблицы. 


## Реализовать отображение объяснения формулы на серверной стороне.
например:
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
![поддержка: экран отображения объяснения формулы](gridjs_show_formula_explanation.png)




