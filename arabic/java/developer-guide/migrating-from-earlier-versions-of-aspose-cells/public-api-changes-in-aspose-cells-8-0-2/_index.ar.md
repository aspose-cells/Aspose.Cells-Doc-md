---
title: API عام تغييرات في Aspose.Cells 8.0.2
type: docs
weight: 40
url: /ar/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.0.1 إلى 8.0.2 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية TextDirection إلى فئة الشكل**
كشفت فئة الشكل عن خاصية TextDirection التي يمكن استخدامها للحصول على أو تعيين اتجاه تدفق النص لكائن الشكل. يمكن أيضًا استخدام خاصية TextDirection لتعيين اتجاه النص المطلوب للتعليقات في جدول بيانات كما هو موضح أدناه.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **تمت إضافة خاصية ConvertFormulasData إلى فئة HTMLLoadOptions**
تمت إضافة خاصية ConvertFormulasData إلى فئة HTMLLoadOptions ، وذلك لتسهيل قيام المطورين بتحميل صيغ Excel من ملفات HTML. تشير الخاصية المنطقية ConvertFormulasData إلى ما إذا كان سيتم تحويل السلسلة إلى صيغة أم لا عندما تبدأ قيمة السلسلة بالحرف '='.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

القيمة الافتراضية لخاصية ConvertFormulasData هي false.

{{% /alert %}}
## **تمت إضافة خاصية ImageOptions إلى فئة HtmlSaveOptions**
 تمت إضافة الخاصية ImageOptions إلى فئة HtmlSaveOptions. أدى تعريض خاصية ImageOptions إلى تمكين المطورين من تعيين التفضيلات للصور المضمنة في HTML أثناء تصدير جداول البيانات.
## **خاصية HtmlSaveOptions.ExportChartImageFormat قديمة**
تم وضع علامة HtmlSaveOptions.ExportChartImageFormat على أنه قديم بدءًا من Aspose.Cells for .NET 8.0.2. يُنصح باستخدام HtmlSaveOptions.ImageOptions بدلاً من ذلك لإعدادات تنسيق الصورة أثناء تصدير جداول البيانات إلى تنسيق HTML.
