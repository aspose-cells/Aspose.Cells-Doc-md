---
title: Aspose.Cells 8.4.1中的公共API更改
type: docs
weight: 140
url: /zh/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.4.0到8.4.1的Aspose.Cells API的更改，这对模块/应用程序开发人员可能很有用。它不仅包括新的和更新的公共方法，[添加的类等。](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-1/)和[删除的类等。](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-1/)，还描述了Aspose.Cells后台行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **修改数据库连接的机制**
Aspose.Cells.ExternalConnections.ExternalConnection类已经包含了用于检查存储在电子表格中的数据库连接详细信息的方法和属性。直到发布Aspose.Cells for .NET 8.4.1之前，与Aspose.Cells.ExternalConnections.ExternalConnection类相关的大多数属性都是只读的。通过此发布，API已提供了支持以操纵数据库连接设置。

以下代码片段显示了如何动态修改数据库连接设置。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



这里是{Aspose.Cells.ExternalConnections.ExternalConnection}类公开的一些最重要的属性。

|**属性名称**|**描述**|
| :- | :- |
|BackgroundRefresh|指示连接是否可以在后台进行刷新（异步）。<br>true表示首选使用异步后台刷新连接；<br>false表示首选使用同步前台刷新连接。|
|连接描述|指定此连接的用户描述|
|连接标识符|指定此连接的唯一标识符|
|凭据|指定建立（或重新建立）连接时要使用的身份验证方法|
|已删除|指示关联工作簿连接是否已被删除。如果连接已被删除，则为 true；否则为 false。|
|是否为新连接|如果未为此连接刷新数据首次，为 true；否则为 false。当用户在查询完成返回之前保存文件时，可能会出现这种状态。|
|保持连接|如果电子表格应用程序应该尽力保持连接打开时为 true。当为 false 时，应用程序应在检索信息后关闭连接。|
|名称|指定连接的名称。每个连接必须有一个唯一的名称。|
|Odc文件|指定此连接创建时来自的外部连接文件的完整路径。如果在尝试刷新数据时连接失败，并且 reconnectionMethod=1，则电子表格应用程序将尝试再次使用外部连接文件中的信息，而不是工作簿中嵌入的连接对象。|
|仅使用连接文件|指示电子表格应用程序在刷新连接时是否始终且仅使用由 odcFile 属性指示的外部连接文件中的连接信息。如果为 false，则电子表格应用程序应按照 reconnectionMethod 属性指示的程序进行操作。|
|参数|获取用于 ODBC 或网络查询的 ConnectionParameterCollection。|
|重新连接方法|指定重新连接方法类型|
|RefreshInternal|指定连接自动刷新之间的分钟数。|
|打开时刷新|如果在打开文件时应刷新此连接为 true；否则为 false。|
|保存数据|如果通过连接获取的外部数据用于填充表格需要保存到工作簿中为 true；否则为 false。|
|保存密码|如果密码应作为连接字符串的一部分保存为 true；否则为 false。|
|源文件|当外部数据源是基于文件时使用。当连接到这样的数据源失败时，电子表格应用程序尝试直接连接到此文件。可能以 URI 或特定于系统的文件路径表示。|
|SSOId|用于身份验证的单点登录（SSO）标识符，用于中介电子表格ML服务器与外部数据源之间的身份验证。|
|类型|指定数据源类型。|

### **格式化数据标签文本的子字符串的能力**
Aspose.Cells for .NET 8.4.1已为DataLabels.Characters方法公开了支持，以检索与ChartPoints.DataLabels的子字符串对应的FontSetting类的实例。然后，FontSetting类的实例可用于使用不同字体设置和颜色格式化DataLabels的子字符串。

以下代码片段显示了如何使用DataLabels.Characters方法。

**C#**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **设置电子表格和图表导出的所需图像尺寸的能力**
Aspose.Cells for .NET 8.4.1已公开了ImageOrPrintOptions.SetDesiredSize方法，以设置导出电子表格和图表为图像时的结果图像尺寸。ImageOrPrintOptions.SetDesiredSize方法接受两个整数类型参数，第一个是期望的宽度，第二个是期望的高度。

以下代码段显示了如何导出工作表到PNG时设置所需尺寸。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

相同的属性也可以用于将图表转换为图像。

{{% /alert %}} 


### **将评论渲染为PDF**
随着V8.4.1的发布，Aspose.Cells API提供了PageSetup.PrintComments属性和PrintCommentsType枚举，以便在将电子表格转换为PDF格式时方便渲染评论。PrintCommentsType枚举有以下常量。

- PrintCommentsType.PrintNoComments：不呈现注释。
- PrintCommentsType.PrintInPlace：将注释呈现在其放置的位置。
- PrintCommentsType.PrintSheetEnd：将注释呈现在工作表的末尾。

以下示例代码演示了使用PageSetup.PrintComments属性以使用所有可能的PrintCommentsType枚举值来渲染注释。

**C#**

{{< highlight csharp >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **在Aspose.Cells.GridDesktop中移动工作表**
Aspose.Cells.GridDesktop提供了WorksheetCollection.MoveTo方法，该方法可用于将工作表移动到指定的索引。上述方法参数为源工作表和目标工作表的索引（从零开始）。

以下示例代码演示了如何使用WorksheetCollection.MoveTo属性。

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **添加了Workbook.IsLicensed属性**
Aspose.Cells for .NET 8.4.1已公开了Workbook.IsLicensed属性，可以很好地帮助确定是否已成功加载许可证。如果在设置许可证之前访问此属性，它将返回false，反之亦然，但许可证应有效。

以下示例代码演示了使用Workbook.IsLicensed属性。

**C#**

{{< highlight csharp >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **添加了ImageOrPrintOptions.SVGFitToViewPort属性**
Aspose.Cells for .NET 8.4.1已为ImageOrPrintOptions类公开了SVGFitToViewPort属性，可用于在将电子表格或图表导出为SVG格式时打开viewBox属性。该属性的默认值为false，因此如果未设置上述属性，则生成的SVG文件的基本XML将不包括viewBox属性。

以下示例代码展示了使用ImageOrPrintOptions.SVGFitToViewPort属性的用法。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **弃用的API**
### **已过时的Workbook.ValidateFormula方法**
使用Cell.Formula方法验证公式。
