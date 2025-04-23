---
title: تغييرات الواجهة العمومية في Aspose.Cells 8.0.2
type: docs
weight: 30
url: /ar/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.0.1 إلى 8.0.2، والتي قد تكون ذات أهمية لمطوري الوحدات / التطبيقات. يشمل ذلك ليس فقط الأساليب العمومية الجديدة والمحدثة، ولكن أيضًا وصفاً لأي تغييرات في السلوك الكامنة في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية اتجاه النص إلى فئة الشكل**
تتضمن فئة الشكل خاصية اتجاه النص التي يمكن استخدامها للحصول على الاتجاه أو تعيينه لتدفق النص لكائن الشكل. يمكن أيضًا استخدام خاصية اتجاه النص لتحديد اتجاه النص المطلوب للتعليقات في جدول البيانات كما هو موضح أدناه.

**C#**

{{< highlight csharp >}}

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

يرجى التحقق من المقال المفصل حول [تغيير اتجاه النص في التعليق](/cells/ar/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **تمت إضافة خاصية تحويل بيانات الصيغ إلى فئة خيارات تحميل HTML**
تمت إضافة خاصية تحويل بيانات الصيغ إلى فئة خيارات تحميل HTML، من أجل تيسير عملية تحميل صيغ Excel من ملفات HTML. تشير خاصية تحويل بيانات الصيغ البوليانية إلى ما إذا كان يُحول السلسلة إلى صيغة عندما تبدأ قيمة السلسلة بالحرف '='.

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

القيمة الافتراضية لخاصية تحويل بيانات الصيغ هي false.

{{% /alert %}}
## **تمت إضافة خاصية خيارات الصور إلى فئة خيارات حفظ HTML**
تمت إضافة خاصية خيارات الصور إلى فئة خيارات حفظ HTML. تعرض خاصية خيارات الصور تمكين المطورين من تعيين تفضيلات الصور المضمنة في HTML أثناء تصدير جداول البيانات.
## **تم تسويت خاصية تنسيق الصورة لحفظ خيارات حفظ HTML**
تم تحديد خاصية تنسيق الصورة لحفظ خيارات حفظ HTML بدءاً من 8.0.2 Aspose.Cells for .NET. يُنصح باستخدام خيارات الصور بدلاً من خاصية تنسيق الصورة لتحديد إعدادات تنسيق الصور أثناء تصدير جداول البيانات إلى تنسيق HTML.
{{< app/cells/assistant language="csharp" >}}
