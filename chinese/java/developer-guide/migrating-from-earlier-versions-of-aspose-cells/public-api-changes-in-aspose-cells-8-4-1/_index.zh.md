---
title: 公共 API Aspose.Cells 8.4.1 的变化
type: docs
weight: 150
url: /zh/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.4.0 到 8.4.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)和[删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **修改数据库连接的机制**
com.aspose.cells.ExternalConnection 类已包含可用于检查存储在电子表格中的数据库连接详细信息的方法和属性。在 Aspose.Cells for Java 8.4.1 发布之前，与 ExternalConnection 类关联的大部分属性都是只读的。在此版本中，API 也提供了对操作数据库连接设置的支持。

以下代码片段显示了如何动态修改数据库连接设置。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

以下是 {ExternalConnection}} 类公开的一些最重要的属性。

|**物业名称** |**描述** |
|:- |:- |
|后台刷新|指示是否可以在后台（异步）刷新连接。<br>如果连接的首选用法是在后台异步刷新，则为真；<br>如果连接的首选用法是在前台同步刷新，则为 false。|
|连接说明|指定此连接的用户描述|
|连接ID|指定此连接的唯一标识符。|
|证书|指定建立（或重新建立）连接时要使用的身份验证方法。|
|已删除|指示关联的工作簿连接是否已删除。如果<br>连接已被删除；否则，假的。|
|是新的|如果第一次没有刷新连接则为真；否则，假的。这个<br>当用户在查询完成返回之前保存文件时，可能会出现这种状态。|
|活着|当电子表格应用程序应努力保持连接时为真<br>打开。为 false 时，应用程序应在检索到<br>信息。|
|姓名|指定连接的名称。每个连接都必须有一个唯一的名称。|
| Odc文件|指定此连接来自的外部连接文件的完整路径<br>创建。如果在尝试刷新数据时连接失败，并且 reconnectionMethod=1，<br>然后电子表格应用程序将使用来自外部连接文件的信息重试<br>而不是工作簿中嵌入的连接对象。|
|仅使用连接文件|指示电子表格应用程序是否应始终且仅使用<br>odcFile 属性指示的外部连接文件中的连接信息<br>刷新连接时。如果为假，则电子表格应用程序<br>应遵循 reconnectionMethod 属性指示的过程|
|参数|获取 ODBC 或 Web 查询的 ConnectionParameterCollection。|
|重新连接方法|指定 reconnectionMethod 类型|
|刷新内部|指定连接自动刷新之间的分钟数。|
|加载时刷新|如果在打开文件时应刷新此连接，则为真；否则为真。否则，假的。|
|保存数据|如果要保存通过连接获取的用于填充表的外部数据，则为真<br>与工作簿；否则，假的。|
|保存密码|如果要将密码保存为连接字符串的一部分，则为真；否则为真。否则，假。|
|源文件|当外部数据源是基于文件的时使用。当连接到这样的数据时<br>source 失败，电子表格应用程序尝试直接连接到该文件。或许<br>以 URI 或系统特定的文件路径表示法表示。|
|SSOId|用于中间体之间身份验证的单点登录 (SSO) 标识符<br>spreadsheetML 服务器和外部数据源。|
|类型|指定数据源类型。|

### **能够格式化 DataLabels 文本的子字符串**
Aspose.Cells for Java 8.4.1 公开了 DataLabels.characters 方法以检索对应于 ChartPoints.DataLabels 的子字符串的 FontSetting 类的实例。反过来，FontSetting 类的实例可用于格式化具有不同字体设置和颜色的 DataLabels 的子字符串。

以下代码片段显示了如何使用 DataLabels.characters 方法。

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **能够为电子表格和图表导出设置所需的图像尺寸**
Aspose.Cells for Java 8.4.1 公开了 ImageOrPrintOptions.setDesiredSize 方法以在将电子表格和图表导出到图像时设置结果图像的尺寸。 ImageOrPrintOptions.setDesiredSize 方法接受两个整数类型参数，其中第一个是所需的宽度，第二个是所需的高度。

以下代码片段显示了如何在将工作表导出为 PNG 时设置所需的尺寸。

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

同样的方法也可以用于将图表转换为图像。

{{% /alert %}} 

### **将注释呈现为 PDF**
随着 v8.4.1 的发布，Aspose.Cells API 提供了 PageSetup.PrintComments 属性和 PrintCommentsType 枚举，以便在将电子表格转换为 PDF 格式时方便地呈现注释。 PrintCommentsType 枚举具有以下常量。

- 打印注释类型.PRINT_不_评论：不要发表评论。
- 打印注释类型.PRINT_在_PLACE：评论将在放置它们的地方呈现。
- 打印注释类型.PRINT_床单_结束：评论将在工作表的末尾呈现。

以下示例代码演示了如何使用 PageSetup.PrintComments 属性来使用所有可能的 PrintCommentsType 枚举值呈现注释。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **添加了 Workbook.isLicensed 属性**
Aspose.Cells for Java 8.4.1 公开了 Workbook.isLicensed，这对确定许可证是否已成功加载有很大帮助。如果您在设置许可证之前访问此属性，它将返回 false，反之亦然，但是，许可证应该是有效的。

以下示例代码演示了 Workbook.isLicensed 属性的用法。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **添加了 ImageOrPrintOptions.SVGFitToViewPort 属性**
Aspose.Cells for Java 8.4.1 公开了 ImageOrPrintOptions 类的 SVGFitToViewPort 属性，可用于在将电子表格或图表导出为 SVG 格式时打开 SVG 文件格式的 viewBox 属性。此属性的默认值为 false，因此在未设置上述属性的情况下生成的 SVG 文件的基本 XML 将不包含 viewBox 属性。

以下示例代码演示了 ImageOrPrintOptions.SVGFitToViewPort 属性的用法。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **过时的 API**
### **方法 Workbook.validateFormula 已废弃**
使用 Cell.Formula 属性验证公式。
