---
title: Aspose.Cells 8.2.2中的公共API更改
type: docs
weight: 100
url: /zh/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

本文档介绍了从8.2.1版到8.2.2版的Aspose.Cells API的变更，这对模块/应用程序开发人员可能很有用。

{{% /alert %}} 
## **添加的 API**
### **为BuiltInDocumentPropertyCollection类添加了Version属性**
已经在BuiltInDocumentPropertyCollection类中添加了新属性Version，以允许开发人员获取或设置给定电子表格的应用程序版本。

{{% alert color="primary" %}} 

请查看详细文章【获取创建电子表格的应用程序的版本号】(/cells/zh/java/get-the-version-number-of-the-application-that-created-the-excel-document/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **添加了Chart.Worksheet属性**
在Aspose.Cells 8.2.2发布之前，无法从Chart对象中检索包含的Worksheet实例。Aspose.Cells 8.2.2通过提供Chart.Worksheet属性填补了这一空白。

{{% alert color="primary" %}} 

请查看详细文章【获取图表的工作表】(/cells/zh/java/get-worksheet-of-the-chart/)以获取更多信息。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
