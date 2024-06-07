---
title: 使用Aspose.Cells指定打印时的作业或文档名称
type: docs
weight: 160
url: /zh/java/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

您可以在打印工作簿或工作表时使用[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)或[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)对象指定作业或文档名称。Aspose.Cells提供了[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String,%20java.lang.String)和[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String,%20java.lang.String)方法，您可以使用这些方法在打印工作簿或工作表时指定作业名称。

{{% /alert %}}

## **使用Aspose.Cells打印时指定作业或文档名称**

示例代码加载源Excel文件，然后通过使用[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String,%20java.lang.String))和[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String,%20java.lang.String))方法指定作业或文档名称将其发送到打印机。屏幕截图显示了作业名称在打印队列中的外观。

![todo:image_alt_text](specify-job-or-document-name-while-printing-with-aspose-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyJoborDocumentName-SpecifyJoborDocumentName.java" >}}

## 相关文章

- [打印工作簿](/cells/zh/java/printing-workbooks/)
