---
title: 公共 API Aspose.Cells 8.2.2 的变化
type: docs
weight: 100
url: /zh/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.2.1 到 8.2.2 的变化，模块/应用程序开发人员可能会感兴趣。

{{% /alert %}} 
## **添加的 API**
### **为 BuiltInDocumentPropertyCollection 类添加了属性版本**
新属性 Version 已添加到 BuiltInDocumentPropertyCollection 类中，以允许开发人员获取或设置给定电子表格的应用程序版本。

{{% alert color="primary" %}} 

请查看详细文章[获取创建电子表格的应用程序版本](/cells/zh/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **添加了属性图表。工作表**
在 Aspose.Cells 8.2.2 发布之前，无法从它包含的图表对象中检索工作表的实例。 Aspose.Cells 8.2.2 通过提供 Chart.Worksheet 属性填补了这一空白。

{{% alert color="primary" %}} 

请查看详细文章[获取图表的工作表](/cells/zh/java/get-worksheet-of-the-chart/)了解更多信息。

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
