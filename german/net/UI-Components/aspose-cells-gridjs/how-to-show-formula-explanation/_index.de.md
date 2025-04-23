---
title: Formel Erklärung für GridJs anzeigen  
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Dieser Artikel beschreibt, wie man die Formel Erklärung für GridJs anzeigt.
keywords: GridJs,Formel,Formel Erklärung,Formel Erklärung anzeigen,Formel Interpreter
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# Um die Formel-Erklärung anzuzeigen, wenn man über eine bestimmte Zelle mit einer Formel fährt, sind die Schritte
## Ladeoptionen festlegen.
zum Beispiel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Aktions-URL für showFormulaExplain festlegen.
zum Beispiel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Wenn der Benutzer die Maus über eine Zelle mit einer Formel bewegt, wird die Aktion der Anzeige der Formel-Erklärung automatisch vom Tabellenkalkulationsprogramm ausgelöst 

## Implementieren Sie die API für die Anzeige der Formelerklärung im Controller auf Serverseite.
zum Beispiel:
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
![todo:der Bildschirm der Formel-Erklärung](gridjs_show_formula_explanation.png)




