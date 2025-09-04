---
title: syntax checking & spell correction for GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: This article describes how to add syntax  checking & spell correction for GridJs.
keywords: GridJs,syntax checking,spell correction,syntax,spell,Grammar Checking,Grammar
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
---

 
# To perform syntax checking  & spell correction on user input ,the steps are
## Set load options.
for example:
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
## Set action URL for syntax  checking & spell correction.
for example:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
After a user enters text content in a cell, the action of syntax checking wil be triggered automatically by the spreadsheet application 

## Implement syntax  checking & spell correction action API in Controller in serverside.
for example:
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

You can find more in our github demo page https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html


 
