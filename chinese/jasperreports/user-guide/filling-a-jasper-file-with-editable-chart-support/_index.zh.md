---
title: 用可编辑图表支持填充.jasper文件
type: docs
weight: 10
url: /zh/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

在将 .jrxml 文件导出为 XLS 文件之前，需要将 Aspose.Cells for JasperReports 填充为 .jrprint 或 JasperPrint 对象。.jrxml 文件不需要进行任何修改。填充过程将图表的内部表示存储到 JasperPrint 对象中，然后用于生成可编辑图表。 

{{% /alert %}} 

请阅读JasperReports的文档，详细了解如何填充报表。

以下是一个例子：

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
