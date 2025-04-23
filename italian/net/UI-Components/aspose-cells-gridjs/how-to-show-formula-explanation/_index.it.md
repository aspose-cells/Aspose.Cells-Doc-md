---
title: mostra la spiegazione della formula per GridJs  
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Questo articolo descrive come mostrare la spiegazione della formula per GridJs.
keywords: GridJs, formula, spiegazione della formula, mostra spiegazione della formula, interprete di formule
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# Per mostrare la spiegazione della formula al passaggio del mouse su una cella specifica che contiene una formula, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Imposta l'URL dell'azione per mostrareSpiegazioneFormula.
ad esempio:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Quando l'utente sposta il mouse sopra una cella che contiene una formula, l'azione di visualizzazione della spiegazione della formula verrà attivata automaticamente dall'applicazione del foglio di calcolo 

## Implementa l'API di visualizzazione della spiegazione della formula nel Controller lato server.
ad esempio:
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
![todo:la schermata di mostrare la spiegazione della formula](gridjs_show_formula_explanation.png)




