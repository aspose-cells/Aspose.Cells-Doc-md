---
title: mostra la spiegazione della formula per GridJs  
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Questo articolo descrive come mostrare la spiegazione della formula per GridJs.
keywords: GridJs, formula, spiegazione della formula, mostra spiegazione della formula, interprete di formule
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# Per mostrare la spiegazione della formula al passaggio del mouse su una cella specifica che contiene una formula, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Imposta l'URL dell'azione per mostrareSpiegazioneFormula.
ad esempio:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Quando l'utente sposta il mouse sopra una cella che contiene una formula, l'azione di visualizzazione della spiegazione della formula verrà attivata automaticamente dall'applicazione del foglio di calcolo 

## Implementa l'API di visualizzazione della spiegazione della formula nel Controller lato server.
ad esempio:
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
![todo:la schermata di mostrare la spiegazione della formula](gridjs_show_formula_explanation.png)




