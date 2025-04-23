---
title: عرض شرح الصيغة لـ GridJs  
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: تصف هذه المقالة كيفية عرض شرح الصيغة لـ GridJs.
keywords: GridJs،صيغة،شرح الصيغة،عرض شرح الصيغة،مفسر الصيغة
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# لعرض شرح الصيغة عند المرور فوق خلية معينة تحتوي على صيغة ، الخطوات هي
## تعيين خيارات التحميل.
على سبيل المثال:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## تعيين عنوان URL للإجراء لعرض شرح الصيغة.
على سبيل المثال:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
عندما ينقل المستخدم الماوس فوق خلية تحتوي على صيغة، سيتم تفعيل عرض شرح الصيغة تلقائيًا بواسطة تطبيق جدول البيانات 

## تنفيذ API عرض شرح الصيغة في وحدة التحكم على جانب الخادم.
على سبيل المثال:
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
![todo:شاشة عرض شرح الصيغة](gridjs_show_formula_explanation.png)




