---
title: Vérification de syntaxe et correction orthographique pour GridJs  
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Cet article décrit comment ajouter la vérification de syntaxe & correction orthographique pour GridJs.
keywords: GridJs, vérification de syntaxe, correction orthographique, syntaxe, orthographe, Vérification de grammaire, Grammaire
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Pour effectuer une vérification de syntaxe et une correction orthographique sur l'entrée utilisateur, les étapes sont
## Définir les options de chargement.
par exemple :
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
## Définir l'URL d'action pour la vérification de syntaxe et la correction orthographique.
par exemple :
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Après qu'un utilisateur entre du contenu textuel dans une cellule, l'action de vérification de syntaxe sera déclenchée automatiquement par l'application de feuille de calcul 

## Implémenter l'API de vérification de syntaxe et de correction orthographique dans le contrôleur côté serveur.
par exemple :
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





