---
title: 公共 API Aspose.Cells 8.9.0 的变化
type: docs
weight: 300
url: /zh/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.8.3 到 8.9.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 HtmlSaveOptions.DefaultFontName 属性**
Aspose.Cells for .NET 8.9.0 公开了 HtmlSaveOptions 类的 DefaultFontName 属性，允许在将电子表格呈现为 HTML 格式时指定默认字体名称。只有当样式字体不存在时，才会使用默认字体。 HtmlSaveOptions.DefaultFontName 属性的默认值为 null，即 Aspose.Cells for .NET API 将使用与原始字体同族的通用字体。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关的文章[将呈现电子表格的默认字体设置为 HTML 格式](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **添加了 ImageOrPrintOptions.DefaultFont 属性**
Aspose.Cells for .NET 8.9.0 允许通过公开 DefaultFont 属性为 ImageOrPrintOptions 类设置默认字体名称。当电子表格中的 Unicode 字符未在单元格样式中设置正确的字体时，可以使用上述属性，因此此类字符可能在结果图像中显示为块。

{{% alert color="primary" %}} 

将 DefaultFont 属性设置为 MingLiu 或 MS Gothic 以显示 Unicode 字符。如果不设置该属性，Aspose.Cells将使用系统默认字体显示Unicode字符。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关的文章[为以图像格式呈现电子表格设置默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 PivotTable.IsExcel2003Compatible 属性**
Aspose.Cells for .NET API 公开了数据透视表类的布尔类型 IsExcel2003Compatible 属性，它允许指定数据透视表是否与 Excel 2003 兼容以用于刷新目的。 IsExcel2003Compatible 属性的默认值为 true，这意味着字符串必须小于或等于 255 个字符。如果字符串大于 255 个字符，它将被截断。如为虚假，则不会受到上述限制。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关的文章[刷新数据透视表的 Excel 2003 兼容性](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET 8.9.0 公开了 {GetVersion}} 工厂方法，该方法返回 GridWeb 组件的发布版本。
