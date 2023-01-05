---
title: 公共 API Aspose.Cells 8.5.2 的变化
type: docs
weight: 180
url: /zh/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.1 到 8.5.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-5-2/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **将工作表渲染到图形上下文**
此版本 Aspose.Cells for .NET API 公开了 SheetRender.ToImage 方法的两个新重载，现在允许接受 System.Drawing.Graphics 类的实例以[在图形上下文中渲染](/cells/zh/net/render-worksheet-to-graphic-context/).新增方法的签名如下。

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

以下是简单的使用场景。

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


### **添加了方法 PivotTable.GetCellByDisplayName**
 Aspose.Cells for .NET 8.5.2公开了PivotTable.GetCellByDisplayName方法，可以用来[通过 PivotField 的名称检索 Cell 对象](/cells/zh/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/).在您希望突出显示或格式化 PivotField 标头的情况下，此方法可能很有用。

以下是简单的使用场景。

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


### **添加属性 SaveOptions.MergeAreas**
Aspose.Cells for .NET 8.5.2 公开了可以接受布尔类型值的SaveOptions.MergeAreas 属性。默认值为 false，但是，如果设置为 true，则 Aspose.Cells for .NET API 会在保存文件之前尝试合并单个 CellArea。

{{% alert color="primary" %}} 

如果电子表格包含太多应用了验证的单个单元格，则生成的电子表格可能会损坏。一种可能的解决方案是合并具有相同验证规则的单元格，或者您现在可以使用 SaveOptions.MergeAreas 属性指示 API 在保存操作之前自动合并 CellAreas。

{{% /alert %}} 
### **添加了属性 Shape.Geometry.ShapeAdjustValues**
随着v8.5.2的发布，Aspose.Cells API 已经暴露了Shape.Geometry.ShapeAdjustValues属性，可以用来[改变不同形状的调整点](/cells/zh/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

在Microsoft Excel界面中，调整点显示为黄色菱形节点。

{{% /alert %}} 

例如，

1. 圆角矩形有个调整改变圆弧
1. 三角形有一个调整改变点的位置
1. 梯形有个调整可以改变顶部的宽度
1. 箭头有两个调整来改变头部和尾部的形状

这里是最简单的使用场景。

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


### **添加枚举字段 ConsolidationFunction.DistinctCount**
 Aspose.Cells for .NET 8.5.2暴露了ConsolidationFunction.DistinctCount字段，可用于[应用 Distinct Count 合并函数](/cells/zh/net/consolidation-function/)在数据透视表的数据字段上。

{{% alert color="primary" %}} 

Microsoft 仅 Excel 2013 支持非重复计数合并功能。

{{% /alert %}} 
### **更好的 GridDesktop 事件处理**
本次Aspose.Cells.GridDesktop版本暴露了4个新事件。其中 2 个事件在 GridDesktop 中加载电子表格文件的不同状态时触发，而另外 2 个在计算公式时触发。

事件列表如下。

1. 网格桌面.BeforeLoadFile
1. 网格桌面.FinishLoadFile
1. 网格桌面.BeforeCalculate
1. 网格桌面.FinishCalculate
