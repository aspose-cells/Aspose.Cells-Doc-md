---
title: 使用 Aspose.Cells 打印时指定作业或文档名称
type: docs
weight: 270
url: /zh/net/specify-job-or-document-name-while-printing-with-aspose-cells/
---
{{% alert color="primary" %}}

您可以在使用 WorkbookRender 或 SheetRender 对象打印工作簿或工作表时指定作业或文档名称。 Aspose.Cells 提供了 WorkbookRender.ToPrinter(printerName, jobName) 和 SheetRender.ToPrinter(printerName, jobName) 方法，您可以使用这些方法在打印工作簿或工作表时指定作业名称

{{% /alert %}}

## 使用 Aspose.Cells 打印时指定作业或文档名称

示例代码加载源 Excel 文件，然后通过使用 WorkbookRender.ToPrinter(printerName, jobName) 和 SheetRender.ToPrinter(printerName, jobName) 方法指定作业或文档名称将其发送到打印机。

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
