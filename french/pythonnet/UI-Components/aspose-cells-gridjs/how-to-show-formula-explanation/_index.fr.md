---
title: afficher l explication de la formule pour GridJs  
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Cet article décrit comment afficher l explication de la formule pour GridJs.
keywords: GridJs,formule,explication de formule,afficher l explication de la formule,interprète de formule
aliases:
  - /python-net/aspose-cells-gridjs/show-formula-explanation/
  - /python-net/aspose-cells-gridjs/display-formula-explanation/
  - /python-net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-explanation/
  - /python-net/aspose-cells-gridjs/formula-interpreter/
---


# Pour afficher l'explication de la formule lors du survol d'une cellule spécifique contenant une formule, les étapes sont
## Définir les options de chargement.
par exemple :
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Définir l'URL d'action pour showFormulaExplain.
par exemple :
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Lorsque l'utilisateur déplace la souris sur une cellule contenant une formule, l'action d'affichage de l'explication de la formule sera déclenchée automatiquement par l'application de feuille de calcul 


## Implémenter l'affichage de l'explication de la formule côté serveur.
par exemple :
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
![todo: l'écran de l'affichage de l'explication de la formule](gridjs_show_formula_explanation.png)




