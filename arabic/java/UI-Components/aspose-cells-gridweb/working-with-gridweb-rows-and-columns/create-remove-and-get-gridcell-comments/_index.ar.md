---
title: إنشاء إزالة والحصول على تعليقات GridCell
type: docs
weight: 10
url: /ar/java/create-remove-and-get-gridcell-comments/
---
##  **سيناريوهات الاستخدام المحتملة**
يشرح المقال التالي كيفية إنشاء تعليقات GridCell وإزالتها والحصول عليها داخل ورقة عمل GridWeb. تجدر الإشارة إلى أن GridWeb يعرض التعليق كتلميح أداة مثل MS-Excel عند تحريك الماوس فوق الخلية كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
##  **قم بإنشاء كائن تعليق داخل Cell**
الرجاء استخدام أسلوب GridCell.CreateComment لإنشاء كائن تعليق داخل الخلية. يقوم نموذج التعليمات البرمجية التالي بإنشاء تعليق نموذجي في الخلية B4 من ورقة العمل الأولى لـ GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
##  **إزالة كائن التعليق من Cell**
الرجاء استخدام الأسلوب GridCell.RemoveComment لإزالة كائن التعليق من الخلية. يقوم نموذج التعليمات البرمجية التالي بإزالة تعليق الخلية B4 داخل ورقة العمل الأولى لـ GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
##  **احصل على كائن التعليق من Cell**
الرجاء استخدام طريقة GridCell.GetComment() للحصول على كائن التعليق من الخلية. يحصل نموذج التعليمات البرمجية التالي على كائن التعليق من الخلية B4 ثم يصل إلى خصائصه المتنوعة مثل المؤلف والملاحظة والرؤية وما إلى ذلك.

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




