---
title: mostrar explicación de fórmula para GridJs  
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Este artículo describe cómo mostrar la explicación de fórmula para GridJs.
keywords: GridJs,fórmula,explicación de la fórmula,mostrar explicación de fórmula,intérprete de fórmulas
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Para mostrar la explicación de la fórmula al pasar el mouse sobre una celda específica que contiene una fórmula, los pasos son
## Configurar opciones de carga.
por ejemplo:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Establecer la URL de acción para showFormulaExplain.
por ejemplo:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Cuando el usuario pasa el mouse sobre una celda que contiene una fórmula, la acción de mostrar la explicación de la fórmula se activará automáticamente por la aplicación de hoja de cálculo. 


## Implementar  mostrar  explicación de fórmula en servidor.
por ejemplo:
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
![por hacer: la pantalla de mostrar explicación de fórmula](gridjs_show_formula_explanation.png)




