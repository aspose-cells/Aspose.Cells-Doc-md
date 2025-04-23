---
title: visa formel förklaring för GridJs  
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Den här artikeln beskriver hur man visar formelförklaring för GridJs.
keywords: GridJs, formel, formelförklaring, visa formelförklaring, formel tolk
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# För att visa formelförklaring vid hovring över en specifik cell som innehåller en formel, är stegen
## Sätt laddningsalternativ.
till exempel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Sätt action URL för showFormulaExplain.
till exempel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
När användaren för musen över en cell som innehåller en formel, kommer åtgärden för att visa formelförklaring att aktiveras automatiskt av kalkylarksapplikationen 

## Implementera API för att visa formelförklaring i kontrollern i serversidan.
till exempel:
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
![todo: skärmen för att visa formelförklaring](gridjs_show_formula_explanation.png)




