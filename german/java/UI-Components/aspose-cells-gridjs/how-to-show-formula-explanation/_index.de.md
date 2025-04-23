---
title: Formel Erklärung für GridJs anzeigen  
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Dieser Artikel beschreibt, wie man die Formel Erklärung für GridJs anzeigt.
keywords: GridJs,Formel,Formel Erklärung,Formel Erklärung anzeigen,Formel Interpreter
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# Um die Formel-Erklärung anzuzeigen, wenn man über eine bestimmte Zelle mit einer Formel fährt, sind die Schritte
## Ladeoptionen festlegen.
zum Beispiel:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Aktions-URL für showFormulaExplain festlegen.
zum Beispiel:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Wenn der Benutzer die Maus über eine Zelle mit einer Formel bewegt, wird die Aktion der Anzeige der Formel-Erklärung automatisch vom Tabellenkalkulationsprogramm ausgelöst 

## Implementieren Sie die API für die Anzeige der Formelerklärung im Controller auf Serverseite.
zum Beispiel:
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
![todo:der Bildschirm der Formel-Erklärung](gridjs_show_formula_explanation.png)




