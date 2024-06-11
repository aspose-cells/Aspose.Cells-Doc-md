---
title: 用可编辑图表支持填充.jasper文件
type: docs
weight: 10
url: /zh/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports需要将.jasper文件填充到.jrprint或JasperPrint对象中，然后才能将其导出为XLS文件。对于.jrxml文件，不需要任何修改。填充过程将图表的内部表示存储到JasperPrint对象中，然后用于生成可编辑图表。 

{{% /alert %}} 

请阅读JasperReports的文档，详细了解如何填充报表。

以下是一个例子：

Java

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
