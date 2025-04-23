---
title: GridJsの構文チェックとスペル修正のためのシンタックスチェッキング＆スペルコレクション  
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-do-syntax-checking/
description: この記事は、GridJsに構文チェックとスペル修正を追加する方法について説明しています。
keywords: GridJs,構文チェック,スペル修正,構文,スペル,文法チェッカー,文法
aliases:
  - /java/aspose-cells-gridjs/syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /java/aspose-cells-gridjs/how-to-add-spell-correction/
  - /java/aspose-cells-gridjs/spell-correction/
---


# ユーザー入力に対して構文チェック＆スペル修正を行う手順は次のとおりです
## ロードオプションを設定する。
たとえば：
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
## 構文チェック＆スペル修正用のアクションURLを設定する。
たとえば：
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
ユーザーがセルにテキスト内容を入力した後、構文チェックの動作はスプレッドシートアプリケーションによって自動的にトリガーされます。 

## サーバーサイドのコントローラーに構文チェックとスペル補正アクションAPIを実装します。
たとえば：
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





