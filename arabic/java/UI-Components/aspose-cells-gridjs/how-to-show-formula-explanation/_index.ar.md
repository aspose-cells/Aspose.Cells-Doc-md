---
title: عرض شرح الصيغة لـ GridJs  
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: تصف هذه المقالة كيفية عرض شرح الصيغة لـ GridJs.
keywords: GridJs،صيغة،شرح الصيغة،عرض شرح الصيغة،مفسر الصيغة
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# لعرض شرح الصيغة عند المرور فوق خلية معينة تحتوي على صيغة ، الخطوات هي
## تعيين خيارات التحميل.
على سبيل المثال:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## تعيين عنوان URL للإجراء لعرض شرح الصيغة.
على سبيل المثال:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
عندما ينقل المستخدم الماوس فوق خلية تحتوي على صيغة، سيتم تفعيل عرض شرح الصيغة تلقائيًا بواسطة تطبيق جدول البيانات 

## تنفيذ API عرض شرح الصيغة في وحدة التحكم على جانب الخادم.
على سبيل المثال:
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
![todo:شاشة عرض شرح الصيغة](gridjs_show_formula_explanation.png)




