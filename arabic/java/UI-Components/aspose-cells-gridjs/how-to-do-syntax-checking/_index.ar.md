---
title: التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs  
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: تصف هذه المقالة كيفية إضافة التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs.
keywords: GridJs،التحقق من بناء الجمل،تصحيح الإملاء،بناء الجمل،إملاء،فحص القواعد،تدقيق النحو
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# لتنفيذ فحص الصياغة وتصحيح الإملاء على إدخال المستخدم ، الخطوات هي
## تعيين خيارات التحميل.
على سبيل المثال:
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
## تعيين عنوان URL للإجراء لفحص الصياغة وتصحيح الإملاء.
على سبيل المثال:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
بعد أن يدخل المستخدم محتوى نصيًا في خلية ، سيتم تفعيل عملية فحص الصياغة تلقائيًا بواسطة تطبيق جدول البيانات 

## تنفيذ API فحص الصيغة وتصحيح الإملاء في وحدة التحكم على جانب الخادم.
على سبيل المثال:
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





