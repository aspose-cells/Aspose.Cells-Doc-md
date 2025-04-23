---
title: GridJs için formül açıklaması göster  
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Bu makale, GridJs için formül açıklamasının nasıl gösterileceğini anlatmaktadır.
keywords: GridJs,formül,formül açıklaması,göster formül açıklaması,formül yorumlayıcı
aliases:
  - /java/aspose-cells-gridjs/show-formula-explanation/
  - /java/aspose-cells-gridjs/display-formula-explanation/
  - /java/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /java/aspose-cells-gridjs/formula-explanation/
  - /java/aspose-cells-gridjs/formula-interpreter/
---


# Formül içeren belirli bir hücrenin üzerine gelindiğinde formül açıklamasını göstermek için adımlar
## Yükleme seçeneklerini ayarla.
örneğin:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## showFormulaExplain için işlem URL'sini ayarla.
örneğin:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Kullanıcı bir formülü içeren hücre üzerinde fareyi hareket ettirdiğinde, formül açıklaması gösterme işlemi aktarım tablosu uygulaması tarafından otomatik olarak tetiklenecektir. 

## Sunucudaki Controller'da göster formül açıklaması eylem API'sini uygulayın.
örneğin:
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
![todo: göster formül açıklaması ekranı](gridjs_show_formula_explanation.png)




