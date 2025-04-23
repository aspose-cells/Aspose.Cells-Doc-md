---
title: Aspose.Cells 8.1.0中的公共API更改
type: docs
weight: 40
url: /zh/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.0.2到8.1.0的Aspose.Cells API更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells背后的任何行为更改。

{{% /alert %}} 
## **已添加HtmlSaveOptions.ExportHiddenWorksheet属性**
HtmlSaveOptions类已公开ExportHiddenWorksheet属性，可用于指定是否导出隐藏工作表到HTML格式。默认值为true。如果设置为false，Aspose.Cells将不会导出隐藏的工作表内容。

{{% alert color="primary" %}} 

请查看[阻止导出隐藏工作表的详细文章](/cells/zh/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **已添加Cell.StringValueWithoutFormat属性**
已添加StringValueWithoutFormat属性到Cell类，以便开发人员在没有应用任何格式的情况下检索单元格值。

下面提供的代码片段演示了使用 Cell.StringValueWithoutFormat 属性与创建电子表格并将数字格式应用于其中一个单元格的 cell.DisplayStringValue 的用法对比。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

上述代码的输出如下

123,456

123456

{{% /alert %}}
## **已废弃Bytes、Characters、CharactersWithSpaces、Lines、Paragraphs属性**
从Aspose.Cells for .NET 8.1.0开始，BuiltInDocumentPropertyCollection类中的许多属性已被标记为过时。这些属性包括Bytes，Characters，CharactersWithSpaces，Lines和Paragraphs。原因是这些属性在保留Excel电子表格时没有用处，因为Excel会省略它们。而这些属性最初是为Word文档和PowerPoint演示文稿编写的。
{{< app/cells/assistant language="csharp" >}}
