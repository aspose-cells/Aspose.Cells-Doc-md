---
title: проверка синтаксиса и автозамена ошибок для GridJs  
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: В этой статье описывается, как добавить проверку синтаксиса и автозамену ошибок для GridJs.
keywords: GridJs,проверка синтаксиса,автозамена ошибок,синтаксис,ошибка,Грамматическая проверка,Грамматика
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# Для проверки синтаксиса и исправления орфографии пользовательского ввода, шаги следующие
## Установить параметры загрузки.
например:
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
## Установить адрес URL для действия проверки синтаксиса и исправления орфографии.
например:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
После ввода текста пользователем в ячейке, действие проверки синтаксиса будет автоматически запущено приложением электронной таблицы. 

## Реализовать API действия проверки синтаксиса и исправления орфографии в контроллере на серверной стороне.
например:
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





