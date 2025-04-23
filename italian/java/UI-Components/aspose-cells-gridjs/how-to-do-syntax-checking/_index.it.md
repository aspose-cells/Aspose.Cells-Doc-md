---
title: controllo della sintassi & correzione ortografica per GridJs  
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Questo articolo descrive come aggiungere controllo della sintassi & correzione ortografica a GridJs.
keywords: GridJs,controllo della sintassi,correzione ortografica,sintassi,ortografia,Controllo grammaticale,Controllo grammaticale
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Per eseguire il controllo della sintassi e la correzione ortografica sull'input dell'utente, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
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
## Imposta l'URL dell'azione per il controllo della sintassi e la correzione ortografica.
ad esempio:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Dopo che un utente inserisce il contenuto di testo in una cella, l'azione di controllo della sintassi verrà attivata automaticamente dall'applicazione del foglio di calcolo 

## Implementa l'API di controllo azione per verifica sintassi e correzione ortografica lato server.
ad esempio:
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





