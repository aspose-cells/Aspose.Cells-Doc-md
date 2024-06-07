---
title: Aspose.Cells 8.0.2 中的公共 API 更改
type: docs
weight: 40
url: /zh/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

本文描述了从版本 8.0.1 到 8.0.2 的 Aspose.Cells API 更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还包括任何可能影响 Aspose.Cells 幕后行为的更改描述。

{{% /alert %}} 
## **向 Shape 类添加了 TextDirection 属性**
Shape 类已公开 TextDirection 属性，用于获取或设置形状对象的文本流方向。TextDirection 属性还可用于为电子表格中的注释设置所需的文本方向，如下所示。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **向 HTMLLoadOptions 类添加了 ConvertFormulasData 属性**
已向 HTMLLoadOptions 类添加了 ConvertFormulasData 属性，以便开发人员从 HTML 文件加载 Excel 公式。布尔型 ConvertFormulasData 属性指示是否在字符串值以字符 '=' 开头时将其转换为公式。

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasData 属性的默认值为 false。

{{% /alert %}}
## **向 HtmlSaveOptions 类添加了 ImageOptions 属性**
已向 HtmlSaveOptions 类添加了 ImageOptions 属性。公开 ImageOptions 属性使开发人员能够设置导出电子表格时嵌入在 HTML 中的图像的首选项。 
## **标记为过时的 HtmlSaveOptions.ExportChartImageFormat 属性**
自 Aspose.Cells for .NET 8.0.2 起，HtmlSaveOptions.ExportChartImageFormat 已经被标记为过时。建议在将电子表格导出为 HTML 格式时使用 HtmlSaveOptions.ImageOptions 来设置图像格式设置。
