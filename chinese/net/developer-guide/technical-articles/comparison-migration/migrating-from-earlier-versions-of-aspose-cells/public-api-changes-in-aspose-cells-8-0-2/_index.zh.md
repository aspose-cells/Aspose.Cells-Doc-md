---
title: 公共 API Aspose.Cells 8.0.2 的变化
type: docs
weight: 30
url: /zh/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.0.1 到 8.0.2 的更改，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **向 Shape 类添加了 TextDirection 属性**
Shape 类公开了 TextDirection 属性，可用于获取或设置 Shape 对象的文本流方向。 TextDirection 属性还可用于为电子表格中的注释设置所需的文本方向，如下所示。

**C#**

{{< highlight "csharp" >}}

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

请查看详细文章[更改注释的文本方向](/cells/zh/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **将 ConvertFormulasData 属性添加到 HTMLLoadOptions 类**
ConvertFormulasData 属性已添加到 HTMLLoadOptions 类，以方便开发人员从 HTML 文件加载 Excel 公式。布尔型 ConvertFormulasData 属性指示当字符串值以字符“=”开头时是否将字符串转换为公式。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasData 属性的默认值为 false。

{{% /alert %}}
## **将 ImageOptions 属性添加到 HtmlSaveOptions 类**
ImageOptions 属性已添加到 HtmlSaveOptions 类。公开 ImageOptions 属性使开发人员能够在导出电子表格时为嵌入在 HTML 中的图像设置首选项。
## **废弃的 HtmlSaveOptions.ExportChartImageFormat 属性**
从 Aspose.Cells for .NET 8.0.2 开始，HtmlSaveOptions.ExportChartImageFormat 已被标记为过时。在将电子表格导出为 HTML 格式时，建议使用 HtmlSaveOptions.ImageOptions 代替图像格式设置。
