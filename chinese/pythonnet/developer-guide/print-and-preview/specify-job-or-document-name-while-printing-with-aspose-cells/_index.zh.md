---
title: 使用Aspose.Cells在打印时指定作业或文档名称
type: docs
weight: 270
url: /zh/python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

你可以在打印工作簿或工作表时，使用WorkbookRender或SheetRender对象指定作业或文档名称。Aspose.Cells for Python via .NET 提供了WorkbookRender.ToPrinter（打印机名称，作业名称）和SheetRender.ToPrinter（打印机名称，作业名称）方法，可以在打印时指定作业名称。

{{% /alert %}}

## **在使用 Aspose.Cells for Python via .NET 打印时，指定作业或文档名称**

示例代码加载源Excel文件，然后使用WorkbookRender.ToPrinter(printerName, jobName)和SheetRender.ToPrinter(printerName, jobName)方法将其发送到打印机并指定作业或文档名称。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
