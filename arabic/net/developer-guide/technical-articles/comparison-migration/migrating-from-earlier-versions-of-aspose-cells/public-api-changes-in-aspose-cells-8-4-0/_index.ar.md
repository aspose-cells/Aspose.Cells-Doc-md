---
title: عام API التغييرات في Aspose.Cells 8.4.0
type: docs
weight: 130
url: /ar/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.2 إلى 8.4.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-0/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-0/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية لتعديل VBA / Macro Code في جداول البيانات**
 من أجل توفير ميزة[معالجة التعليمات البرمجية لـ VBA / الماكرو](/cells/ar/net/modifying-vba-or-macro-code-using-aspose-cells/)، أظهر Aspose.Cells for .NET 8.4.0 سلسلة من الفئات والخصائص الجديدة في مساحة الاسم Aspose.Cells.Vba. فيما يلي بعض التفاصيل المهمة لهذه الفئات الجديدة.

- يمكن استخدام فئة VbaProject لجلب مشروع VBA من جدول بيانات معين.
- تمثل فئة VbaModuleCollection مجموعة وحدات VBA النمطية التي تعد جزءًا من مشروع VbaProject المحدد.
- تمثل فئة VbaModule وحدة واحدة من VbaModuleCollection.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعديل مقاطع التعليمات البرمجية لـ VBA ديناميكيًا.

**C#**

{{< highlight "csharp" >}}

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


### **القدرة على إزالة الجدول المحوري**
كشف Aspose.Cells for .NET 8.4.0 طريقتين لمجموعة PivotTableCollection لتوفير ميزة إزالة Pivot Table من جدول بيانات معين. تفاصيل الطرق المذكورة هي كما يلي.

- يقبل أسلوب PivotTableCollection.Remove كائن PivotTable ويزيله من المجموعة.
- يقبل أسلوب PivotTableCollection.RemoveAt قيمة عدد صحيح تستند إلى فهرس صفري ويزيل PivotTable معين من المجموعة.

يوضح مقتطف التعليمات البرمجية التالي كيفية إزالة PivotTable باستخدام كلتا الطريقتين المذكورتين أعلاه.

**C#**

{{< highlight "csharp" >}}

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


### **دعم لتخطيطات الجدول المحوري المختلفة**
Aspose.Cells for .NET 8.4.0 يوفر الدعم لمختلف المخططات المعرفة مسبقًا للجداول المحورية. لتوفير هذه الميزة ، كشفت واجهات برمجة التطبيقات Aspose.Cells ثلاث طرق لفئة PivotTable كما هو مفصل أدناه.

- يعرض أسلوب PivotTable.ShowInCompactForm الجدول المحوري في التخطيط المضغوط.
- يعرض أسلوب PivotTable.ShowInOutlineForm الجدول المحوري في تخطيط المخطط التفصيلي.
- يعرض أسلوب PivotTable.ShowInTabularForm الجدول المحوري في تخطيط جدولي.

{{% alert color="primary" %}} 

من المهم استدعاء PivotTable.RefreshData & PivotTable.CalculateData بعد تعيين أي من التخطيطات المذكورة أعلاه.

{{% /alert %}} 

يعيّن نموذج التعليمات البرمجية التالي تخطيطات مختلفة لجدول Pivot ويخزن النتيجة على القرص.

**C#**

{{< highlight "csharp" >}}

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


### **Class TxtLoadStyle الإستراتيجية والممتلكات TxtLoadOptions.LoadStyle الإستراتيجية المضافة**
كشف Aspose.Cells for .NET 8.4.0 عن فئة TxtLoadStyleStrategy و TxtLoadOptions.LoadStyleStrategy من أجل تحديد استراتيجية تنسيق القيم التي تم تحليلها أثناء تحويل قيمة السلسلة إلى رقم أو وقت تاريخ.
### **الطريقة DataBar.ToImage مضافة**
مع إصدار v8.4.0 ، قدم Aspose.Cells API طريقة DataBar.ToImage لحفظ أشرطة البيانات المنسقة شرطيًا في تنسيق صورة. تقبل طريقة {DataBar.ToImage}} معلمتين على النحو المفصل أدناه.

- المعلمة الأولى من النوع Aspose.Cells.Cell التي تم تطبيق التنسيق الشرطي عليها.
- المعلمة الثانية من النوع Aspose.Cells.Rendering.ImageOrPrintOptions لتعيين معلمات مختلفة للصورة الناتجة.

يوضح نموذج التعليمات البرمجية التالي استخدام أسلوب DataBar.ToImage لتقديم DataBar بتنسيق صورة.

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **تمت إضافة الخاصية Border.ThemeColor**
تسمح واجهات برمجة التطبيقات Aspose.Cells باستخراج بيانات التنسيق المتعلقة بالموضوع من جداول البيانات. مع إصدار Aspose.Cells for .NET 8.4.0 ، كشف API خاصية Border.ThemeColor التي يمكن استخدامها لاسترداد سمات لون النسق لحدود Cell.
### **تمت إضافة خاصية DrawObject.ImageBytes**
كشف Aspose.Cells for .NET 8.4.0 الخاصية DrawObject.ImageBytes للحصول على بيانات الصورة من Chart أو Shape.
### **تمت إضافة الخاصية HtmlSaveOptions.ExportBogusRowData**
قدم Aspose.Cells for .NET 8.4.0 خاصية {HtmlSaveOptions.ExportBogusRowData}}. تحدد خاصية النوع المنطقي ما إذا كان API سيضخ بيانات زائفة للصف السفلي أثناء تصدير جدول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي الحقيقية.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي استخدام الخاصية المذكورة.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **تمت إضافة الخاصية HtmlSaveOptions.CellCssPrefix**
الخاصية المضافة حديثًا HtmlSaveOptions.CellCssPrefix تسمح بتعيين البادئة لملفات CSS أثناء تصدير جداول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي سلسلة فارغة).

{{% /alert %}}
## **واجهات برمجة التطبيقات المهجورة**
### **طرق Cells. GetCellByIndex & Row.GetCellByIndex قديمة**
استخدم طريقة GetEnumerator لتكرار كل الخلايا بدلاً من ذلك.
### **خاصية DrawObject.Image قديمة**
استخدم خاصية DrawObject.ImageBytes للحصول على بيانات الصورة بدلاً من ذلك.
