---
title: 公共 API Aspose.Cells 8.5.2 的变化
type: docs
weight: 190
url: /zh/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.1 到 8.5.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-2/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **将工作表渲染到图形上下文**
此版本的 Aspose.Cells for Java API 公开了 SheetRender.toImage 方法的另一个重载，该方法现在允许接受 Graphics2D 类的实例以[在图形上下文中呈现工作表](/cells/zh/java/render-worksheet-to-graphic-context/).新增方法的签名如下。

- SheetRender.toImage(int pageIndex, Graphics2D 图形)

以下是简单的使用场景。

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
### **添加了方法 PivotTable.getCellByDisplayName**
 Aspose.Cells for Java 8.5.2公开了PivotTable.getCellByDisplayName方法，可以用来[通过 PivotField 的名称检索 Cell 对象](/cells/zh/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/).在您希望突出显示或格式化 PivotField 标头的情况下，此方法可能很有用。

以下是简单的使用场景。

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
### **添加属性 SaveOptions.MergeAreas**
Aspose.Cells for Java 8.5.2 公开了可以接受布尔类型值的SaveOptions.MergeAreas 属性。默认值为 false，但是，如果设置为 true，则 Aspose.Cells for Java API 会在保存文件之前尝试合并单个 CellArea。

{{% alert color="primary" %}} 

如果电子表格包含太多应用了验证的单个单元格，则生成的电子表格可能会损坏。一种可能的解决方案是合并具有相同验证规则的单元格，或者您现在可以使用 SaveOptions.MergeAreas 属性指示 API 在保存操作之前自动合并 CellAreas。

{{% /alert %}} 
### **添加了属性 Geometry.ShapeAdjustValues**
随着v8.5.2的发布，Aspose.Cells API 已经暴露了Geometry.getShapeAdjustValues方法，可以用来[访问和更改不同形状的调整点](/cells/zh/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

在Microsoft Excel界面中，调整点显示为黄色菱形节点。

{{% /alert %}} 

例如，

1. 圆角矩形有个调整改变圆弧
1. 三角形有一个调整改变点的位置
1. 梯形有个调整可以改变顶部的宽度
1. 箭头有两个调整来改变头部和尾部的形状

这里是最简单的使用场景。

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
### **枚举字段 ConsolidationFunction.DISTINCT_COUNT 添加**
Aspose.Cells for Java 8.5.2 公开了 ConsolidationFunction.DISTINCT_COUNT 字段，可用于在数据透视表的 DataField 上应用 Distinct Count 合并函数。

{{% alert color="primary" %}} 

Microsoft 仅 Excel 2013 支持非重复计数合并功能。

{{% /alert %}}
