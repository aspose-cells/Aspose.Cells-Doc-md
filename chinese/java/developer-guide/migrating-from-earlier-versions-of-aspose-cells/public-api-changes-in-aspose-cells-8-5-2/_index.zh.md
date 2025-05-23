---
title: Aspose.Cells 8.5.2中的公共API更改
type: docs
weight: 190
url: /zh/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

描述了Aspose.Cells API从版本8.5.1到8.5.2的更改，这些更改可能对模块/应用程序开发人员感兴趣。其中包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-2/)，以及Aspose.Cells背后的行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **将工作表渲染到图形上下文**
Aspose.Cells for Java API的此版本已经暴露出SheetRender.toImage方法的另一个重载，现在可以接受Graphics2D类的实例来[在图形上下文中呈现Worksheet](/cells/zh/java/render-worksheet-to-graphic-context/)。新增方法的签名如下。

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

以下是简单的使用场景。

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
### **添加了PivotTable.getCellByDisplayName方法**
Aspose.Cells for Java 8.5.2已经暴露出PivotTable.getCellByDisplayName方法，可用于[根据PivotField的名称检索Cell对象](/cells/zh/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/)。在希望突出显示或格式化PivotField标题的情况下，此方法可能非常有用。

以下是简单的使用场景。

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
### **添加了SaveOptions.MergeAreas属性**
Aspose.Cells for Java 8.5.2已经暴露出SaveOptions.MergeAreas属性，可以接受布尔类型值。默认值为false，但如果设置为true，则在保存文件之前，Aspose.Cells for Java API将尝试合并单个CellArea。

{{% alert color="primary" %}} 

如果电子表格有太多应用了验证的个别单元格，导致最终的电子表格可能会损坏。一个可能的解决方案是合并具有相同验证规则的单元格，或者您现在可以使用SaveOptions.MergeAreas属性来指示API在保存操作之前自动合并CellAreas。

{{% /alert %}} 
### **添加了Geometry.ShapeAdjustValues属性**
随着v8.5.2版本的发布，Aspose.Cells API已经公开了Geometry.getShapeAdjustValues方法，可以用于[访问并更改不同形状的调整点](/cells/zh/java/change-adjustment-values-of-the-shape/)。

{{% alert color="primary" %}} 

在Microsoft Excel界面上，调整点显示为黄色菱形节点。

{{% /alert %}} 

例如， 

1. 圆角矩形具有用于更改弧度的调整
1. 三角形具有用于更改点位置的调整
1. 梯形具有用于更改顶部宽度的调整
1. 箭头具有用于更改头部和尾部形状的两个调整

这是最简单的使用场景。

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
### **添加了字段ConsolidationFunction.DISTINCT_COUNT枚举**
Aspose.Cells for Java 8.5.2已经暴露出ConsolidationFunction.DISTINCT_COUNT字段，可用于在PivotTable的DataField上应用不同计数合并函数。

{{% alert color="primary" %}} 

仅Microsoft Excel 2013支持Distinct Count统计函数。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
