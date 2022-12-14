---
title: 使用可编辑图表支持填充 .jasper 文件
type: docs
weight: 10
url: /zh/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

JasperReports 的 Aspose.Cells 需要将 .jasper 文件填充到 .jrprint 或 JasperPrint 对象，然后才能将其导出到 XLS 文件。 .jrxml 文件不需要任何修改。填充过程将图表的内部表示存储到 JasperPrint 对象中，然后使用该对象生成可编辑图表。

{{% /alert %}} 

请阅读 JasperReports 的文档以获取有关如何填写报告的详细说明。

这是一个例子：

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
