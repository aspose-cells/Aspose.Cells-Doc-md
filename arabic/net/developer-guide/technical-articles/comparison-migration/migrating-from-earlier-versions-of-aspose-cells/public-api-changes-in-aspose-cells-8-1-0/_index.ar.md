---
title: تغييرات الواجهة العمومية في Aspose.Cells 8.1.0
type: docs
weight: 40
url: /ar/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.0.2 إلى 8.1.0، والتي قد تكون ذات أهمية لمطوري الوحدات / التطبيقات. يشمل ذلك ليس فقط الأساليب العمومية الجديدة والمحدثة، ولكن أيضًا وصفاً لأي تغييرات في السلوك الكامنة في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية حفظ الورقة مخفية إلى خيارات حفظ HTML**
فصل HtmlSaveOptions تضم خاصية ExportHiddenWorksheet التي يمكن استخدامها لتحديد ما إذا كانت الأوراق العمل المخفية تُصدر إلى تنسيق HTML. القيمة الافتراضية هي true، حيث إذا تم تعيينها على false، فإن Aspose.Cells لن تصدر محتويات الأوراق العمل المخفية.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [منع تصدير الورقة العامة الخفية](/cells/ar/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **تمت إضافة خاصية Cell.StringValueWithoutFormat**
تمت إضافة خاصية StringValueWithoutFormat إلى فئة الخلية، لتسهيل عمل المطورين في استرداد قيمة الخلية بدون تطبيق أي تنسيق.

يوضح قطعة الكود المقدمة أدناه استخدام خاصية Cell.StringValueWithoutFormat بالمقارنة مع خاصية cell.DisplayStringValue من خلال إنشاء جدول بيانات من البداية وتطبيق تنسيق الأرقام على إحدى الخلايا.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

إخراج الكود أعلاه هو كما يلي

123,456

123456

{{% /alert %}}
## **خصائص Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs تم تسجيلها بأنها منتهية الصلاحية**
تم تحديد العديد من الخصائص من فئة BuiltInDocumentPropertyCollection كمهجون اعتبارًا من Aspose.Cells for .NET 8.1.0. يشمل ذلك الخصائص Bytes وCharacters وCharactersWithSpaces وLines & Paragraphs. السبب في ذلك هو عدم الفائدة من هذه الخصائص في الحفاظ على جداول بيانات Excel لأن Excel يتجاهلها. حيث كانت هذه الخصائص مكتوبة أصلاً لمستندات Word وعروض تقديمية لـ PowerPoint.
