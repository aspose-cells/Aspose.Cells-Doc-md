---
title: 显示GridJs的公式说明  
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: 本文介绍了如何为GridJs显示公式说明。
keywords: GridJs,公式,公式说明,显示公式说明,公式解释器
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# 在悬停包含公式的特定单元格时显示公式说明的步骤为
## 设置加载选项。
例如：
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## 设置显示公式说明的操作URL。
例如：
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
当用户将鼠标移动到包含公式的单元格时，显示公式说明的操作将由电子表格应用程序自动触发 

## 在服务器端的控制器中实现显示公式解释的API。
例如：
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
![待办：显示公式说明的屏幕](gridjs_show_formula_explanation.png)




