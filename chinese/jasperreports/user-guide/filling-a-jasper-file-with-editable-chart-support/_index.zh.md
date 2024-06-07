---
title: 填充带有可编辑图表支持的 .jasper 文件
type: docs
weight: 10
url: /zh/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports 需要将 .jasper 文件填充到 .jrprint 或 JasperPrint 对象中，然后才能将其导出到 XLS 文件。对 .jrxml 文件不需要进行任何修改。填充过程将图表的内部表示存储到 JasperPrint 对象中，然后用于生成可编辑图表。 

{{% /alert %}} 

请阅读 JasperReports 的文档，详细了解如何填充报告。

以下是一个例子:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
