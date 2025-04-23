---
title: afficher l explication de la formule pour GridJs  
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Cet article décrit comment afficher l explication de la formule pour GridJs.
keywords: GridJs,formule,explication de formule,afficher l explication de la formule,interprète de formule
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
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

## Implémenter l'API d'affichage de l'explication de la formule dans le Contrôleur côté serveur.
par exemple :
```C#
  [HttpPost]
 public async Task<IActionResult> FormulaExplainAsync()
 {
     String formulaText = HttpContext.Request.Form["v"];
     String locale = HttpContext.Request.Form["locale"];
     if (string.IsNullOrEmpty(formulaText))
     {
         return Ok(new
         {
             Success = false,
             v = ""
         });
     }
     //here the formulaText is the formula ,etc "=SUM(B1:B10)"
     string correctedContent = await GetFormulaExplainAsync(formulaText, locale);

     return Ok(new
     {
         Success = true,
         v = correctedContent
     });
 }
 //you need to implement it youself
 private async Task<string> GetFormulaExplainAsync(string formulaText,string locale)
 {   String result=null;
     //your logic to get the detail explanation for the formulaText
     return result;
 }
```
![todo: l'écran de l'affichage de l'explication de la formule](gridjs_show_formula_explanation.png)




