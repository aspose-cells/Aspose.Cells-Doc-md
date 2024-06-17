---
title: Aspose.Cells 8.4.1中的公共API更改
type: docs
weight: 150
url: /zh/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.4.0到8.4.1的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)以及[删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-1/)，还描述了Aspose.Cells背后的任何变化的行为。

{{% /alert %}} 
## **添加的 API**
### **修改数据库连接的机制**
com.aspose.cells.ExternalConnection类已经包含了可以用于检查存储在电子表格中的数据库连接细节的方法和属性。与ExternalConnection类相关的大多数属性在Aspose.Cells for Java 8.4.1之前都是只读的。随着这一发布，API现在还提供了支持来操纵数据库连接设置。

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

以下是ExternalConnection类公开的一些最重要的属性。

|属性名称|描述|
| :- | :- |
|BackgroundRefresh |指示连接是否可以在后台（异步）刷新。 true表示首选使用连接的用法是在后台异步刷新；false表示首选使用连接的用法是在前台同步刷新。
|ConnectionDescription |指定此连接的用户描述
|ConnectionId |指定此连接的唯一标识符
|Credentials |指定建立（或重新建立）连接时要使用的认证方法
|IsDeleted |指示关联的工作簿连接是否已被删除。如果连接已被删除，则为true；否则为false。
|IsNew |如果连接尚未首次刷新，则为true；否则为false。当用户在查询完成返回之前保存文件时，可能会出现这种状态。
|KeepAlive |此处有两处翻译不够准确。当电子表格应用程序应该努力保持连接打开时为true。如已经说过的，此处_TRANSLATION_NEEDED_关闭连接后应关闭连接。 
|Name |指定连接的名称。每个连接都必须有一个唯一名称。
|OdcFile |指定从创建此连接的外部连接文件到此文件的完整路径。如果在尝试刷新数据时连接失败，并且reconnectionMethod=1，那么电子表格应用程序将尝试使用来自外部连接文件的信息，而不是工作簿内嵌连接对象的信息。
|OnlyUseConnectionFile |指示电子表格应用程序是否应始终且仅应在刷新连接时使用由odcFile属性指示的外部连接文件中的连接信息。如果为false，则电子表格应用程序应遵循reconnectionMethod属性指示的过程。
|Parameters |获取ODBC或Web查询的ConnectionParameterCollection
|ReConnectionMethod |指定reconnectionMethod类型
|RefreshInternal|指定连接自动刷新之间的分钟数
|RefreshOnLoad |如果此连接在打开文件时应刷新，则为true；否则为false。
|SaveData |如果通过连接获取的外部数据用于填充表，并且应保存到工作簿中，为true；否则为false。
|SavePassword |如果要将密码保存为连接字符串的一部分，则为True；否则为False。
|SourceFile |用于外部数据源为基于文件时使用。当连接到此类数据源失败时，电子表格应用程序将尝试直接连接到此文件。可以用URI或特定于系统的文件路径表示。
|SSOId|用于在中间spreadsheetML服务器和外部数据源之间进行身份验证的单点登录（SSO）标识符。
|Type |指定数据源类型。

### **格式化数据标签文本的子字符串的能力**
Aspose.Cells for Java 8.4.1已经暴露了DataLabels.characters方法，用于检索与ChartPoints.DataLabels子串对应的FontSetting类的实例。转而，可以使用FontSetting类的实例来使用不同的字体设置和颜色格式化DataLabels的子串。

以下代码段显示了如何使用DataLabels.characters方法。

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

### **设置电子表格和图表导出的所需图像尺寸的能力**
Aspose.Cells for Java 8.4.1已经暴露了ImageOrPrintOptions.setDesiredSize方法，用于设置导出电子表格和图表到图像时的结果图像的尺寸。ImageOrPrintOptions.setDesiredSize方法接受两个整数类型的参数，第一个是所需的宽度，第二个是所需的高度。

以下代码段显示了如何导出工作表到PNG时设置所需尺寸。

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
随着V8.4.1的发布，Aspose.Cells API提供了PageSetup.PrintComments属性和PrintCommentsType枚举，以便在将电子表格转换为PDF格式时方便渲染评论。PrintCommentsType枚举有以下常量。 

- PrintCommentsType.PRINT_NO_COMMENTS：不渲染评论。
- PrintCommentsType.PRINT_IN_PLACE：在其位置渲染评论。
- PrintCommentsType.PRINT_SHEET_END：在工作表末尾渲染评论。

以下示例代码演示了使用PageSetup.PrintComments属性以使用所有可能的PrintCommentsType枚举值来渲染注释。

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

### **添加了Workbook.isLicensed属性**
Aspose.Cells for Java 8.4.1已经暴露了Workbook.isLicensed属性，对于确定许可证是否已成功加载是非常有帮助的。如果在设置许可证之前访问此属性，它将返回false，反之亦然，但是许可证应该是有效的。

以下示例代码演示了Workbook.isLicensed属性的用法。

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

### **添加了ImageOrPrintOptions.SVGFitToViewPort属性**
Aspose.Cells for Java 8.4.1已经暴露了SVGFitToViewPort属性，用于在将电子表格或图表导出为SVG格式时打开SVG文件格式的viewBox属性。因此，未设置上述属性的情况下生成的SVG文件的基本XML将不包括viewBox属性，默认值为false。

以下示例代码展示了使用ImageOrPrintOptions.SVGFitToViewPort属性的用法。

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
## **已弃用的API**
### **不推荐使用Workbook.validateFormula方法**
请使用Cell.Formula属性验证公式。
