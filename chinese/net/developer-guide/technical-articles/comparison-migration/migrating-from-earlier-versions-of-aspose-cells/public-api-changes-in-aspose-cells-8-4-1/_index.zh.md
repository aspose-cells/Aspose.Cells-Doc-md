---
title: 公共 API Aspose.Cells 8.4.1 的变化
type: docs
weight: 140
url: /zh/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.4.0 到 8.4.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-1/)和[删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-1/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **修改数据库连接的机制**
Aspose.Cells.ExternalConnections.ExternalConnection 类已包含可用于检查存储在电子表格中的数据库连接详细信息的方法和属性。在 Aspose.Cells for .NET 8.4.1 发布之前，与 Aspose.Cells.ExternalConnections.ExternalConnection 类关联的大部分属性都是只读的。在此版本中，API 也提供了对操作数据库连接设置的支持。

以下代码片段显示了如何动态修改数据库连接设置。

**C#**

{{< highlight "csharp" >}}

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



以下是 {Aspose.Cells.ExternalConnections.ExternalConnection}} 类公开的一些最重要的属性。

|**物业名称**|**描述**|
|:- |:- |
|后台刷新|指示是否可以在后台（异步）刷新连接。<br>如果连接的首选用法是在后台异步刷新，则为真；<br>如果连接的首选用法是在前台同步刷新，则为 false。|
|连接说明|指定此连接的用户描述|
|连接ID|指定此连接的唯一标识符。|
|证书|指定建立（或重新建立）连接时要使用的身份验证方法。|
|已删除|指示关联的工作簿连接是否已删除。如果<br>连接已被删除；否则，假的。|
|是新的|如果第一次没有刷新连接则为真；否则，假的。这个<br>当用户在查询完成返回之前保存文件时，可能会出现这种状态。|
|活着|当电子表格应用程序应努力保持连接时为真<br>打开。为 false 时，应用程序应在检索到<br>信息。|
|姓名|指定连接的名称。每个连接都必须有一个唯一的名称。|
|Odc文件|指定此连接来自的外部连接文件的完整路径<br>创建。如果在尝试刷新数据时连接失败，并且 reconnectionMethod=1，<br>然后电子表格应用程序将使用来自外部连接文件的信息重试<br>而不是工作簿中嵌入的连接对象。|
|仅使用连接文件|指示电子表格应用程序是否应始终且仅使用<br>odcFile 属性指示的外部连接文件中的连接信息<br>刷新连接时。如果为假，则电子表格应用程序<br>应遵循 reconnectionMethod 属性指示的过程|
|参数|获取 ODBC 或 Web 查询的 ConnectionParameterCollection。|
|重新连接方法|指定 reconnectionMethod 类型|
|刷新内部|指定连接自动刷新之间的分钟数。|
|加载时刷新|如果在打开文件时应刷新此连接，则为真；否则为真。否则，假的。|
|保存数据|如果要保存通过连接获取的用于填充表的外部数据，则为真<br>与工作簿；否则，假的。|
|保存密码|如果要将密码保存为连接字符串的一部分，则为真；否则为真。否则，假。|
|源文件|当外部数据源是基于文件的时使用。当连接到这样的数据时<br>source 失败，电子表格应用程序尝试直接连接到该文件。也许<br>以 URI 或系统特定的文件路径表示法表示。|
|SSOId|用于中间体之间身份验证的单点登录 (SSO) 标识符<br>spreadsheetML 服务器和外部数据源。|
|类型|指定数据源类型。|

### **能够格式化 DataLabels 文本的子字符串**
Aspose.Cells for .NET 8.4.1 公开了 DataLabels.Characters 方法以检索对应于 ChartPoints.DataLabels 的子字符串的 FontSetting 类的实例。反过来，FontSetting 类的实例可用于格式化具有不同字体设置和颜色的 DataLabels 的子字符串。

以下代码片段显示了如何使用 DataLabels.Characters 方法。

**C#**

{{< highlight "csharp" >}}

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


### **能够为电子表格和图表导出设置所需的图像尺寸**
Aspose.Cells for .NET 8.4.1 公开了 ImageOrPrintOptions.SetDesiredSize 方法以在将电子表格和图表导出到图像时设置结果图像的尺寸。 ImageOrPrintOptions.SetDesiredSize 方法接受两个整数类型参数，其中第一个是所需的宽度，第二个是所需的高度。

以下代码片段显示了如何在将工作表导出到 PNG 时设置所需的尺寸。

**C#**

{{< highlight "csharp" >}}

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

相同的属性也可用于将图表转换为图像。

{{% /alert %}} 


### **将评论呈现给 PDF**
随着v8.4.1的发布，Aspose.Cells API 提供了PageSetup.PrintComments属性& PrintCommentsType枚举，以便在将电子表格转换为PDF格式时方便注释的呈现。 PrintCommentsType 枚举具有以下常量。

- PrintCommentsType.PrintNoComments：不呈现评论。
- PrintCommentsType.PrintInPlace：注释将在放置它们的地方呈现。
- PrintCommentsType.PrintSheetEnd：注释将在工作表末尾呈现。

以下示例代码演示了如何使用 PageSetup.PrintComments 属性来使用所有可能的 PrintCommentsType 枚举值呈现注释。

**C#**

{{< highlight "csharp" >}}

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


### **在 Aspose.Cells.GridDesktop 中移动工作表**
Aspose.Cells.GridDesktop 提供WorksheetCollection.MoveTo 方法，可用于将工作表移动到指定索引。上述方法以源工作表和目标工作表的索引（从零开始）为参数。

以下示例代码演示了 WorksheetCollection.MoveTo 属性的用法。

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **添加了 Workbook.IsLicensed 属性**
Aspose.Cells for .NET 8.4.1 公开了 Workbook.IsLicensed，这对确定许可证是否已成功加载有很大帮助。如果您在设置许可证之前访问此属性，它将返回 false，反之亦然，但是，许可证应该是有效的。

以下示例代码演示了 Workbook.IsLicensed 属性的用法。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 ImageOrPrintOptions.SVGFitToViewPort 属性**
Aspose.Cells for .NET 8.4.1 公开了 ImageOrPrintOptions 类的 SVGFitToViewPort 属性，可用于在将电子表格或图表导出为 SVG 格式时打开 SVG 文件格式的 viewBox 属性。此属性的默认值为 false，因此在未设置上述属性的情况下生成的 SVG 文件的基本 XML 将不包含 viewBox 属性。

以下示例代码演示了 ImageOrPrintOptions.SVGFitToViewPort 属性的用法。

**C#**

{{< highlight "csharp" >}}

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
## **废弃的 API**
### **方法 Workbook.ValidateFormula 已废弃**
使用 Cell.Formula 方法验证公式。
