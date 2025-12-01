---
title: show formula explanation for GridJs  
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

 
# To display formula explanation when hovering over a specific cell that contains a formula ,the steps are
## Set load options.
for example:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Set action URL for showFormulaExplain.
for example:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
When the user moves the mouse over a cell that contains a formula, the action of display formula explanation will be triggered automatically by the spreadsheet application 

## Implement show  formula explanation action API in Controller in serverside.
for example:
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
![todo:the screen of show formula explanation](gridjs_show_formula_explanation.png)



 
