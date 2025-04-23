---
title: 使用Aspose.Cells在打印时指定作业或文档名称
type: docs
weight: 270
url: /zh/net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

您可以使用WorkbookRender或SheetRender对象在打印工作簿或工作表时指定作业或文档名称。Aspose.Cells提供WorkbookRender.ToPrinter(printerName, jobName)和SheetRender.ToPrinter(printerName, jobName)方法，您可以使用这些方法在打印工作簿或工作表时指定作业名称。

{{% /alert %}}

##使用Aspose.Cells在打印时指定作业或文档名称

示例代码加载源Excel文件，然后使用WorkbookRender.ToPrinter(printerName, jobName)和SheetRender.ToPrinter(printerName, jobName)方法将其发送到打印机并指定作业或文档名称。

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
