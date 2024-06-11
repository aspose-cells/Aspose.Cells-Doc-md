---
title: Aspose.Cells 8.0.2中的公共API变更
type: docs
weight: 30
url: /zh/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

这份文档描述了从版本8.0.1到8.0.2的Aspose.Cells API的变更，这些变更可能会对模块/应用程序开发人员感兴趣。其中包括不仅有新的和更新的公共方法，还描述了在Aspose.Cells背后的行为中的任何变化的说明。

{{% /alert %}} 
## **在Shape类中添加了TextDirection属性**
Shape类已公开了TextDirection属性，用于获取或设置Shape对象的文本流方向。TextDirection属性也可用于设置电子表格中注释的所需文本方向，如下所示。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看关于[更改注释的文本方向](/cells/zh/net/change-text-direction-of-the-comment/)的详细文章

{{% /alert %}}
## **已添加ConvertFormulasData属性到HTMLLoadOptions类**
已添加ConvertFormulasData属性到HTMLLoadOptions类，以方便开发人员从HTML文件加载Excel公式。布尔型ConvertFormulasData属性指示当字符串值以'='字符开头时，是否将其转换为公式。

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

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
