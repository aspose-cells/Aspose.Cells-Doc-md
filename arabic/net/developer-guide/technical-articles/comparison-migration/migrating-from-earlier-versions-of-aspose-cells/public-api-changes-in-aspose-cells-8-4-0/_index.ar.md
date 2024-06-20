---
title: تغييرات الواجهة العامة في Aspose.Cells 8.4.0
type: docs
weight: 130
url: /ar/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات العامة لـ Aspose.Cells من الإصدار 8.3.2 إلى 8.4.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. إنه يشمل ليس فقط الطرق العامة الجديدة والمحدثة و [الفئات المضافة الخ](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-0/) و [الفئات المحذوفة الخ](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-0/)، ولكن أيضاً وصف لأي تغييرات في السلوك الكامن في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية تعديل رموز VBA/Macro في جداول البيانات**
من أجل توفير وظيفة [تلاعب بكود VBA/ماكرو](/cells/ar/net/modifying-vba-or-macro-code-using-aspose-cells/)، قد عرضت Aspose.Cells for .NET 8.4.0 سلسلة من الفئات والخصائص الجديدة في فضاء Aspose.Cells.Vba. عدد من التفاصيل الهامة لهذه الفئات الجديدة هي كالتالي.

- يمكن استخدام فئة VbaProject لاسترداد مشروع VBA من جدول بيانات معين.
- تمثل فئة VbaModuleCollection مجموعة الوحدات VBA التي تشكل جزءًا من VbaProject معين.
- تمثل فئة VbaModule وحدة واحدة من VbaModuleCollection.

يظهر مقتطف الكود التالي كيفية تعديل الأكواد VBA بشكل ديناميكي.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **القدرة على إزالة جدول الدوران**
Aspose.Cells for .NET 8.4.0 عرضت طريقتين لـ PivotTableCollection لتوفير وظيفة إزالة جدول محور من ورقة عمل معينة. تفاصيل الطرق المذكورة سابقًا هي كالتالي.

- تقبل طريقة PivotTableCollection.Remove كائن PivotTable وتقوم بإزالته من المجموعة.
- تقبل طريقة PivotTableCollection.RemoveAt قيمة صحيفة استنادية بناءً على الصفر وتقوم بإزالة الجدول المحوري المعين من المجموعة.

يوضح مقتطف الكود التالي كيفية إزالة جدول الدوران باستخدام الارتباطين المذكورة أعلاه.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **دعم تخطيطات جدول الدوران المختلفة**
Aspose.Cells for .NET 8.4.0 يوفر الدعم لتخطيطات محددة مختلفة لجداول Pivot. من أجل توفير هذه الميزة ، فإن واجهات برمجة التطبيقات Aspose.Cells قد كشفت عن ثلاثة طرق لفئة PivotTable كما هو موضح أدناه.

- تقوم طريقة PivotTable.ShowInCompactForm بعرض جدول Pivot في التخطيط المضغوط.
- تقوم طريقة PivotTable.ShowInOutlineForm بعرض جدول Pivot في تخطيط المخطط.
- تقوم طريقة PivotTable.ShowInTabularForm بعرض جدول Pivot في التخطيط الجدولي.

{{% alert color="primary" %}} 

من المهم استدعاء PivotTable.RefreshData و PivotTable.CalculateData بعد ضبط أي من التخطيطات المذكورة أعلاه.

{{% /alert %}} 

يقوم المقتطف البرمجي التالي بتعيين تخطيطات مختلفة لجدول دوران ويخزن النتيجة على القرص.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **تمت إضافة فئة TxtLoadStyleStrategy وخاصية TxtLoadOptions.LoadStyleStrategy**
قامت Aspose.Cells for .NET 8.4.0 بكشف فئة TxtLoadStyleStrategy وخاصية TxtLoadOptions.LoadStyleStrategy لتحديد استراتيجية تنسيق القيم المحللة أثناء تحويل القيمة النصية إلى رقم أو تاريخ.
### **تمت إضافة DataBar.ToImage Method**
مع إصدار v8.4.0 ، قدمت واجهة برمجة التطبيقات Aspose.Cells طريقة DataBar.ToImage لحفظ شريط بيانات الشروط بتنسيق الصورة. تقبل الطريقة {DataBar.ToImage}} معلمتين كما هو موضح أدناه.

- المعلمة الأولى هي من نوع Aspose.Cells.Cell التي تم تطبيق التنسيق الشرطي عليها.
- المعلمة الثانية هي من نوع Aspose.Cells.Rendering.ImageOrPrintOptions من أجل ضبط معلمات مختلفة للصورة الناتجة.

الكود النموذجي التالي يوضح استخدام طريقة DataBar.ToImage لعرض شريط البيانات بتنسيق صورة.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **تمت إضافة خاصية Border.ThemeColor.**
تسمح واجهات برمجة التطبيقات Aspose.Cells باستخراج بيانات التنسيق ذات الصلة بالنوع من ورق الجداول. مع إصدار Aspose.Cells for .NET 8.4.0 ، فقد كشفت الواجهة عن خاصية Border.ThemeColor التي يمكن استخدامها لاسترداد سمات لون النمط الخاص بحدود الخلية.
### **تمت إضافة خاصية DrawObject.ImageBytes.**
قامت Aspose.Cells for .NET 8.4.0 بكشف الخاصية DrawObject.ImageBytes للحصول على بيانات الصورة من الرسم البياني أو الشكل.
### **تمت إضافة خاصية HtmlSaveOptions.ExportBogusRowData.**
قدمت Aspose.Cells for .NET 8.4.0 الخاصية {HtmlSaveOptions.ExportBogusRowData}}. تحدد الخاصية من نوع Boolean ما إذا كانت واجهة برمجة التطبيقات ستدخل بيانات الصف الباطل أثناء تصدير جدول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي صحيحة.

{{% /alert %}} 

الكود عينة التالية توضح استخدام الخاصية المذكورة سابقًا.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية HtmlSaveOptions.CellCssPrefix.**
خاصية HtmlSaveOptions.CellCssPrefix الجديدة تسمح بتعيين البادئة لملفات CSS أثناء تصدير جداول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي "" (سلسلة فارغة).

{{% /alert %}}
## **واجهات برمجة التطبيقات المهملة**
### **واجهات برمجة التطبيقات المهجورة Cells.GetCellByIndex & Row.GetCellByIndex**
استخدم الطريقة GetEnumerator لتكرار جميع الخلايا بدلاً من ذلك.
### **واجهات برمجة التطبيقات المهملة DrawObject.Image**
استخدم خاصية DrawObject.ImageBytes للحصول على بيانات الصورة بدلاً من ذلك.
