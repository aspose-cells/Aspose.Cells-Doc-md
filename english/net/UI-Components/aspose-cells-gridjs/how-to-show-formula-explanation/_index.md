---
title: Show Formula Explanation for GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: This article describes how to show formula explanation for GridJs.
keywords: GridJs,formula,formula explanation,show formula explanation,formula interpreter
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# To display formula explanation when hovering over a specific cell that contains a formula, the steps are:

## Set load options.  
For example:
```javascript
 const option = {
     ...
     // set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```

## Set action URL for showFormulaExplain.  
For example:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```

When the user moves the mouse over a cell that contains a formula, the action of displaying the formula explanation will be triggered automatically by the spreadsheet application.

## Implement show formula explanation action API in controller on the server side.  
For example:
```csharp
  [HttpPost]
 public async Task<IActionResult> FormulaExplainAsync()
 {
     string formulaText = HttpContext.Request.Form["v"];
     string locale = HttpContext.Request.Form["locale"];
     if (string.IsNullOrEmpty(formulaText))
     {
         return Ok(new
         {
             Success = false,
             v = ""
         });
     }
     // here the formulaText is the formula, e.g., "=SUM(B1:B10)"
     string correctedContent = await GetFormulaExplainAsync(formulaText, locale);

     return Ok(new
     {
         Success = true,
         v = correctedContent
     });
 }
 // you need to implement it yourself
 private async Task<string> GetFormulaExplainAsync(string formulaText, string locale)
 {   
     // your logic to get the detailed explanation for the formulaText
     string result = null;
     return result;
 }
```
![todo: the screen of show formula explanation](gridjs_show_formula_explanation.png)
