---
title: GridJsの計算式の解説表示  
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: この記事は、GridJsで計算式の解説表示を行う方法について説明しています。
keywords: GridJs,計算式,計算式解説,計算式表示,フォーミュラインタープリタ
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# 計算式を含むセルにカーソルを合わせたときに計算式の解説を表示する手順は次のとおりです
## ロードオプションを設定する。
たとえば：
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## showFormulaExplain用のアクションURLを設定する。
たとえば：
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
ユーザーが計算式を含むセルにマウスを移動させると、計算式の解説表示の動作はスプレッドシートアプリケーションによって自動的にトリガーされます 


## サーバー側に数式解説表示を実装します。
たとえば：
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
![todo:show式の画面](gridjs_show_formula_explanation.png)




