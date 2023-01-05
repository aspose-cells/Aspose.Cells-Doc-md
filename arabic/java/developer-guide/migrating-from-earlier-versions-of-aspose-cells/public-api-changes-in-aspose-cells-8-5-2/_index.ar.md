---
title: عام API التغييرات في Aspose.Cells 8.5.2
type: docs
weight: 190
url: /ar/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 توضح هذه الوثيقة التغييرات التي تم إجراؤها على Aspose.Cells API من النسخة 8.5.1 إلى 8.5.2 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-5-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تقديم ورقة العمل إلى سياق رسومي**
كشف هذا الإصدار من Aspose.Cells for Java API عن حمل زائد آخر لطريقة SheetRender.toImage التي تسمح الآن بقبول مثيل لفئة Graphics2D[تقديم ورقة العمل في سياق الرسومات](/cells/ar/java/render-worksheet-to-graphic-context/). تواقيع الطريقة المضافة حديثًا هي كما يلي.

- SheetRender.toImage (int pageIndex ، Graphics2D Graphic)

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **أسلوب PivotTable.getCellByDisplayName مضاف**
 كشف Aspose.Cells for Java 8.5.2 طريقة PivotTable.getCellByDisplayName التي يمكن استخدامها[استرداد عنصر Cell بواسطة اسم PivotField](/cells/ar/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). قد تكون هذه الطريقة مفيدة في السيناريوهات التي تريد فيها تمييز رأس PivotField أو تنسيقه.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **تمت إضافة خاصية SaveOptions.MergeAreas**
كشف Aspose.Cells for Java 8.5.2 خاصية SaveOptions.MergeAreas التي يمكنها قبول قيمة النوع المنطقي. القيمة الافتراضية غير صحيحة ، ولكن إذا تم ضبطها على صواب ، فإن Aspose.Cells for Java API يحاول دمج CellArea الفردي قبل حفظ الملف.

{{% alert color="primary" %}} 

إذا كان جدول البيانات يحتوي على عدد كبير جدًا من الخلايا الفردية مع تطبيق التحقق من الصحة ، فهناك احتمالية أن يكون جدول البيانات الناتج تالفًا. أحد الحلول الممكنة هو دمج الخلايا بقواعد تحقق مماثلة أو يمكنك الآن استخدام خاصية SaveOptions.MergeAreas لتوجيه API لدمج CellAreas تلقائيًا قبل حفظ العملية.

{{% /alert %}} 
### **هندسة الخاصية. تمت إضافة ShapeAdjustValues**
 مع إصدار v8.5.2 ، كشف Aspose.Cells API عن طريقة Geometry.getShapeAdjustValues التي يمكن استخدامها[الوصول إلى نقاط الضبط ذات الأشكال المختلفة وإجراء تغييرات عليها](/cells/ar/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

في واجهة Microsoft Excel ، يتم عرض نقاط الضبط كعقد ماسية صفراء.

{{% /alert %}} 

 على سبيل المثال،

1. مستطيل مدور لديه تعديل لتغيير القوس
1. المثلث لديه تعديل لتغيير موقع النقطة
1. شبه منحرف لديه تعديل لتغيير عرض الجزء العلوي
1. تحتوي الأسهم على تعديلين لتغيير شكل الرأس والذيل

هنا هو أبسط سيناريو استخدام.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **دمج حقل التعداد. تمت إضافة DISTINCT_COUNT**
كشف Aspose.Cells for Java 8.5.2 وظيفة Consolidation.DISTINCT_COUNT التي يمكن استخدامها لتطبيق وظيفة Distinct Count المدمجة في DataField في PivotTable.

{{% alert color="primary" %}} 

وظيفة دمج العد المميزة مدعومة بواسطة Microsoft Excel 2013 فقط.

{{% /alert %}}
