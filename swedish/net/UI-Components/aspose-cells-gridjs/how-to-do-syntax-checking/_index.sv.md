---
title: Syntaxkontroll & stavningskorrigering för GridJs  
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Den här artikeln beskriver hur man lägger till syntaxkontroll & stavningskorrigering för GridJs.
keywords: GridJs, syntaxkontroll, stavningskorrigering, syntax, stavning, grammatikgranskning, grammatik
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
---


# För att utföra syntaxkontroll & stavningskorrigering på användarens inmatning, är stegen
## Sätt laddningsalternativ.
till exempel:
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
## Sätt action URL för syntaxkontroll & stavningskorrigering.
till exempel:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Efter att en användare skriver in textinnehåll i en cell, kommer syntaxkontrollen att utlösas automatiskt av kalkylplatsapplikationen 

## Implementera syntaxkontroll & stavningskorrigerings-API i Controller på serversidan.
till exempel:
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

Du kan hitta mer på vår github demosida https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



