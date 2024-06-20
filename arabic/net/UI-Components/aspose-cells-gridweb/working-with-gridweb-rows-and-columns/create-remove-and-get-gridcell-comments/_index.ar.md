---
title: إنشاء وحذف والحصول على تعليقات خلية الجدول
type: docs
weight: 100
url: /ar/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: يقدم هذا المقال كيفية العمل مع التعليق في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
يشرح المقال التالي كيفية إنشاء وإزالة والحصول على تعليق من خلية (GridCell) داخل ورقة العمل GridWeb. يجدر بالذكر أن GridWeb يعرض التعليق كتلميح مثل MS-Excel عندما تحوم بالفأرة فوق الخلية كما هو موضح في هذه اللقطة.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **إنشاء كائن تعليق داخل الخلية**
يرجى استخدام طريقة GridCell.CreateComment لإنشاء كائن تعليق داخل الخلية. يقوم الكود النموذجي التالي بإنشاء تعليق عينة في خلية B4 من الورقة العمل الأولى لـ GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **إزالة كائن التعليق من الخلية**
يرجى استخدام طريقة GridCell.RemoveComment لإزالة كائن تعليق من الخلية. يقوم الكود النموذجي التالي بإزالة تعليق خلية B4 داخل الورقة الأولى لـ GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **الحصول على كائن التعليق من الخلية**
يرجى استخدام الطريقة GridCell.GetComment() للحصول على كائن التعليق من الخلية. يقوم الكود النموذجي التالي بالحصول على كائن التعليق من الخلية B4 ثم الوصول إلى خصائصه المختلفة مثل الكاتب، الملاحظة، الرؤية وما إلى ذلك.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
