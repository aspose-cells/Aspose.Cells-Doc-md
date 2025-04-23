---
title: GridJs için formül açıklaması göster  
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Bu makale, GridJs için formül açıklamasının nasıl gösterileceğini anlatmaktadır.
keywords: GridJs,formül,formül açıklaması,göster formül açıklaması,formül yorumlayıcı
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Formül içeren belirli bir hücrenin üzerine gelindiğinde formül açıklamasını göstermek için adımlar
## Yükleme seçeneklerini ayarla.
örneğin:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## showFormulaExplain için işlem URL'sini ayarla.
örneğin:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Kullanıcı bir formülü içeren hücre üzerinde fareyi hareket ettirdiğinde, formül açıklaması gösterme işlemi aktarım tablosu uygulaması tarafından otomatik olarak tetiklenecektir. 


## Sunucu tarafında formül açıklamasını gösterme işlemini uygula.
örneğin:
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
![todo: göster formül açıklaması ekranı](gridjs_show_formula_explanation.png)




