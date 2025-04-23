---
title: Syntaxprüfung & Rechtschreibkorrektur für GridJs  
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Dieser Artikel beschreibt, wie man Syntaxprüfung & Rechtschreibkorrektur für GridJs hinzufügt.
keywords: GridJs, Syntaxprüfung, Rechtschreibkorrektur, Syntax, Rechtschreibung, Grammatikprüfung, Grammatik
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
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

## Implementieren Sie die API für Syntaxprüfung & Rechtschreibkorrektur im Controller auf Serverseite.
zum Beispiel:
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

Weitere Informationen finden Sie auf unserer Github-Demo-Seite https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



