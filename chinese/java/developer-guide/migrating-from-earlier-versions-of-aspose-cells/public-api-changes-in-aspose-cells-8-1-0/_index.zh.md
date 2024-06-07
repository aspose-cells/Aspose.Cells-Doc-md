---
title: Aspose.Cells 8.1.0 中的公共 API 更改
type: docs
weight: 50
url: /zh/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.0.2到8.1.0的Aspose.Cells API的更改，这可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加了HtmlSaveOptions.ExportHiddenWorksheet属性**
HtmlSaveOptions类已公开ExportHiddenWorksheet属性，该属性用于指定是否将隐藏的工作表导出为HTML格式。默认值为true。如果设置为false，则Aspose.Cells将不导出隐藏的工作表内容。

{{% alert color="primary" %}} 

请查看有关[防止导出隐藏工作表](/cells/zh/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)的详细文章。

{{% /alert %}}
## **添加了Cell.StringValueWithoutFormat属性**
StringValueWithoutFormat属性已添加到Cell类，以便开发人员可以检索未应用任何格式的单元格值。 

下面提供的代码片段演示了使用 Cell.getStringValueWithoutFormat 方法与 cell.getDisplayStringValue 相比，通过从头开始创建电子表格并将一些单元格应用数格式，可以获得更高级的字符串值。 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

上述代码的输出如下

格式化的字符串值：123,456
未格式化的字符串值：123456

{{% /alert %}}
## **弃用Bytes，Characters，CharactersWithSpaces，Lines，Paragraphs属性**
从Aspose.Cells for .NET 8.1.0开始，BuiltInDocumentPropertyCollection类中的许多属性已被标记为过时。这些属性包括Bytes，Characters，CharactersWithSpaces，Lines和Paragraphs。原因是，上述属性对于保护Excel电子表格没有用处，因为Excel会忽略它们。而这些属性最初是为Word文档和PowerPoint演示文稿编写的。 
