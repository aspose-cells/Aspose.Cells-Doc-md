---
title: API عام تغييرات في Aspose.Cells 8.0.2
type: docs
weight: 30
url: /ar/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.0.1 إلى 8.0.2 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية TextDirection إلى فئة الشكل**
كشفت فئة الشكل عن خاصية TextDirection التي يمكن استخدامها للحصول على أو تعيين اتجاه تدفق النص لكائن الشكل. يمكن أيضًا استخدام خاصية TextDirection لتعيين اتجاه النص المطلوب للتعليقات في جدول بيانات كما هو موضح أدناه.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[تغيير اتجاه نص التعليق](/cells/ar/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **تمت إضافة خاصية ConvertFormulasData إلى فئة HTMLLoadOptions**
تمت إضافة خاصية ConvertFormulasData إلى فئة HTMLLoadOptions ، من أجل تسهيل المطورين لتحميل صيغ Excel من ملفات HTML. تشير الخاصية المنطقية ConvertFormulasData إلى ما إذا كان سيتم تحويل السلسلة إلى صيغة أم لا عندما تبدأ قيمة السلسلة بالحرف '='.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

القيمة الافتراضية لخاصية ConvertFormulasData هي false.

{{% /alert %}}
## **تمت إضافة خاصية ImageOptions إلى فئة HtmlSaveOptions**
تمت إضافة الخاصية ImageOptions إلى فئة HtmlSaveOptions. أدى تعريض الخاصية ImageOptions إلى تمكين المطورين من تعيين التفضيلات للصور المضمنة في HTML أثناء تصدير جداول البيانات.
## **خاصية HtmlSaveOptions.ExportChartImageFormat قديمة**
تم وضع علامة HtmlSaveOptions.ExportChartImageFormat على أنه قديم بدءًا من Aspose.Cells for .NET 8.0.2. يُنصح باستخدام HtmlSaveOptions.ImageOptions بدلاً من ذلك لإعدادات تنسيق الصورة أثناء تصدير جداول البيانات إلى تنسيق HTML.
