---
title: controllo della sintassi & correzione ortografica per GridJs  
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Questo articolo descrive come aggiungere controllo della sintassi & correzione ortografica a GridJs.
keywords: GridJs,controllo della sintassi,correzione ortografica,sintassi,ortografia,Controllo grammaticale,Controllo grammaticale
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
---


# Per eseguire il controllo della sintassi e la correzione ortografica sull'input dell'utente, i passaggi sono
## Imposta le opzioni di caricamento.
ad esempio:
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
## Imposta l'URL dell'azione per il controllo della sintassi e la correzione ortografica.
ad esempio:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Dopo che un utente inserisce il contenuto di testo in una cella, l'azione di controllo della sintassi verrà attivata automaticamente dall'applicazione del foglio di calcolo 

## Implementa l'API di verifica della sintassi e correzione ortografica nel Controller lato server.
ad esempio:
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

Puoi trovare altro sulla nostra pagina demo di github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



