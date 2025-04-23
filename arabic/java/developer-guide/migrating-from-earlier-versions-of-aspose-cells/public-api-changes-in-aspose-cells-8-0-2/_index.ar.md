---
title: تغييرات الواجهة العمومية في Aspose.Cells 8.0.2
type: docs
weight: 40
url: /ar/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.0.1 إلى 8.0.2، والتي قد تكون ذات أهمية لمطوري الوحدات / التطبيقات. يشمل ذلك ليس فقط الأساليب العمومية الجديدة والمحدثة، ولكن أيضًا وصفاً لأي تغييرات في السلوك الكامنة في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية اتجاه النص إلى فئة الشكل**
تتضمن فئة الشكل خاصية اتجاه النص التي يمكن استخدامها للحصول على الاتجاه أو تعيينه لتدفق النص لكائن الشكل. يمكن أيضًا استخدام خاصية اتجاه النص لتحديد اتجاه النص المطلوب للتعليقات في جدول البيانات كما هو موضح أدناه.

**Java**

{{< highlight csharp >}}

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
## **تمت إضافة خاصية تحويل بيانات الصيغ إلى فئة خيارات تحميل HTML**
تمت إضافة خاصية تحويل بيانات الصيغ إلى فئة خيارات تحميل HTML، من أجل تيسير عملية تحميل صيغ Excel من ملفات HTML. تشير خاصية تحويل بيانات الصيغ البوليانية إلى ما إذا كان يُحول السلسلة إلى صيغة عندما تبدأ قيمة السلسلة بالحرف '='.

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

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
{{< app/cells/assistant language="java" >}}
