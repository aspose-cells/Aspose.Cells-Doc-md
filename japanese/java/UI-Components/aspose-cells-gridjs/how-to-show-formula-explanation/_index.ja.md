---
title: GridJsの計算式の解説表示  
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: この記事は、GridJsで計算式の解説表示を行う方法について説明しています。
keywords: GridJs,計算式,計算式解説,計算式表示,フォーミュラインタープリタ
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
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
```java
 @PostMapping("/FormulaExplain")
 public ResponseEntity<?>  formulaExplain(  
            @RequestParam(name = "v", required = true) String formulaText,  
            @RequestParam(name = "locale", required = false) String locale) {  
        //here the formulaText is the formula in the cell ,etc "=SUM(B1:B10)"
        //check if the formulaText is null or empty  
        if (formulaText == null || formulaText.isEmpty()) {  
            // Return a response indicating failure and an empty string for the corrected content  
            return ResponseEntity.ok(Map.of("success", false, "v", ""));  
        }  

        // Call the syntax correction logic, which could be a third-party library or custom code  
        // This is a placeholder method that should be replaced with actual logic  
        String correctedContent = getFormulaExplain(formulaText, locale);  

        // Return a response indicating success and the corrected content  
        return ResponseEntity.ok(Map.of("success", true, "v", correctedContent));  
    }  

    // Placeholder method for formula explanation
    // This should be replaced with the actual implementation  
    private String getFormulaExplain(String formulaText, String locale) {  
        // Implement your logic to get the detail explanation for the formulaText
        // For demonstration, simply returning the input text  
        return text;  
    }  
```
![todo:show式の画面](gridjs_show_formula_explanation.png)




