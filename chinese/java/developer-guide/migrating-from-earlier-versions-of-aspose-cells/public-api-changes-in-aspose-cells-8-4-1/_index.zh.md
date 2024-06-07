---
title: Aspose.Cells 8.4.1 中的公共 API 更改
type: docs
weight: 150
url: /zh/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本 8.4.0 到 8.4.1 的 Aspose.Cells API 的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)和[删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)，还包括对 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **修改数据库连接的机制**
com.aspose.cells.ExternalConnection 类已经包含了用于检查存储在电子表格中的数据库连接详细信息的方法和属性。直到 Aspose.Cells for Java 8.4.1 的发布，与 ExternalConnection 类相关的大多数属性都是只读的。随着此版本的发布，API已经提供了支持以操作数据库连接设置。

以下代码片段显示了如何动态修改数据库连接设置。

**Java**

{{< highlight csharp >}}

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

这里是{ExternalConnection}}类公开的一些最重要的属性。

|**属性名称**|**描述**|
| :- | :- |
|BackgroundRefresh |指示连接是否可以在后台刷新（异步）。<br>如果首选使用连接的方式是在后台异步刷新，则为 true；<br>如果首选使用连接的方式是在前台同步刷新，则为 false。|
|ConnectionDescription |指定此连接的用户描述 |
|ConnectionId |指定此连接的唯一标识符。|
|Credentials |指定在建立（或重新建立）连接时要使用的身份验证方法。|
|IsDeleted |指示关联的工作簿连接是否已删除。如果连接已被删除，则为 true；否则为 false。|
|IsNew |如果连接尚未首次刷新，则为 true；否则为 false。这种状态可能发生在用户在查询完成返回前保存文件时。|
|KeepAlive |当电子表格应尽力保持连接开放时为 true。当为 false 时，应用程序应在检索信息后关闭连接。|
|Name |指定连接的名称。每个连接必须有唯一的名称。|
|OdcFile |指定从创建此连接的外部连接文件的完整路径。<br>如果在尝试刷新数据时连接失败，并且 reconnectionMethod=1，则电子表格应用程序将尝试使用外部连接文件的信息再次尝试，而不使用嵌入在工作簿中的连接对象。|
|OnlyUseConnectionFile |指示电子表格应用程序在刷新连接时始终且只使用由 odcFile 属性指示的外部连接文件中的连接信息。如果为 false，则电子表格应用程序应遵循 reconnectionMethod 属性所指示的程序。|
|Parameters |获取 ODBC 或 Web 查询的 ConnectionParameterCollection。|
|ReConnectionMethod |指定 reconnectionMethod 类型。|
|RefreshInternal|指定连接自动刷新之间的分钟数。|
|RefreshOnLoad |如果打开文件时应刷新此连接，则为 true；否则为 false。|
|SaveData |如果通过连接提取外部数据以填充表格，则应将其保存到工作簿中，则为 true；否则为 false。|
|SavePassword |如果密码应作为连接字符串的一部分保存，则为 true；否则为 False。|
|SourceFile |当外部数据源为基于文件时使用。当连接到此类数据源失败时，电子表格应用程序尝试直接连接到此文件。可以用 URI 或特定于系统的文件路径表示。|
|SSOId|用于在中间 spreadsheetML 服务器和外部数据源之间进行身份验证的单点登录 (SSO) 标识符。|
|Type |指定数据源类型。|

### **能够格式化数据标签文本的子字符串**
Aspose.Cells for Java 8.4.1已经公开了DataLabels.characters方法，用于检索对应于ChartPoints.DataLabels的子串的FontSetting类的实例。然后，可以使用FontSetting类的实例来使用不同的字体设置和颜色格式化DataLabels的子串。

以下代码片段显示了如何使用DataLabels.characters方法。

**Java**

{{< highlight csharp >}}

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

### **在电子表格和图表导出中设置所需的图像尺寸**
Aspose.Cells for Java 8.4.1已经公开了ImageOrPrintOptions.setDesiredSize方法，用于在导出电子表格和图表到图像时设置结果图像的尺寸。ImageOrPrintOptions.setDesiredSize方法接受两个整数类型参数，第一个是期望的宽度，第二个是期望的高度。

以下代码段显示了如何在将工作表导出为PNG时设置所需的尺寸。

**Java**

{{< highlight csharp >}}

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

相同的方法也可用于将图表转换为图像。 

{{% /alert %}} 

### **将评论渲染为PDF**
随着v8.4.1的发布，Aspose.Cells API提供了PageSetup.PrintComments属性和PrintCommentsType枚举，以便在将电子表格转换为PDF格式时渲染评论。PrintCommentsType枚举具有以下常量。 

- PrintCommentsType.PRINT_NO_COMMENTS: 不渲染注释。
- PrintCommentsType.PRINT_IN_PLACE: 渲染注释并将它们放置在其所在位置。
- PrintCommentsType.PRINT_SHEET_END: 将注释渲染到工作表末尾。

以下示例代码演示了使用PageSetup.PrintComments属性使用所有可能的PrintCommentsType枚举值来渲染评论的方法。

**Java**

{{< highlight csharp >}}

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

### **添加了Workbook.isLicensed属性。**
Aspose.Cells for Java 8.4.1已经公开了Workbook.isLicensed属性，可帮助确定许可证是否已成功加载。如果在设置许可证之前访问此属性，它将返回false，反之亦然。但是，许可证应该是有效的。

以下示例代码演示了如何使用Workbook.isLicensed属性。

**Java**

{{< highlight csharp >}}

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

### **添加了ImageOrPrintOptions.SVGFitToViewPort属性。**
Aspose.Cells for Java 8.4.1已经公开了ImageOrPrintOptions类的SVGFitToViewPort属性，用于在导出电子表格或图表到SVG格式时打开SVG文件格式的viewBox属性。该属性的默认值为false，因此未设置上述属性生成的SVG文件的基本XML将不包括viewBox属性。

以下示例代码演示了如何使用ImageOrPrintOptions.SVGFitToViewPort属性。

**Java**

{{< highlight csharp >}}

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
## **已废弃的API**
### **已废弃 Workbook.validateFormula 方法**
使用Cell.Formula属性验证公式。
