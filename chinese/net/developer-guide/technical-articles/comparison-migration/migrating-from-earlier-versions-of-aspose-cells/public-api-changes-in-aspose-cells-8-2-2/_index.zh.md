---
title: Aspose.Cells 8.2.2中的公共API更改
type: docs
weight: 90
url: /zh/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.2.1到8.2.2的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。

{{% /alert %}} 
## **已添加API**
### **新增了BuiltInDocumentPropertyCollection.Version属性**
已添加新属性Version到BuiltInDocumentPropertyCollection类，以允许开发人员检索创建给定电子表格的应用程序的版本。

{{% alert color="primary" %}} 

请查阅有关[获取创建电子表格的应用程序版本号的详细文章](/cells/zh/net/get-the-version-number-of-the-application-that-created-the-excel-document/)以获取更多信息

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **新增了Chart.Worksheet属性**
在Aspose.Cells 8.2.2发布之前，无法从Chart对象中检索其持有的Worksheet实例。Aspose.Cells 8.2.2通过提供Chart.Worksheet属性填补了这一空白。

{{% alert color="primary" %}} 

请查阅有关[获取图表工作表的详细文章](/cells/zh/net/get-worksheet-of-the-chart/)以获取更多信息

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
