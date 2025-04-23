---
title: показать объяснение формулы для GridJs  
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Эта статья описывает, как показывать объяснение формулы для GridJs.
keywords: GridJs, формула, объяснение формулы, показать объяснение формулы, интерпретатор формулы
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# Для отображения объяснения формулы при наведении на конкретную ячейку, содержащую формулу, шаги следующие
## Установить параметры загрузки.
например:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Установить URL действия для showFormulaExplain.
например:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
При перемещении мыши по ячейке с формулой, автоматическое срабатывание отображения объяснения формулы осуществляется приложением электронной таблицы. 

## Реализовать API отображения объяснения формулы в контроллере на серверной стороне.
например:
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
![поддержка: экран отображения объяснения формулы](gridjs_show_formula_explanation.png)




