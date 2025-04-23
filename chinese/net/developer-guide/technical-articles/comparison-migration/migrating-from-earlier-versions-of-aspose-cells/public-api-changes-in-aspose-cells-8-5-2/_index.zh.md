---
title: Aspose.Cells 8.5.2中的公共API更改
type: docs
weight: 180
url: /zh/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

本文描述了Aspose.Cells API从版本8.5.1到8.5.2的更改，这些更改可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、[新增的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-5-2/)，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **添加的 API**
### **将工作表渲染到图形上下文**
此版本的Aspose.Cells for .NET API已公开了SheetRender.ToImage方法的两个新重载，现在可以接受System.Drawing.Graphics类的实例以在[图形上下文中渲染](/cells/zh/net/render-worksheet-to-graphic-context/)。新增方法的签名如下。

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

以下是简单的使用场景。

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


### **新增了 PivotTable.GetCellByDisplayName 方法**
Aspose.Cells for .NET 8.5.2已公开了PivotTable.GetCellByDisplayName方法，可用于[按PivotField的名称检索Cell对象](/cells/zh/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/)。该方法在希望突出显示或格式化PivotField标题的场景中可能很有用。

以下是简单的使用场景。

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


### **添加了SaveOptions.MergeAreas属性**
Aspose.Cells for .NET 8.5.2已公开了SaveOptions.MergeAreas属性，可以接受布尔类型的值。默认值为false，但如果设置为true，则Aspose.Cells API会尝试在保存文件之前合并各个CellArea。

{{% alert color="primary" %}} 

如果电子表格有太多应用了验证的个别单元格，导致最终的电子表格可能会损坏。一个可能的解决方案是合并具有相同验证规则的单元格，或者您现在可以使用SaveOptions.MergeAreas属性来指示API在保存操作之前自动合并CellAreas。

{{% /alert %}} 
### **新增了 Shape.Geometry.ShapeAdjustValues 属性**
随着 v8.5.2 的发布，Aspose.Cells API 已公开了 Shape.Geometry.ShapeAdjustValues 属性，可用于[更改不同形状的调整点](/cells/zh/net/change-adjustment-values-of-the-shape/)。

{{% alert color="primary" %}} 

在 Microsoft Excel 界面中，调整点显示为黄色菱形节点。

{{% /alert %}} 

例如，

1. 圆角矩形具有用于更改弧度的调整
1. 三角形具有用于更改点位置的调整
1. 梯形具有用于更改顶部宽度的调整
1. 箭头具有用于更改头部和尾部形状的两个调整

这是最简单的使用场景。

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


### **新增了枚举字段 ConsolidationFunction.DistinctCount**
Aspose.Cells for .NET 8.5.2已公开了ConsolidationFunction.DistinctCount字段，可用于[应用不同计数合并函数](/cells/zh/net/consolidation-function/)于PivotTable的DataField上。

{{% alert color="primary" %}} 

仅Microsoft Excel 2013支持Distinct Count统计函数。

{{% /alert %}} 
### **GridDesktop 更好地处理事件**
Aspose.Cells.GridDesktop 的此版本暴露了 4 个新事件。其中 2 个事件在 GridDesktop 中加载电子表格文件的不同状态时触发，而另外 2 个事件在公式计算时触发。

以下是事件列表。

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
{{< app/cells/assistant language="csharp" >}}
