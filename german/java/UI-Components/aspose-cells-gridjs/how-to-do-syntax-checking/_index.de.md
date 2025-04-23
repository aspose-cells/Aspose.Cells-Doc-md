---
title: Syntaxprüfung & Rechtschreibkorrektur für GridJs  
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Dieser Artikel beschreibt, wie man Syntaxprüfung & Rechtschreibkorrektur für GridJs hinzufügt.
keywords: GridJs, Syntaxprüfung, Rechtschreibkorrektur, Syntax, Rechtschreibung, Grammatikprüfung, Grammatik
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Um Syntaxprüfung & Rechtschreibkorrektur bei Benutzereingaben durchzuführen, sind die Schritte
## Ladeoptionen festlegen.
zum Beispiel:
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
## Aktions-URL für Syntaxprüfung & Rechtschreibkorrektur festlegen.
zum Beispiel:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Nachdem ein Benutzer Textinhalt in eine Zelle eingegeben hat, wird die Syntaxprüfung automatisch vom Tabellenkalkulationsprogramm ausgelöst 

## Implementieren Sie API für Syntaxprüfung & Rechtschreibkorrektur in den Controller auf Serverseite.
zum Beispiel:
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





