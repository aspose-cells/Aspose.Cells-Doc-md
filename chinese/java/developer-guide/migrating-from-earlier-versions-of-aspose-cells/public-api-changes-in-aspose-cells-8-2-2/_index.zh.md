---
title: Aspose.Cells 8.2.2中的公共API更改
type: docs
weight: 100
url: /zh/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.2.1到8.2.2的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。

{{% /alert %}} 
## **已添加API**
### **为BuiltInDocumentPropertyCollection类添加了版本属性**
向BuiltInDocumentPropertyCollection类添加了新的Version属性，允许开发人员获取或设置给定电子表格所属应用程序的版本。

{{% alert color="primary" %}} 

请查看[获取创建电子表格的应用程序版本号](/cells/zh/java/get-the-version-number-of-the-application-that-created-the-excel-document/)的详细文章了解更多信息。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **新增了Chart.Worksheet属性**
在Aspose.Cells 8.2.2之前，无法从Chart对象中检索其包含的工作表实例。Aspose.Cells 8.2.2通过提供Chart.Worksheet属性填补了这一空白。

{{% alert color="primary" %}} 

请查看[获取图表的工作表](/cells/zh/java/get-worksheet-of-the-chart/)的详细文章了解更多信息。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
