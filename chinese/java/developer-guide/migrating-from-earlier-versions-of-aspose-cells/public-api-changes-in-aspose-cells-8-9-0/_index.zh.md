---
title: Aspose.Cells 8.9.0中的公共API更改
type: docs
weight: 310
url: /zh/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.8.3到8.9.0的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了Aspose.Cells背后的行为变化。

{{% /alert %}} 
## **添加的 API**
### **添加了HtmlSaveOptions.DefaultFontName属性**
Aspose.Cells for Java 8.9.0版本已暴露了HtmlSaveOptions类的DefaultFontName属性，允许在将电子表格渲染为HTML格式时指定默认字体名称。默认字体仅在样式的字体不存在时使用。HtmlSaveOptions.DefaultFontName属性的默认值为null，这意味着Aspose.Cells for Java API将使用与原始字体相同系列的通用字体。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查阅[将电子表格渲染为HTML格式时设置默认字体](/cells/zh/java/set-default-font-while-rendering-spreadsheet-to/)的文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

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
### **添加了ImageOrPrintOptions.DefaultFont属性**
Aspose.Cells for Java 8.9.0版本允许通过暴露DefaultFont属性为ImageOrPrintOptions类设置默认字体名称。当电子表格中的Unicode字符在单元格样式中未正确设置字体时，可以使用该属性。因此，这些字符在生成的图像中可能显示为块。 

{{% alert color="primary" %}} 

将DefaultFont属性设置为MingLiu或MS Gothic以显示Unicode字符。如果未设置该属性，Aspose.Cells将使用系统的默认字体显示Unicode字符。 

{{% /alert %}} {{% alert color="primary" %}} 

要了解更多有关此功能的详细信息，请查看 [在图像格式中设置渲染电子表格的默认字体](/cells/zh/java/set-default-font-while-rendering-spreadsheet-to-images/) 文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

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
### **添加了 PivotTable.Excel2003Compatible 属性**
Aspose.Cells for Java API已为PivotTable类暴露了布尔类型的Excel2003Compatible属性，允许指定PivotTable是否为Excel 2003兼容以进行刷新。Excel2003Compatible属性的默认值为true，这意味着字符串必须小于或等于255个字符。如果字符串大于255个字符，则它将被截断。如果为false，则不会施加上述限制。

{{% alert color="primary" %}} 

要了解更多有关此功能的详细信息，请查看 [Excel 2003 刷新数据透视表的兼容性](/cells/zh/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/) 文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

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
