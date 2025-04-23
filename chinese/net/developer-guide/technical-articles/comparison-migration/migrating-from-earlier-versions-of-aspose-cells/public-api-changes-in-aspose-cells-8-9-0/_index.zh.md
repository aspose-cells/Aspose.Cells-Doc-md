---
title: Aspose.Cells 8.9.0中的公共API更改
type: docs
weight: 300
url: /zh/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.8.3到8.9.0的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了Aspose.Cells背后的行为变化。

{{% /alert %}} 
## **添加的 API**
### **添加了HtmlSaveOptions.DefaultFontName属性**
Aspose.Cells for .NET 8.9.0已经公开了HtmlSaveOptions类的DefaultFontName属性，允许在将电子表格渲染为HTML格式时指定默认字体名称。仅当样式的字体不存在时，才会使用默认字体。HtmlSaveOptions.DefaultFontName属性的默认值为null，这意味着Aspose.Cells for .NET API将使用与原始字体相同系列的通用字体。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[设置呈现电子表格为HTML格式时的默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **添加了ImageOrPrintOptions.DefaultFont属性**
Aspose.Cells for .NET 8.9.0允许为ImageOrPrintOptions类设置默认字体名称，通过公开DefaultFont属性。当电子表格中的Unicode字符没有在单元格样式中正确设置字体时，可以使用该属性。因此，在结果图片中这些字符可能出现为方块。

{{% alert color="primary" %}} 

将DefaultFont属性设置为MingLiu或MS Gothic以显示Unicode字符。如果未设置该属性，Aspose.Cells将使用系统的默认字体显示Unicode字符。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[在图像格式下设置呈现电子表格的默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **添加了PivotTable.IsExcel2003Compatible属性**
Aspose.Cells for .NET API已公开了PivotTable类的Boolean类型IsExcel2003Compatible属性，用于指定适用于刷新目的的PivotTable是否与Excel 2003兼容。IsExcel2003Compatible属性的默认值为true，这意味着字符串的长度必须小于或等于255个字符。如果字符串大于255个字符，将被截断。如果为false，则不会施加上述限制。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[刷新数据透视表时对 Excel 2003 的兼容性](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/) 的文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **添加了 GridWeb.GetVersion 方法**
Aspose.Cells.GridWeb for .NET 8.9.0 已公开了 {GetVersion}} 工厂方法，用于返回 GridWeb 组件的发布版本。
{{< app/cells/assistant language="csharp" >}}
