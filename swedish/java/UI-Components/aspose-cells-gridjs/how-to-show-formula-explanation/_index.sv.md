---
title: visa formel förklaring för GridJs  
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Den här artikeln beskriver hur man visar formelförklaring för GridJs.
keywords: GridJs, formel, formelförklaring, visa formelförklaring, formel tolk
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# För att visa formelförklaring vid hovring över en specifik cell som innehåller en formel, är stegen
## Sätt laddningsalternativ.
till exempel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Sätt action URL för showFormulaExplain.
till exempel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
När användaren för musen över en cell som innehåller en formel, kommer åtgärden för att visa formelförklaring att aktiveras automatiskt av kalkylarksapplikationen 

## Implementera API för att visa formelförklaring i kontrollern i serversidan.
till exempel:
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
![todo: skärmen för att visa formelförklaring](gridjs_show_formula_explanation.png)




