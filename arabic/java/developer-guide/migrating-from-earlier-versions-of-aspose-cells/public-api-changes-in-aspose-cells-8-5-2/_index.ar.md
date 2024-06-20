---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.5.2
type: docs
weight: 190
url: /ar/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.5.1 إلى 8.5.2 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. يتضمن ليس فقط الطرق العمومية الجديدة والمُحدثة، [والفئات المضافة وما إلى ذلك](/cells/ar/java/public-api-changes-in-aspose-cells-8-5-2/)، ولكن أيضا وصفا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **عرض الورقة العمل إلى سياق رسومي**
قام هذا الإصدار من واجهة برمجة التطبيقات Aspose.Cells for Java بتعريض إصدار آخر لطريقة SheetRender.toImage الذي يسمح الآن بقبول مثيل من فئة Graphics2D لـ [تقديم الورقة العمل في سياق الرسم](/cells/ar/java/render-worksheet-to-graphic-context/). توقيعات الطريقة الجديدة المضافة هي كالتالي.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة PivotTable.getCellByDisplayName Method**
Aspose.Cells for Java تمت إضافة الطريقة PivotTable.getCellByDisplayName في الإصدار 8.5.2 ليمكن استخدامها ل[استرداد كائن الخلية بواسطة اسم PivotField](/cells/ar/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). يمكن أن تكون هذه الطريقة مفيدة في السيناريوهات التي ترغب في تسليط الضوء على أو تنسيق رأس PivotField.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java تمت إضافة الخاصية SaveOptions.MergeAreas في الإصدار 8.5.2 لتقبل قيمة من نوع Boolean. القيمة الافتراضية هي false. ومع ذلك، إذا تم تعيينها إلى true، فإن Aspose.Cells for Java API يحاول دمج مناطق الخلية الفردية قبل حفظ الملف.

{{% alert color="primary" %}} 

إذا كان لديك ورقة بيانات تحتوي على العديد من الخلايا الفردية مع التطبيقات الصحيحة، فهناك فرص لتلف الورقة الناتجة. إحدى الحلول الممكنة هي دمج الخلايا ذات القواعد الصحيحة المتطابقة أو يمكنك الآن استخدام خاصية SaveOptions.MergeAreas لتوجيه الواجهة البرمجية لتلقائي دمج مناطق الخلايا قبل عملية الحفظ.

{{% /alert %}} 
### **تمت إضافة خاصية Geometry.ShapeAdjustValues**
مع إصدار v8.5.2، قامت واجهة برمجة التطبيقات Aspose.Cells بتوفير الطريقة Geometry.getShapeAdjustValues الممكن استخدامها ل[الوصول وإجراء تغييرات على نقاط التعديل لأشكال مختلفة](/cells/ar/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

في واجهة مستخدم Microsoft Excel، تظهر نقاط التعديل على شكل نقاط الماس الصفراء.

{{% /alert %}} 

على سبيل المثال، 

1. لديك مستطيل مستدير له تعديل لتغيير القوس
1. لديك مثلث له تعديل لتغيير موقع النقطة
1. لديك متوازي الأضلاع له تعديل لتغيير عرض الجزء العلوي
1. لديك سهام له تعديلين لتغيير شكل الرأس والذيل

فيما يلي سيناريو الاستخدام الأبسط.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة حقل عدد فريد لدالة التجميع ConsolidationFunction.DISTINCT_COUNT**
قامت الإصدارة 8.5.2 لـ Aspose.Cells for Java بعرض حقل ConsolidationFunction.DISTINCT_COUNT الذي يمكن استخدامه لتطبيق دالة التجميع الفريدة لحقول البيانات في PivotTable.

{{% alert color="primary" %}} 

دالة التجميع الفريدة Distinct Count مدعومة فقط في Microsoft Excel 2013.

{{% /alert %}}
