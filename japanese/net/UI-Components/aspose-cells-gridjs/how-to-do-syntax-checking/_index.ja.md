---
title: GridJsの構文チェックとスペル修正のためのシンタックスチェッキング＆スペルコレクション  
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: この記事は、GridJsに構文チェックとスペル修正を追加する方法について説明しています。
keywords: GridJs,構文チェック,スペル修正,構文,スペル,文法チェッカー,文法
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
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

## サーバーサイドのコントローラーで構文チェック＆スペル修正APIを実装する。
たとえば：
```C#
 [HttpPost]
 public async Task<IActionResult> CheckSyntaxAsync()
 {   //the input text content 
     String text = HttpContext.Request.Form["v"];
     /* the locale info : support multiple language for menus ,the locale can be:
	                        en, zh, es, pt, de, ru, nl, 
	                   for  English,Chinese,Spanish,Portuguese,German,Russian,Dutch
			        ar, fr,id,it,ja
                           for  Arabic,French,Indonesian,Italian,Japanese
			        ko,th,tr,vi,cht
                           for  Korean,Thai,Turkey,Vietnamese,Traditional Chinese    
			   */
     String locale = HttpContext.Request.Form["locale"];
     if (string.IsNullOrEmpty(text))
     {
         return Ok(new
         {
             Success = false,
             v = ""
         });
     }

     // The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
     string correctedContent = await CorrectSyntaxAsync(text, locale);

     return Ok(new
     {
         Success = true,
         v = correctedContent
     });
 }
 //you need to implement it youself
 private async Task<string> CorrectSyntaxAsync(string text,string locale)
 {   String result=null;
     //your logic to do syntax checking
     return result;
 }
```

GitHubのデモページで詳細をご覧いただけます：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



