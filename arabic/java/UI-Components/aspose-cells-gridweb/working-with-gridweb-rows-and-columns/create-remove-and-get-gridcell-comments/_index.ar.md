---
title: إنشاء إزالة والحصول على تعليقات GridCell
type: docs
weight: 10
url: /ar/java/create-remove-and-get-gridcell-comments/
---
## **سيناريوهات الاستخدام الممكنة**
تشرح المقالة التالية كيفية إنشاء وإزالة والحصول على تعليقات GridCell داخل ورقة عمل GridWeb. من الجدير بالذكر أن GridWeb يعرض التعليق على أنه تلميح أداة مثل MS-Excel عند تحريك الماوس فوق الخلية كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](create-remove-and-get-gridcell-comments_1.png)
## **تكوين كائن تعليق داخل Cell**
الرجاء استخدام طريقة GridCell.CreateComment لإنشاء كائن تعليق داخل الخلية. ينشئ نموذج التعليمات البرمجية التالي تعليق نموذج في الخلية B4 من ورقة العمل الأولى من GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **إزالة كائن التعليق من Cell**
الرجاء استخدام طريقة GridCell.RemoveComment لإزالة كائن تعليق من الخلية. يزيل نموذج التعليمات البرمجية التالي تعليق الخلية B4 داخل ورقة العمل الأولى من GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **احصل على كائن تعليق من Cell**
الرجاء استخدام طريقة GridCell.GetComment () للحصول على كائن تعليق من الخلية. يحصل نموذج التعليمات البرمجية التالي على كائن التعليق من الخلية B4 ثم يصل إلى خصائصه المختلفة مثل المؤلف والملاحظة والرؤية وما إلى ذلك.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




