---
title: Aspose.Cells 8.0.2中的公共API变更
type: docs
weight: 40
url: /zh/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

这份文档描述了从版本8.0.1到8.0.2的Aspose.Cells API的变更，这些变更可能会对模块/应用程序开发人员感兴趣。其中包括不仅有新的和更新的公共方法，还描述了在Aspose.Cells背后的行为中的任何变化的说明。

{{% /alert %}} 
## **在Shape类中添加了TextDirection属性**
Shape类已公开了TextDirection属性，用于获取或设置Shape对象的文本流方向。TextDirection属性也可用于设置电子表格中注释的所需文本方向，如下所示。

Java

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
## **已添加ConvertFormulasData属性到HTMLLoadOptions类**
已添加ConvertFormulasData属性到HTMLLoadOptions类，以方便开发人员从HTML文件加载Excel公式。布尔型ConvertFormulasData属性指示当字符串值以'='字符开头时，是否将其转换为公式。

Java

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

ConvertFormulasData属性的默认值为false。

{{% /alert %}}
## **已添加ImageOptions属性到HtmlSaveOptions类**
已添加ImageOptions属性到HtmlSaveOptions类。公开ImageOptions属性使开发人员能够设置导出电子表格到HTML时嵌入图像的偏好设置。 
## **已废弃HtmlSaveOptions.ExportChartImageFormat属性**
从Aspose.Cells for .NET 8.0.2开始，HtmlSaveOptions.ExportChartImageFormat已被标记为过时。建议在将电子表格导出为HTML格式时使用HtmlSaveOptions.ImageOptions进行图像格式设置。
