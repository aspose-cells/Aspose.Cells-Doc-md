---
title: Aspose.Cells 8.1.0 中的公共 API 更改
type: docs
weight: 40
url: /zh/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.0.2到8.1.0的Aspose.Cells API的更改，这可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加了HtmlSaveOptions.ExportHiddenWorksheet属性**
HtmlSaveOptions类已公开ExportHiddenWorksheet属性，该属性用于指定是否将隐藏的工作表导出为HTML格式。默认值为true。如果设置为false，则Aspose.Cells将不导出隐藏的工作表内容。

{{% alert color="primary" %}} 

请查阅有关[在保存时阻止导出隐藏工作表内容的详细文章](/cells/zh/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **添加了Cell.StringValueWithoutFormat属性**
StringValueWithoutFormat属性已添加到Cell类，以便开发人员可以检索未应用任何格式的单元格值。

以下提供的代码片段演示了使用Cell.StringValueWithoutFormat属性与通过从头开始创建电子表格并将数字格式应用于其中一个单元格来比较单元格.DisplayStringValue的用法。

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
## **弃用Bytes，Characters，CharactersWithSpaces，Lines，Paragraphs属性**
从Aspose.Cells for .NET 8.1.0开始，BuiltInDocumentPropertyCollection类中的许多属性已被标记为过时。这些属性包括Bytes，Characters，CharactersWithSpaces，Lines和Paragraphs。原因是，上述属性对于保护Excel电子表格没有用处，因为Excel会忽略它们。而这些属性最初是为Word文档和PowerPoint演示文稿编写的。
