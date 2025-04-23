---
title: проверка синтаксиса и автозамена ошибок для GridJs  
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: В этой статье описывается, как добавить проверку синтаксиса и автозамену ошибок для GridJs.
keywords: GridJs,проверка синтаксиса,автозамена ошибок,синтаксис,ошибка,Грамматическая проверка,Грамматика
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
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

## Реализация API для проверки синтаксиса и корректировки орфографии в контроллере на серверной стороне.
например:
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

Вы можете найти больше на нашей демонстрационной странице github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



