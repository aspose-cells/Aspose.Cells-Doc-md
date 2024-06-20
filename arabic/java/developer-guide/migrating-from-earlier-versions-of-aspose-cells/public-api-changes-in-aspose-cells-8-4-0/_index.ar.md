---
title: تغييرات الواجهة العامة في Aspose.Cells 8.4.0
type: docs
weight: 140
url: /ar/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.3.2 إلى 8.4.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات / التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة ، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية تعديل رموز VBA/Macro في جداول البيانات**
لتوفير ميزة [تلاعب الكود VBA/Macro](/cells/ar/java/modifying-vba-or-macro-code-using-aspose-cells/)، قامت Aspose.Cells for Java 8.4.0 بتعريض سلسلة من الفئات والخصائص الجديدة في حزمة com.aspose.cells.Vba. بعض تفاصيل الفئات الجديدة المهمة كما يلي.

- يمكن استخدام فئة VbaProject لاسترداد مشروع VBA من جدول بيانات معين.
- تمثل فئة VbaModuleCollection مجموعة الوحدات VBA التي تشكل جزءًا من VbaProject معين.
- تمثل فئة VbaModule وحدة واحدة من VbaModuleCollection.

يظهر مقتطف الكود التالي كيفية تعديل الأكواد VBA بشكل ديناميكي.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **القدرة على إزالة جدول الدوران**
قامت Aspose.Cells for Java 8.4.0 بتعريض طريقتين لمجموعة الجدول المحوري لتوفير ميزة إزالة جدول بيانات محوري من جدول بيانات معين. تفاصيل الطرق المذكورة أدناه.

- يقبل الارتباط PivotTableCollection.remove كائنًا من PivotTable ، ويزيله من المجموعة.
- يقبل الارتباط PivotTableCollection.removeAt قيمة صحيحة من نوع الصفر ويزيل PivotTable معينة من المجموعة.

يوضح مقتطف الكود التالي كيفية إزالة جدول الدوران باستخدام الارتباطين المذكورة أعلاه.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **دعم تخطيطات جدول الدوران المختلفة**
توفر Aspose.Cells for Java 8.4.0 الدعم لتخطيطات محددة مخصصة مختلفة للجداول الدورية. من أجل توفير هذه الميزة، قدم واجهات برمجة التطبيقات Aspose.Cells ثلاث طرق لفئة PivotTable كما هو مفصل أدناه.

- يقوم الارتباط PivotTable.showInCompactForm بعرض جدول الدوران في النسق المضغوط.
- يقوم الارتباط PivotTable.showInOutlineForm بعرض جدول الدوران في تخطيط المخطط.
- يقوم الارتباط PivotTable.showInTabularForm بعرض جدول الدوران في التخطيط الجدولي.

{{% alert color="primary" %}} 

من المهم استدعاء PivotTable.refreshData و PivotTable.calculateData بعد تعيين أي من التخطيطات المذكورة أعلاه. 

{{% /alert %}} 

يقوم المقتطف البرمجي التالي بتعيين تخطيطات مختلفة لجدول دوران ويخزن النتيجة على القرص.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **تمت إضافة فئة TxtLoadStyleStrategy وخاصية TxtLoadOptions.LoadStyleStrategy**
قدمت Aspose.Cells for Java 8.4.0 فئة TxtLoadStyleStrategy وخاصية TxtLoadOptions.LoadStyleStrategy من أجل تحديد الاستراتيجية لتنسيق القيم المعالجة أثناء تحويل القيمة النصية إلى رقم أو تاريخ.
### **تمت إضافة DataBar.ToImage Method**
مع إصدار الإصدار 8.4.0، قدّمت واجهة برمجة التطبيقات لـ Aspose.Cells الارتباط DataBar.toImage لحفظ شريط البيانات المشروط في تنسيق الصورة. يقبل الارتباط DataBar.toImage ثلاثة معلمات كما هو مفصل أدناه.

- النموذج الأول من النوع com.aspose.cells.Cell الذي تم تطبيق التنسيق المشروط عليه.
- النموذج الثاني من نوع com.aspose.cells.rendering.ImageOrPrintOptions من أجل تعيين معلمات مختلفة للصورة الناتجة.

الكود عينة التالية توضح استخدام الطريقة DataBar.toImage لتقديم DataBar في شكل صورة.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **تمت إضافة خاصية Border.ThemeColor.**
تسمح واجهات برمجة التطبيقات Aspose.Cells باستخراج البيانات ذات الصلة بالسمة من جداول البيانات. مع إصدار Aspose.Cells for Java 8.4.0، قد عُرضت خاصية Border.ThemeColor التي يمكن استخدامها لاسترداد خصائص لون السمة لحدود الخلية.
### **تمت إضافة خاصية DrawObject.ImageBytes.**
Aspose.Cells for Java 8.4.0 قد عرضت خاصية DrawObject.ImageBytes للحصول على بيانات الصورة من الرسم البياني أو الشكل.
### **تمت إضافة خاصية HtmlSaveOptions.ExportBogusRowData.**
قدمت Aspose.Cells for Java 8.4.0 خاصية {HtmlSaveOptions.ExportBogusRowData}. تحدد الخاصية من نوع بولياني إذا كان سيقوم الواجهة برمجة التطبيقات بحقن بيانات صف سفلية وهمية أثناء تصدير جداول البيانات إلى تنسيق HTML. 

{{% alert color="primary" %}} 

القيمة الافتراضية هي صحيحة.

{{% /alert %}} 

الكود عينة التالية توضح استخدام الخاصية المذكورة سابقًا.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **تمت إضافة خاصية HtmlSaveOptions.CellCssPrefix.**
خاصية HtmlSaveOptions.CellCssPrefix الجديدة تسمح بتعيين البادئة لملفات CSS أثناء تصدير جداول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي "" (سلسلة فارغة).

{{% /alert %}}
## **واجهات برمجة التطبيقات المهملة**
### **واجهات برمجة التطبيقات المهملة Cells.getCellByIndex & Row.getCellByIndex**
استخدم الطريقة getEnumerator لتكرار جميع الخلايا بدلاً من ذلك.
### **واجهات برمجة التطبيقات المهملة DrawObject.Image**
استخدم خاصية DrawObject.ImageBytes للحصول على بيانات الصورة بدلاً من ذلك.
