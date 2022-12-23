---
title: إضافة ارتباطات تشعبية لربط البيانات في Aspose.Cells
type: docs
weight: 10
url: /ar/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية ، خاصة على مواقع الويب.

باستخدام Aspose.Cells ، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Excel Microsoft. يناقش هذا الموضوع أنواع الارتباطات التشعبية التي يدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}}

## **إضافة الارتباطات التشعبية**

يمكن إضافة ثلاثة أنواع من الارتباط التشعبي إلى خلية باستخدام Aspose.Cells:

- [إضافة ارتباط إلى URL](#adding-link-to-a-url).
- [إضافة ارتباط إلى خلية أخرى في نفس الملف](#adding-a-link-to-a-cell-in-the-same-file).
- [إضافة ارتباط إلى ملف خارجي](#adding-a-link-to-an-external-file).

 Aspose.Cells يسمح للمطورين بإضافة ارتباطات تشعبية إلى ملفات Excel إما باستخدام API أو[جداول بيانات المصمم](/cells/ar/net/what-is-a-designer-spreadsheet/)(جداول البيانات حيث يتم إنشاء الارتباطات التشعبية يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class طرقًا مختلفة لإضافة ارتباطات تشعبية مختلفة إلى ملفات Excel.

### **إضافة ارتباط إلى URL**

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة تحتوي على[**الارتباطات التشعبية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) مجموعة. يمثل كل عنصر في مجموعة الارتباطات التشعبية ارتباطًا تشعبيًا. أضف ارتباطات تشعبية إلى عناوين URL عن طريق استدعاء طريقة إضافة مجموعة الارتباطات التشعبية. تأخذ طريقة الإضافة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا
- URL ، عنوان URL.

**C#**

{{< highlight "csharp" >}}

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

### **إضافة ارتباط إلى Cell في نفس الملف**

من الممكن إضافة ارتباطات تشعبية إلى الخلايا في نفس ملف Excel عن طريق استدعاء طريقة إضافة مجموعة الارتباط التشعبي. تعمل طريقة الإضافة مع الارتباطات التشعبية الداخلية والخارجية. يأخذ إصدار واحد من الطريقة overloaded المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الخلية المستهدفة.

**C#**

{{< highlight "csharp" >}}

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

### **إضافة ارتباط إلى ملف خارجي**

من الممكن إضافة ارتباطات تشعبية إلى ملفات Excel الخارجية عن طريق استدعاء طريقة إضافة مجموعة الارتباطات التشعبية. تأخذ طريقة الإضافة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الهدف ، ملف Excel خارجي.

**C#**

{{< highlight "csharp" >}}

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

## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
