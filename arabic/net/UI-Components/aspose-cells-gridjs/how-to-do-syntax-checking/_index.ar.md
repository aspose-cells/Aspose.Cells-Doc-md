---
title: التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs  
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: تصف هذه المقالة كيفية إضافة التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs.
keywords: GridJs،التحقق من بناء الجمل،تصحيح الإملاء،بناء الجمل،إملاء،فحص القواعد،تدقيق النحو
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
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

## تطبيق التحقق من الصياغة API وتصحيح الإملاء في وحدة التحكم في الخادم.
على سبيل المثال:
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

يمكنك العثور على المزيد في صفحة العرض التوضيحي لدينا على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



