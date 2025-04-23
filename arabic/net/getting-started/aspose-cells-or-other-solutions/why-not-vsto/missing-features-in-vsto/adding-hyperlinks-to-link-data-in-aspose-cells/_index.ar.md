---
title: إضافة ارتباطات تشعبية لربط البيانات في Aspose.Cells
type: docs
weight: 10
url: /ar/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.

باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}}

## **إضافة الروابط المختصرة**

يمكن إضافة ثلاثة أنواع من الارتباطات التشعبية إلى خلية باستخدام Aspose.Cells:

- [إضافة رابط إلى عنوان URL](#adding-link-to-a-url)
- [إضافة رابط إلى خلية أخرى في نفس الملف](#adding-a-link-to-a-cell-in-the-same-file)
- [إضافة رابط إلى ملف خارجي](#adding-a-link-to-an-external-file)

تتيح Aspose.Cells للمطورين إضافة ارتباطات تشعبية إلى ملفات Excel إما باستخدام واجهة برمجة التطبيقات أو [جداول البيانات المصممة](/cells/ar/net/what-is-a-designer-spreadsheet/) (جداول بيانات حيث يتم إنشاء الارتباطات التشعبية يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) طرقًا مختلفة لإضافة ارتباطات تشعبية مختلفة إلى ملفات Excel.

### **إضافة رابط إلى عنوان URL**

تحتوي فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) على مجموعة [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). يمثل كل عنصر في مجموعة الارتباطات Hyperlinks ارتباطًا تشعبيًا. أضف ارتباطات تشعبية إلى عناوين URL عن طريق استدعاء طريقة Add لمجموعة الارتباطات Hyperlinks. تأخذ طريقة Add المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة, عدد الأعمدة في نطاق الارتباط التشعبي
- عنوان URL, عنوان عنوان URL.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **إضافة رابط إلى خلية في نفس الملف**

من الممكن إضافة روابط فائقة إلى الخلايا في نفس ملف Excel عن طريق استدعاء أسلوب الإضافة في مجموعة الروابط الفائقة. يعمل أسلوب الإضافة لكل من الروابط الفائقة الداخلية والخارجية. إحدى الإصدارات المكدسة للطريقة تأخذ المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط الفائق إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **إضافة رابط إلى ملف خارجي**

من الممكن إضافة روابط تشعبية إلى ملفات Excel خارجية عن طريق استدعاء طريقة Add في مجموعة Hyperlinks. تأخذ طريقة Add المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **تحميل رمز عينة**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
