---
title: mostrar explicación de fórmula para GridJs  
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Este artículo describe cómo mostrar la explicación de fórmula para GridJs.
keywords: GridJs,fórmula,explicación de la fórmula,mostrar explicación de fórmula,intérprete de fórmulas
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# Para mostrar la explicación de la fórmula al pasar el mouse sobre una celda específica que contiene una fórmula, los pasos son
## Configurar opciones de carga.
por ejemplo:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Establecer la URL de acción para showFormulaExplain.
por ejemplo:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Cuando el usuario pasa el mouse sobre una celda que contiene una fórmula, la acción de mostrar la explicación de la fórmula se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar la API de acción de mostrar explicación de fórmula en Controller en el lado del servidor.
por ejemplo:
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
![por hacer: la pantalla de mostrar explicación de fórmula](gridjs_show_formula_explanation.png)




