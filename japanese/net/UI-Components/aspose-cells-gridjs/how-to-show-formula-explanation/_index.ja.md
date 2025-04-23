---
title: GridJsの計算式の解説表示  
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: この記事は、GridJsで計算式の解説表示を行う方法について説明しています。
keywords: GridJs,計算式,計算式解説,計算式表示,フォーミュラインタープリタ
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# 計算式を含むセルにカーソルを合わせたときに計算式の解説を表示する手順は次のとおりです
## ロードオプションを設定する。
たとえば：
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## showFormulaExplain用のアクションURLを設定する。
たとえば：
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
ユーザーが計算式を含むセルにマウスを移動させると、計算式の解説表示の動作はスプレッドシートアプリケーションによって自動的にトリガーされます 

## コントローラーのサーバーサイドでのshow式の説明アクションAPIの実装。
たとえば：
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
![todo:show式の画面](gridjs_show_formula_explanation.png)




