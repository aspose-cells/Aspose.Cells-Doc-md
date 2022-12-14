---
title: 公共 API Aspose.Cells 8.2.2 的变化
type: docs
weight: 90
url: /zh/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.2.1 到 8.2.2 的变化，模块/应用程序开发人员可能会感兴趣。

{{% /alert %}} 
## **添加的 API**
### **已添加属性 BuiltInDocumentPropertyCollection.Version**
新属性 Version 已添加到 BuiltInDocumentPropertyCollection 类中，以允许开发人员检索创建给定电子表格的应用程序的版本。

{{% alert color="primary" %}} 

请查看详细文章[获取创建电子表格的应用程序版本](/cells/zh/net/get-the-version-number-of-the-application-that-created-the-excel-document/)了解更多信息。

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **添加了属性图表。工作表**
在 Aspose.Cells 8.2.2 发布之前，无法从其持有的图表对象中检索工作表的实例。 Aspose.Cells 8.2.2 通过提供 Chart.Worksheet 属性填补了这一空白。

{{% alert color="primary" %}} 

请查看详细文章[获取图表的工作表](/cells/zh/net/get-worksheet-of-the-chart/)了解更多信息。

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
