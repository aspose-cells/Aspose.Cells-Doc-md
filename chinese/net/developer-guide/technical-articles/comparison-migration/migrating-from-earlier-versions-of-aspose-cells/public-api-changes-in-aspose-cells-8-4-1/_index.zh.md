---
title: Aspose.Cells 8.4.1 中的公共 API 更改
type: docs
weight: 140
url: /zh/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

本文描述了从版本8.4.0到8.4.1的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **修改数据库连接的机制**
Aspose.Cells.ExternalConnections.ExternalConnection 类已包含了可用于检查电子表格中存储的数据库连接详细信息的方法和属性。直到 Aspose.Cells for .NET 8.4.1 发布之前，大多数与 Aspose.Cells.ExternalConnections.ExternalConnection 类相关的属性都是只读的。随着此版本的发布，API 提供了支持以操纵数据库连接设置。

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



以下是{Aspose.Cells.ExternalConnections.ExternalConnection}}类暴露的一些最重要的属性。

|**属性名称**|**描述**|
| :- | :- |
|BackgroundRefresh|指示连接是否可以在后台（异步方式）刷新。 <br>true 表示首选使用连接是在后台异步刷新； <br>false 表示首选使用连接是在前台同步刷新。|
|ConnectionDescription|指定此连接的用户描述|
|ConnectionId|指定此连接的唯一标识符。|
|Credentials|指定建立（或重新建立）连接时要使用的身份验证方法。|
|IsDeleted|指示关联的工作簿连接是否已被删除。true 表示连接已被删除；否则为 false。|
|IsNew|如果连接尚未第一次刷新，则为 True；否则为 false。当用户在查询完成返回前保存文件时，可能出现此状态。|
|KeepAlive|当电子表格应用程序应保持连接打开时为 True。当为 false 时，应用程序在检索信息后关闭连接。|
|Name|指定连接的名称。每个连接必须具有唯一名称。|
|OdcFile|指定从中创建此连接的外部连接文件的完整路径。如果在尝试刷新数据时连接失败，并且 reconnectionMethod=1，则电子表格应用程序将尝试使用外部连接文件中的信息再次连接，而不是使用嵌入在工作簿中的连接对象。|
|OnlyUseConnectionFile|指示电子表格应用程序是否始终且仅使用由 odcFile 属性指示的外部连接文件中的连接信息在刷新连接时。如果为 false，电子表格应用程序应遵循重新连接方法属性所指示的过程。|
|Parameters|获取ODBC或Web查询的ConnectionParameterCollection。|
|ReConnectionMethod|指定重新连接的方法类型。|
|RefreshInternal|指定连接自动刷新之间的分钟数.|
|RefreshOnLoad|如果打开文件时应刷新此连接，则为True；否则为False。|
|SaveData|如果通过连接获取的外部数据用于填充表格应随工作簿一起保存，则为 true；否则为 false。|
|SavePassword|如果密码应作为连接字符串的一部分保存，则为True；否则为False。|
|SourceFile|当外部数据源为基于文件时使用。当连接到此类数据源失败时，电子表格应用程序将尝试直接连接到此文件。可以表达为 URI 或特定于系统的文件路径表示法。|
|SSOId|用于中间的密码表服务器和外部数据源之间认证的单点登录(SSO)标识符.|
|Type|指定数据源类型。|

### **能够格式化数据标签文本的子字符串**
Aspose.Cells for .NET 8.4.1已公开了DataLabels.Characters方法，用于检索与ChartPoints.DataLabels的子字符串对应的FontSetting类的实例。反过来，FontSetting类的实例可用于使用不同的字体设置和颜色格式化DataLabels的子字符串。

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


### **在电子表格和图表导出中设置所需的图像尺寸**
Aspose.Cells for .NET 8.4.1已公开了ImageOrPrintOptions.SetDesiredSize方法，用于在将电子表格和图表导出为图像时设置结果图像的尺寸。ImageOrPrintOptions.SetDesiredSize方法接受两个整数类型参数，第一个是期望的宽度，第二个是期望的高度。

以下代码段显示了如何在将工作表导出为PNG时设置所需的尺寸。

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

同样的属性也可以用于将图表转换为图像。

{{% /alert %}} 


### **将评论渲染为PDF**
随着v8.4.1的发布，Aspose.Cells API提供了PageSetup.PrintComments属性和PrintCommentsType枚举，以便在将电子表格转换为PDF格式时渲染评论。PrintCommentsType枚举具有以下常量。

- PrintCommentsType.PrintNoComments：不渲染评论。
- PrintCommentsType.PrintInPlace：在原处渲染评论。
- PrintCommentsType.PrintSheetEnd：在工作表末尾渲染评论。

以下示例代码演示了使用PageSetup.PrintComments属性使用所有可能的PrintCommentsType枚举值来渲染评论的方法。

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
Aspose.Cells.GridDesktop提供了WorksheetCollection.MoveTo方法，可用于将工作表移动到指定的索引。上述方法使用源工作表和目标工作表的索引（从零开始）作为参数。

以下示例代码演示了如何使用WorksheetCollection.MoveTo属性。

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **添加了Workbook.IsLicensed属性**
Aspose.Cells for .NET 8.4.1已公开了Workbook.IsLicensed属性，可以帮助确定许可证是否已成功加载。如果在设置许可证之前访问此属性，它将返回false，反之亦然，但是许可证应该是有效的。

以下示例代码演示了如何使用Workbook.IsLicensed属性。

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


### **添加了ImageOrPrintOptions.SVGFitToViewPort属性。**
Aspose.Cells for .NET 8.4.1已经为ImageOrPrintOptions类的SVGFitToViewPort属性提供了支持，可用于在导出电子表格或图表为SVG格式时打开SVG文件格式的viewBox属性。该属性的默认值为false，因此在不设置上述属性的情况下生成的SVG文件的基本XML不包括viewBox属性。

以下示例代码演示了如何使用ImageOrPrintOptions.SVGFitToViewPort属性。

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
## **已弃用的API**
### **已弃用 Workbook.ValidateFormula 方法**
使用Cell.Formula方法验证公式。
