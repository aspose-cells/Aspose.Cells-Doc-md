---
title: comprobación de sintaxis y corrección ortográfica para GridJs  
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Este artículo describe cómo agregar comprobación de sintaxis y corrección ortográfica para GridJs.
keywords: GridJs,verificación de sintaxis,corrección ortográfica,sintaxis,ortografía,Verificación gramatical,Gramática
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Para realizar la verificación de sintaxis y corrección ortográfica en la entrada del usuario, los pasos son
## Configurar opciones de carga.
por ejemplo:
```javascript
 const option = {
     ...
     //set showCheckSyntaxButton to true
    showCheckSyntaxButton:true,
    //set checkSyntax to true
    checkSyntax:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Establecer URL de acción para verificación de sintaxis y corrección ortográfica.
por ejemplo:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Después de que un usuario ingresa contenido de texto en una celda, la acción de verificación de sintaxis se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar API de acción de verificación de sintaxis y corrección ortográfica en el Controlador en el servidor.
por ejemplo:
```java
    @PostMapping("/CheckSyntax")  
    public ResponseEntity<?> checkSyntax(  
            @RequestParam(name = "v", required = true) String textInput,  
            @RequestParam(name = "locale", required = false) String locale) {  

        // Check if the input text is null or empty  
        if (textInput == null || textInput.isEmpty()) {  
            // Return a response indicating failure and an empty string for the corrected content  
            return ResponseEntity.ok(Map.of("success", false, "v", ""));  
        }  

        // Call the syntax correction logic, which could be a third-party library or custom code  
        // This is a placeholder method that should be replaced with actual logic  
        String correctedContent = correctSyntax(textInput, locale);  

        // Return a response indicating success and the corrected content  
        return ResponseEntity.ok(Map.of("success", true, "v", correctedContent));  
    }  

    // Placeholder method for syntax correction logic  
    // This should be replaced with the actual implementation  
    private String correctSyntax(String text, String locale) {  
        // Implement your syntax correction logic here  
        // For demonstration, simply returning the input text  
        return text; // Replace this with the actual syntax correction  
    }  
```





