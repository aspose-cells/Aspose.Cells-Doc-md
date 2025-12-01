---
title: syntax checking & spell correction for GridJs  
type: docs
weight: 250
url: /java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: This article describes how to add syntax  checking & spell correction for GridJs.
keywords: GridJs,syntax checking,spell correction,syntax,spell,Grammar Checking,Grammar
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

 
# To perform syntax checking  & spell correction on user input ,the steps are
## Set load options.
for example:
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
## Set action URL for syntax  checking & spell correction.
for example:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
After a user enters text content in a cell, the action of syntax checking wil be triggered automatically by the spreadsheet application 

## Implement syntax  checking & spell correction action API in Controller  in serverside .
for example:
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




 
