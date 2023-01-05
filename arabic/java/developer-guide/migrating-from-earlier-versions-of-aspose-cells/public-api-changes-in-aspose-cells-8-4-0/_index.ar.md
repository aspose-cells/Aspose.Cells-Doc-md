---
title: عام API التغييرات في Aspose.Cells 8.4.0
type: docs
weight: 140
url: /ar/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.2 إلى 8.4.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-0/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-0/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية لتعديل VBA / Macro Code في جداول البيانات**
 من أجل توفير ميزة[معالجة التعليمات البرمجية لـ VBA / الماكرو](/cells/ar/java/modifying-vba-or-macro-code-using-aspose-cells/)، كشف Aspose.Cells for Java 8.4.0 عن سلسلة من الفئات والخصائص الجديدة في حزمة com.aspose.cells.Vba. فيما يلي بعض التفاصيل المهمة لهذه الفئات الجديدة.

- يمكن استخدام فئة VbaProject لجلب مشروع VBA من جدول بيانات معين.
- تمثل فئة VbaModuleCollection مجموعة وحدات VBA النمطية التي تعد جزءًا من مشروع VbaProject المحدد.
- تمثل فئة VbaModule وحدة واحدة من VbaModuleCollection.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعديل مقاطع التعليمات البرمجية لـ VBA ديناميكيًا.

**Java**

{{< highlight "csharp" >}}

 مصنف المصنف = مصنف جديد ("source.xlsm") ؛

// تغيير رمز وحدة VBA

وحدات VbaModuleCollection = workbook.getVbaProject (). getModules () ؛

 لـ (int i = 0 ؛ i< modules.getCount(); i++)

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
### **القدرة على إزالة الجدول المحوري**
كشف Aspose.Cells for Java 8.4.0 طريقتين لمجموعة PivotTableCollection لتوفير ميزة إزالة Pivot Table من جدول بيانات معين. تفاصيل الطرق المذكورة هي كما يلي.

- يقبل أسلوب PivotTableCollection.remove كائن PivotTable ويزيله من المجموعة.
- يقبل أسلوب PivotTableCollection.removeAt قيمة عدد صحيح تستند إلى فهرس صفري ويزيل PivotTable معين من المجموعة.

يوضح مقتطف التعليمات البرمجية التالي كيفية إزالة PivotTable باستخدام كلتا الطريقتين المذكورتين أعلاه.

**Java**

{{< highlight "csharp" >}}

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
### **دعم لتخطيطات الجدول المحوري المختلفة**
Aspose.Cells for Java 8.4.0 يوفر الدعم لمختلف المخططات المعرفة مسبقًا للجداول المحورية. لتوفير هذه الميزة ، كشفت واجهات برمجة التطبيقات Aspose.Cells ثلاث طرق لفئة PivotTable كما هو مفصل أدناه.

- يعرض أسلوب PivotTable.showInCompactForm الجدول المحوري في التخطيط المضغوط.
- يعرض أسلوب PivotTable.showInOutlineForm الجدول المحوري في تخطيط المخطط التفصيلي.
- يعرض أسلوب PivotTable.showInTabularForm الجدول المحوري في تخطيط جدولي.

{{% alert color="primary" %}} 

 من المهم استدعاء PivotTable.refreshData & PivotTable.calculateData بعد تعيين أي من التخطيطات المذكورة أعلاه.

{{% /alert %}} 

يعيّن نموذج التعليمات البرمجية التالي تخطيطات مختلفة لجدول Pivot ويخزن النتيجة على القرص.

**Java**

{{< highlight "csharp" >}}

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
### **Class TxtLoadStyle الإستراتيجية والممتلكات TxtLoadOptions.LoadStyle الإستراتيجية المضافة**
كشف Aspose.Cells for Java 8.4.0 عن فئة TxtLoadStyleStrategy و TxtLoadOptions.LoadStyleStrategy من أجل تحديد استراتيجية تنسيق القيم التي تم تحليلها أثناء تحويل قيمة السلسلة إلى رقم أو وقت تاريخ.
### **الطريقة DataBar.ToImage مضافة**
مع إصدار v8.4.0 ، قدم Aspose.Cells API طريقة DataBar.toImage لحفظ DataBar المنسق شرطيًا في تنسيق صورة. تقبل طريقة {DataBar.toImage}} معلمتين على النحو المفصل أدناه.

- المعامل الأول من النوع com.aspose.cells.Cell الذي تم تطبيق التنسيق الشرطي عليه.
- المعامل الثاني هو من النوع com.aspose.cells.rendering.ImageOrPrintOptions لتعيين معاملات مختلفة للصورة الناتجة.

يوضح نموذج التعليمات البرمجية التالي استخدام أسلوب DataBar.toImage لتقديم DataBar بتنسيق صورة.

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **تمت إضافة الخاصية Border.ThemeColor**
تسمح واجهات برمجة التطبيقات Aspose.Cells باستخراج البيانات المتعلقة بالموضوع من جداول البيانات. مع إصدار Aspose.Cells for Java 8.4.0 ، كشف API خاصية Border.ThemeColor التي يمكن استخدامها لاسترداد سمات لون النسق لحدود Cell.
### **تمت إضافة خاصية DrawObject.ImageBytes**
كشف Aspose.Cells for Java 8.4.0 الخاصية DrawObject.ImageBytes للحصول على بيانات الصورة من Chart أو Shape.
### **تمت إضافة الخاصية HtmlSaveOptions.ExportBogusRowData**
 قدم Aspose.Cells for Java 8.4.0 خاصية {HtmlSaveOptions.ExportBogusRowData}}. تحدد خاصية النوع المنطقي ما إذا كان API سيضخ بيانات زائفة للصف السفلي أثناء تصدير جدول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي الحقيقية.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي استخدام الخاصية المذكورة.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **تمت إضافة الخاصية HtmlSaveOptions.CellCssPrefix**
تسمح الخاصية المضافة حديثًا HtmlSaveOptions.CellCssPrefix بتعيين البادئة لملفات CSS أثناء تصدير جداول البيانات إلى تنسيق HTML.

{{% alert color="primary" %}} 

القيمة الافتراضية هي سلسلة فارغة).

{{% /alert %}}
## **واجهات برمجة التطبيقات المهجورة**
### **طرق Cells.getCellByIndex & Row.getCellByIndex قديمة**
استخدم طريقة getEnumerator لتكرار كل الخلايا بدلاً من ذلك.
### **خاصية DrawObject.Image قديمة**
استخدم خاصية DrawObject.ImageBytes للحصول على بيانات الصورة بدلاً من ذلك.
