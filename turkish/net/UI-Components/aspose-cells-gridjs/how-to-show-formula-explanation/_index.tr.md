---
title: GridJs için formül açıklaması göster  
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Bu makale, GridJs için formül açıklamasının nasıl gösterileceğini anlatmaktadır.
keywords: GridJs,formül,formül açıklaması,göster formül açıklaması,formül yorumlayıcı
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# Formül içeren belirli bir hücrenin üzerine gelindiğinde formül açıklamasını göstermek için adımlar
## Yükleme seçeneklerini ayarla.
örneğin:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## showFormulaExplain için işlem URL'sini ayarla.
örneğin:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Kullanıcı bir formülü içeren hücre üzerinde fareyi hareket ettirdiğinde, formül açıklaması gösterme işlemi aktarım tablosu uygulaması tarafından otomatik olarak tetiklenecektir. 

## Sunucudaki Controller'da göster formül açıklaması eylem API'sini uygulayın.
örneğin:
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
![todo: göster formül açıklaması ekranı](gridjs_show_formula_explanation.png)




