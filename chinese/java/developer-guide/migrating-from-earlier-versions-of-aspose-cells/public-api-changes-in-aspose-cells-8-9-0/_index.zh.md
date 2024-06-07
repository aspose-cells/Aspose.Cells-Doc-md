---
title: Aspose.Cells 8.9.0 中的公共 API 更改
type: docs
weight: 310
url: /zh/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本 8.8.3 到 8.9.0 的 Aspose.Cells API 中的更改，可能对模块/应用程序开发人员感兴趣。除了新的和更新的公共方法，添加和删除的类等，还包括任何在 Aspose.Cells 底层行为中的更改的描述。

{{% /alert %}} 
## **已添加API**
### **已添加 HtmlSaveOptions.DefaultFontName 属性**
Aspose.Cells for Java 8.9.0 已为 HtmlSaveOptions 类公开了 DefaultFontName 属性，允许在将电子表格呈现为 HTML 格式时指定默认字体名称。仅当样式的字体不存在时，才会使用默认字体。HtmlSaveOptions.DefaultFontName 属性的默认值为 null，这意味着 Aspose.Cells for Java API 将使用具有与原始字体相同系列的通用字体。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[在将电子表格呈现为 HTML 格式时设置默认字体](/cells/zh/java/set-default-font-while-rendering-spreadsheet-to/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **已添加 ImageOrPrintOptions.DefaultFont 属性**
Aspose.Cells for Java 8.9.0 允许为 ImageOrPrintOptions 类设置默认字体名称，通过公开 DefaultFont 属性。当电子表格中的 Unicode 字符没有在单元格样式中正确设置字体时，可以使用该属性。因此，这些字符在生成的图像中可能会显示为块。 

{{% alert color="primary" %}} 

将 DefaultFont 属性设置为 MingLiu 或 MS Gothic 以显示 Unicode 字符。如果未设置该属性，则 Aspose.Cells 将使用系统默认字体显示 Unicode 字符。 

{{% /alert %}} {{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[在图像格式中呈现电子表格时设置默认字体](/cells/zh/java/set-default-font-while-rendering-spreadsheet-to-images/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **新增 PivotTable.Excel2003Compatible 属性**
Aspose.Cells for Java API 为 PivotTable 类公开了布尔类型 Excel2003Compatible 属性，允许指定用于刷新目的的 PivotTable 是否与 Excel 2003 兼容。Excel2003Compatible 属性的默认值为 true，这意味着字符串长度必须小于或等于 255 个字符。如果字符串长度大于 255 个字符，则会被截断。如果为 false，则不会施加上述限制。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[用于 Excel 2003 刷新数据透视表时的兼容性](/cells/zh/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
