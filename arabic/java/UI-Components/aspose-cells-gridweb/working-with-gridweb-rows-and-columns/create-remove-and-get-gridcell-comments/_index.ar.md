---
title: إنشاء وحذف والحصول على تعليقات خلية الجدول
type: docs
weight: 10
url: /ar/java/create-remove-and-get-gridcell-comments/
---

## **سيناريوهات الاستخدام المحتملة**
المقال التالي يشرح كيفية إنشاء وإزالة والحصول على تعليقات خلية الشبكة داخل ورقة العمل GridWeb. من الملحوظ أن GridWeb يعرض التعليق كأداة تلميحية مثل MS-Excel عندما تحوم الماوس فوق الخلية كما هو موضح في هذه اللقطة الشاشة.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **إنشاء كائن تعليق داخل الخلية**
يرجى استخدام طريقة GridCell.CreateComment لإنشاء كائن تعليق داخل الخلية. يقوم الكود النموذجي التالي بإنشاء تعليق عينة في خلية B4 من الورقة العمل الأولى لـ GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **إزالة كائن التعليق من الخلية**
يرجى استخدام طريقة GridCell.RemoveComment لإزالة كائن تعليق من الخلية. يقوم الكود العيني التالي بإزالة تعليق الخلية B4 داخل الورقة العمل الأولى في GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **الحصول على كائن التعليق من الخلية**
يرجى استخدام طريقة GridCell.GetComment() للحصول على كائن تعليق من الخلية. يقوم الكود العيني التالي بالحصول على كائن التعليق من الخلية B4 ثم الوصول إلى خصائصها المختلفة مثل المؤلف والملاحظة والرؤية وما إلى ذلك.

{{< highlight java >}}

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




