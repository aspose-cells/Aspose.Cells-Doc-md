---
title: Aspose.Cells 8.9.0 中的公共 API 更改
type: docs
weight: 300
url: /zh/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本 8.8.3 到 8.9.0 的 Aspose.Cells API 中的更改，可能对模块/应用程序开发人员感兴趣。除了新的和更新的公共方法，添加和删除的类等，还包括任何在 Aspose.Cells 底层行为中的更改的描述。

{{% /alert %}} 
## **已添加API**
### **已添加 HtmlSaveOptions.DefaultFontName 属性**
Aspose.Cells for .NET 8.9.0 已公开 HtmlSaveOptions 类的 DefaultFontName 属性，允许在将电子表格呈现为 HTML 格式时指定默认字体名称。仅当样式的字体不存在时才会使用默认字体。HtmlSaveOptions.DefaultFontName 属性的默认值为 null，这意味着 Aspose.Cells for .NET API 将使用与原始字体相同系列的通用字体。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[设置呈现电子表格为HTML格式的默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to/)上的文章。

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


### **已添加 ImageOrPrintOptions.DefaultFont 属性**
Aspose.Cells for .NET 8.9.0 允许设置 ImageOrPrintOptions 类的默认字体名称，通过公开 DefaultFont 属性。当电子表格中的 Unicode 字符未在单元样式中设置正确的字体时，可以使用该属性，在结果图像中，该类字符可能会显示为块。

{{% alert color="primary" %}} 

将 DefaultFont 属性设置为 MingLiu 或 MS Gothic 以显示 Unicode 字符。如果未设置该属性，则 Aspose.Cells 将使用系统默认字体显示 Unicode 字符。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[设置呈现电子表格为图像格式的默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/)上的文章。

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


### **已添加 PivotTable.IsExcel2003Compatible 属性**
Aspose.Cells for .NET API 已为 PivotTable 类公开了布尔类型的 IsExcel2003Compatible 属性，允许指定 PivotTable 是否为 Excel 2003 兼容以进行刷新目的。IsExcel2003Compatible 属性的默认值为 true，这意味着字符串的长度必须小于或等于 255 个字符。如果字符串大于 255 个字符，它将被截断。如果为 false，则不会施加上述限制。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅[用于 Excel 2003 刷新数据透视表的兼容性](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/)文章。

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


### **已添加 GridWeb.GetVersion 方法**
Aspose.Cells.GridWeb for .NET 8.9.0 已公开返回 GridWeb 组件的发布版本的 GetVersion 工厂方法。
