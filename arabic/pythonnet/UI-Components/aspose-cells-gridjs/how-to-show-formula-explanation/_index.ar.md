---
title: عرض شرح الصيغة لـ GridJs  
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: تصف هذه المقالة كيفية عرض شرح الصيغة لـ GridJs.
keywords: GridJs،صيغة،شرح الصيغة،عرض شرح الصيغة،مفسر الصيغة
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# لعرض شرح الصيغة عند المرور فوق خلية معينة تحتوي على صيغة ، الخطوات هي
## تعيين خيارات التحميل.
على سبيل المثال:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## تعيين عنوان URL للإجراء لعرض شرح الصيغة.
على سبيل المثال:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
عندما ينقل المستخدم الماوس فوق خلية تحتوي على صيغة، سيتم تفعيل عرض شرح الصيغة تلقائيًا بواسطة تطبيق جدول البيانات 


## تنفيذ عرض شرح الصيغة في جانب الخادم.
على سبيل المثال:
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
![todo:شاشة عرض شرح الصيغة](gridjs_show_formula_explanation.png)




