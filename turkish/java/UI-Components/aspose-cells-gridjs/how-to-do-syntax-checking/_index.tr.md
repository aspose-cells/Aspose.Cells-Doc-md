---
title: GridJs için sözdizimi denetimi ve yazım düzeltmesi  
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Bu makale, GridJs için sözdizimi denetimi ve yazım düzeltmesi eklemenin nasıl yapılacağını anlatmaktadır.
keywords: GridJs,sözdizimi denetimi,yazım düzeltmesi,sözdizimi,yazım,grafik kontrolü,Gramer Kontrolü
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Kullanıcı girişi üzerinde sözdizimi denetimi ve yazım düzeltmesi yapmak için adımlar
## Yükleme seçeneklerini ayarla.
örneğin:
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
## Sözdizimi denetimi ve yazım düzeltmesi için işlem URL'sini ayarla.
örneğin:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Kullanıcı bir hücreye metin girdikten sonra, sözdizimi denetimi işlemi otomatik olarak elektronik tablo uygulaması tarafından tetiklenir. 

## Sunucu tarafında sözdizimi denetimi ve yazım düzeltme API’sini gerçekleştir.
örneğin:
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





