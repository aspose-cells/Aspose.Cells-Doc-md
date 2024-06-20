---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.5.2
type: docs
weight: 180
url: /ar/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.5.1 إلى 8.5.2 التي قد تكون مثيرة لاهتمام مطوري الوحدات / التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة، وإضافة الفئات، وما إلى ذلك، ولكن أيضاً وصفاً لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **عرض الورقة العمل إلى سياق رسومي**
تم تعريف إصدار Aspose.Cells for .NET API الحالي بطرح اثنين من Overloads الجديدة لطريقة SheetRender.ToImage التي تسمح الآن بقبول مثيل من فئة System.Drawing.Graphics ل[الرسم في سياق الرسم](/cells/ar/net/render-worksheet-to-graphic-context/). تواقيع الأساليب الجديدة التي تمت إضافتها هي كالتالي.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **أضيفت طريقة PivotTable.GetCellByDisplayName**
ضاف Aspose.Cells for .NET 8.5.2 طريقة PivotTable.GetCellByDisplayName التي يمكن استخدامها ل[استرجاع كائن الخلية باسم PivotField](/cells/ar/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). يمكن أن تكون هذه الطريقة مفيدة في السيناريوهات حيث ترغب في تسليط الضوء على أو تنسيق رأس PivotField.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
ضاف Aspose.Cells for .NET 8.5.2 خاصية SaveOptions.MergeAreas التي يمكن أن تقبل قيمة من نوع Boolean. القيمة الافتراضية هي false، ومع ذلك، إذا تم ضبطها على true، فإن Aspose.Cells for .NET API يحاول دمج CellArea الفردية قبل حفظ الملف.

{{% alert color="primary" %}} 

إذا كان لديك ورقة بيانات تحتوي على العديد من الخلايا الفردية مع التطبيقات الصحيحة، فهناك فرص لتلف الورقة الناتجة. إحدى الحلول الممكنة هي دمج الخلايا ذات القواعد الصحيحة المتطابقة أو يمكنك الآن استخدام خاصية SaveOptions.MergeAreas لتوجيه الواجهة البرمجية لتلقائي دمج مناطق الخلايا قبل عملية الحفظ.

{{% /alert %}} 
### **أضيفت خاصية Shape.Geometry.ShapeAdjustValues**
مع إصدار v8.5.2، تم تعريف Aspose.Cells API بخاصية Shape.Geometry.ShapeAdjustValues التي يمكن استخدامها ل[إجراء تغييرات على نقاط التعديل لأشكال مختلفة](/cells/ar/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

في واجهة Microsoft Excel، تعرض نقاط التعديل كأعقاب الماسية الصفراء.

{{% /alert %}} 

على سبيل المثال،

1. لديك مستطيل مستدير له تعديل لتغيير القوس
1. لديك مثلث له تعديل لتغيير موقع النقطة
1. لديك متوازي الأضلاع له تعديل لتغيير عرض الجزء العلوي
1. لديك سهام له تعديلين لتغيير شكل الرأس والذيل

فيما يلي سيناريو الاستخدام الأبسط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة تعداد Field ConsolidationFunction.DistinctCount**
قام Aspose.Cells for .NET 8.5.2 بتعريض حقل ConsolidationFunction.DistinctCount الذي يمكن استخدامه لـ [تطبيق وظيفة تجميع العدد المميز](/cells/ar/net/consolidation-function/) على DataField من PivotTable.

{{% alert color="primary" %}} 

دالة التجميع الفريدة Distinct Count مدعومة فقط في Microsoft Excel 2013.

{{% /alert %}} 
### **تحسين معالجة الأحداث لـ GridDesktop**
تم تعريض 4 أحداث جديدة في الإصدار الحالي من Aspose.Cells.GridDesktop.  يُشغّل 2 من هذه الأحداث في حالات مختلفة من تحميل ملفات جداول البيانات في GridDesktop بينما تُشغّل 2 أخرى عند حساب الصيغ.

تم سرد الأحداث على النحو التالي.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
