---
title: Aspose.Cells 8.5.2 中的公共 API 更改
type: docs
weight: 180
url: /zh/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

本文描述了从版本8.5.1到8.5.2的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **将工作表渲染到图形上下文**
这个Aspose.Cells for .NET API的版本公开了SheetRender.ToImage方法的两个新重载，现在允许接受System.Drawing.Graphics类的实例来在图形环境中渲染。新增方法的签名如下。

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


### **新增 PivotTable.GetCellByDisplayName 方法**
Aspose.Cells for .NET 8.5.2公开了PivotTable.GetCellByDisplayName方法，可用于通过PivotField的名称检索Cell对象。此方法在希望突出显示或格式化PivotField标题的情况下非常有用。

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


### **新增 SaveOptions.MergeAreas 属性**
Aspose.Cells for .NET 8.5.2已公开了SaveOptions.MergeAreas属性，可接受布尔类型的值。默认值为false，但如果设置为true，则Aspose.Cells for .NET API将尝试在保存文件之前合并单个CellArea。

{{% alert color="primary" %}} 

如果电子表格具有太多已应用验证的单元格，则可能会造成生成的电子表格损坏。一种可能的解决方案是合并具有相同验证规则的单元格，或者您现在可以使用SaveOptions.MergeAreas属性，指示API在保存操作之前自动合并CellAreas。

{{% /alert %}} 
### **新增 Shape.Geometry.ShapeAdjustValues 属性**
随着v8.5.2的发布，Aspose.Cells API已公开了Shape.Geometry.ShapeAdjustValues属性，可用于更改不同形状的调整点。

{{% alert color="primary" %}} 

在Microsoft Excel界面中，调整点显示为黄色菱形节点。

{{% /alert %}} 

例如，

1. 圆角矩形具有可以更改弧度的调整
1. 三角形具有可更改顶点位置的调整
1. 梯形具有可以更改顶部宽度的调整
1. 箭头具有两个调整，以更改头部和尾部的形状

这里是最简单的使用场景。

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


### **枚举 Field ConsolidationFunction.DistinctCount 已添加**
Aspose.Cells for .NET 8.5.2公开了ConsolidationFunction.DistinctCount字段，可用于在PivotTable的DataField上应用不同计数合并函数。

{{% alert color="primary" %}} 

仅Microsoft Excel 2013支持Distinct Count合并函数。

{{% /alert %}} 
### **GridDesktop更好的事件处理**
Aspose.Cells.GridDesktop的这个版本已公开了4个新事件。其中2个事件在GridDesktop中加载电子表格文件的不同状态时触发，另外2个事件在计算公式时触发。

这些事件列举如下。

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
