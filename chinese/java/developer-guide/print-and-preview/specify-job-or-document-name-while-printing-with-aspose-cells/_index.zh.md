---
title: 使用Aspose.Cells在打印时指定作业或文档名称
type: docs
weight: 160
url: /zh/java/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

您可以使用[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)或[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)对象打印工作簿或工作表时指定作业或文档名称。Aspose.Cells提供了[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-java.lang.String-)和[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-java.lang.String-)方法，您可以使用它们来指定打印工作簿或工作表时的作业名称。

{{% /alert %}}

## **在使用 Aspose.Cells 打印时指定作业或文档名称**

示例代码加载源Excel文件，然后通过指定作业或文档名称使用[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-java.lang.String-)和[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-java.lang.String-)方法将其发送到打印机。屏幕截图显示了作业名称在打印队列中的外观。

![todo:image_alt_text](specify-job-or-document-name-while-printing-with-aspose-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyJoborDocumentName-SpecifyJoborDocumentName.java" >}}

## 相关文章

- [打印工作簿](/cells/zh/java/printing-workbooks/)
{{< app/cells/assistant language="java" >}}
