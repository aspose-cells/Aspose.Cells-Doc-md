---
title: afficher l explication de la formule pour GridJs  
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Cet article décrit comment afficher l explication de la formule pour GridJs.
keywords: GridJs,formule,explication de formule,afficher l explication de la formule,interprète de formule
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# Pour afficher l'explication de la formule lors du survol d'une cellule spécifique contenant une formule, les étapes sont
## Définir les options de chargement.
par exemple :
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Définir l'URL d'action pour showFormulaExplain.
par exemple :
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Lorsque l'utilisateur déplace la souris sur une cellule contenant une formule, l'action d'affichage de l'explication de la formule sera déclenchée automatiquement par l'application de feuille de calcul 

## Implémenter l'API d'affichage de l'explication de la formule dans le Contrôleur côté serveur.
par exemple :
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
![todo: l'écran de l'affichage de l'explication de la formule](gridjs_show_formula_explanation.png)




