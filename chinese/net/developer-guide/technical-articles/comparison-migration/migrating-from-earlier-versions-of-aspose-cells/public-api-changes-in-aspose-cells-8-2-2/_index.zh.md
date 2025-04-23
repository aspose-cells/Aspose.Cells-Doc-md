---
title: Aspose.Cells 8.2.2中的公共API更改
type: docs
weight: 90
url: /zh/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

本文档介绍了从8.2.1版到8.2.2版的Aspose.Cells API的变更，这对模块/应用程序开发人员可能很有用。

{{% /alert %}} 
## **添加的 API**
### **已添加 BuiltInDocumentPropertyCollection.Version 属性**
已向 BuiltInDocumentPropertyCollection 类中添加新属性 Version，以便开发人员能够检索创建给定电子表格的应用程序的版本。

{{% alert color="primary" %}} 

请查看详细文章[获取创建电子表格的应用程序的版本号](/cells/zh/net/get-the-version-number-of-the-application-that-created-the-excel-document/)以获取更多信息。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **添加了Chart.Worksheet属性**
在 Aspose.Cells 8.2.2 发布之前，无法从 Chart 对象中检索 Worksheet 的实例。Aspose.Cells 8.2.2 填补了这一空白，提供了 Chart.Worksheet 属性。

{{% alert color="primary" %}} 

请查看详细文章[获取图表的工作表](/cells/zh/net/get-worksheet-of-the-chart/)以获取更多信息。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
