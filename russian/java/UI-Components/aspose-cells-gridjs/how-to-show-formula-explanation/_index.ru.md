---
title: показать объяснение формулы для GridJs  
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Эта статья описывает, как показывать объяснение формулы для GridJs.
keywords: GridJs, формула, объяснение формулы, показать объяснение формулы, интерпретатор формулы
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
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
![поддержка: экран отображения объяснения формулы](gridjs_show_formula_explanation.png)




