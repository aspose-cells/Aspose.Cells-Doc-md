---
title: تغييرات الواجهة العمومية في Aspose.Cells 8.1.0
type: docs
weight: 50
url: /ar/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.0.2 إلى 8.1.0، والتي قد تكون ذات أهمية لمطوري الوحدات / التطبيقات. يشمل ذلك ليس فقط الأساليب العمومية الجديدة والمحدثة، ولكن أيضًا وصفاً لأي تغييرات في السلوك الكامنة في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية حفظ الورقة مخفية إلى خيارات حفظ HTML**
فصل HtmlSaveOptions تضم خاصية ExportHiddenWorksheet التي يمكن استخدامها لتحديد ما إذا كانت الأوراق العمل المخفية تُصدر إلى تنسيق HTML. القيمة الافتراضية هي true، حيث إذا تم تعيينها على false، فإن Aspose.Cells لن تصدر محتويات الأوراق العمل المخفية.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [منع تصدير الأوراق العمل المخفية](/cells/ar/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **تمت إضافة خاصية Cell.StringValueWithoutFormat**
تمت إضافة خاصية StringValueWithoutFormat إلى فئة الخلية، لتسهيل عمل المطورين في استرداد قيمة الخلية بدون تطبيق أي تنسيق. 

الكود المقدم أدناه يظهر كيفية استخدام طريقة Cell.getStringValueWithoutFormat مقارنة ب cell.getDisplayStringValue عن طريق إنشاء جدول بيانات من البداية وتطبيق تنسيق على إحدى الخلايا. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

إخراج الكود أعلاه هو كما يلي

القيمة المنسقة: 123,456
القيمة غير المنسقة: 123456

{{% /alert %}}
## **خصائص Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs تم تسجيلها بأنها منتهية الصلاحية**
تم تحديد العديد من الخصائص من فئة BuiltInDocumentPropertyCollection كمهجون اعتبارًا من Aspose.Cells for .NET 8.1.0. يشمل ذلك الخصائص Bytes وCharacters وCharactersWithSpaces وLines & Paragraphs. السبب في ذلك هو عدم الفائدة من هذه الخصائص في الحفاظ على جداول بيانات Excel لأن Excel يتجاهلها. حيث كانت هذه الخصائص مكتوبة أصلاً لمستندات Word وعروض تقديمية لـ PowerPoint. 
{{< app/cells/assistant language="java" >}}
