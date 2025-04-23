---
title: 显示GridJs的公式说明  
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: 本文介绍了如何为GridJs显示公式说明。
keywords: GridJs,公式,公式说明,显示公式说明,公式解释器
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
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
![待办：显示公式说明的屏幕](gridjs_show_formula_explanation.png)




