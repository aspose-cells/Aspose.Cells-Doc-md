---
title: عام API التغييرات في Aspose.Cells 8.5.2
type: docs
weight: 180
url: /ar/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 توضح هذه الوثيقة التغييرات التي تم إجراؤها على Aspose.Cells API من النسخة 8.5.1 إلى 8.5.2 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-5-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تقديم ورقة العمل إلى سياق رسومي**
 كشف هذا الإصدار من Aspose.Cells for .NET API عن حملين زائدين جديدين من طريقة SheetRender.ToImage التي تسمح الآن بقبول مثيل لفئة System.Drawing.Graphics إلى[تقديم في سياق الرسومات](/cells/ar/net/render-worksheet-to-graphic-context/). تواقيع الطرق المضافة حديثًا هي كما يلي.

1. SheetRender.ToImage (int pageIndex ، Graphics g ، float x ، float y)
1. SheetRender.ToImage (int pageIndex، Graphics g، float x، float y، float width، float width، float height)

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **أسلوب PivotTable.GetCellByDisplayName مضاف**
 كشف Aspose.Cells for .NET 8.5.2 طريقة PivotTable.GetCellByDisplayName التي يمكن استخدامها[استرداد عنصر Cell بواسطة اسم PivotField](/cells/ar/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). قد تكون هذه الطريقة مفيدة في السيناريوهات التي تريد فيها تمييز رأس PivotField أو تنسيقه.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية SaveOptions.MergeAreas**
كشف Aspose.Cells for .NET 8.5.2 خاصية SaveOptions.MergeAreas التي يمكنها قبول قيمة النوع المنطقي. القيمة الافتراضية غير صحيحة ، ولكن إذا تم ضبطها على صواب ، فإن Aspose.Cells for .NET API يحاول دمج CellArea الفردي قبل حفظ الملف.

{{% alert color="primary" %}} 

إذا كان جدول البيانات يحتوي على عدد كبير جدًا من الخلايا الفردية مع تطبيق التحقق من الصحة ، فهناك احتمالية أن يكون جدول البيانات الناتج تالفًا. أحد الحلول الممكنة هو دمج الخلايا بقواعد تحقق مماثلة أو يمكنك الآن استخدام خاصية SaveOptions.MergeAreas لتوجيه API لدمج CellAreas تلقائيًا قبل حفظ العملية.

{{% /alert %}} 
### **تمت إضافة شكل الملكية. الهندسة**
 مع إصدار v8.5.2 ، كشف Aspose.Cells API خاصية Shape.Geometry.ShapeAdjustValues التي يمكن استخدامها[إجراء تغييرات على نقاط الضبط للأشكال المختلفة](/cells/ar/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

في واجهة Microsoft Excel ، يتم عرض نقاط الضبط كعقد ماسية صفراء.

{{% /alert %}} 

على سبيل المثال،

1. مستطيل مدور لديه تعديل لتغيير القوس
1. المثلث لديه تعديل لتغيير موقع النقطة
1. شبه منحرف لديه تعديل لتغيير عرض الجزء العلوي
1. تحتوي الأسهم على تعديلين لتغيير شكل الرأس والذيل

هنا هو أبسط سيناريو استخدام.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **تمت إضافة حقل التعداد**
 كشف Aspose.Cells for .NET 8.5.2 دالة Consolidation.DistinctCount التي يمكن استخدامها[تطبيق وظيفة توحيد العد المميز](/cells/ar/net/consolidation-function/) في DataField في PivotTable.

{{% alert color="primary" %}} 

وظيفة دمج العد المميزة مدعومة بواسطة Microsoft Excel 2013 فقط.

{{% /alert %}} 
### **معالجة أفضل للأحداث لـ GridDesktop**
كشف هذا الإصدار من Aspose.Cells.GridDesktop عن 4 أحداث جديدة. يتم تشغيل 2 من هذه الأحداث في حالات مختلفة لتحميل ملفات جداول البيانات في GridDesktop بينما يتم تشغيل الحدثين الآخرين عند حساب الصيغ.

يتم سرد الأحداث على النحو التالي.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop. قبل الحساب
1. GridDesktop.FinishCalculate
