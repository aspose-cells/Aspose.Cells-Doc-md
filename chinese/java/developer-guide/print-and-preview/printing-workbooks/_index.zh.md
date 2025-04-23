---
title: 打印工作簿
type: docs
weight: 20
url: /zh/java/printing-workbooks/
description: 如何使用 Java 打印工作表和工作簿。本文提供了使用 Aspose.Cells for Java API 打印工作表和工作簿的 Java 代码。
keywords: 打印工作簿，打印工作表，打印工作表页，打印工作簿，打印工作簿java，打印工作表java，打印excel工作簿java，打印excel工作表java，打印工作簿，打印工作表
---

{{% alert color="primary" %}}

本文档旨在为开发人员提供如何以简明方式打印电子表格的理解。

{{% /alert %}}

## 使用情景

完成创建电子表格后，您可能希望打印工作表的硬拷贝以备份。在打印时，MS Excel假定您要打印整个工作表区域，除非您指定所需的选择。以下截图显示了在Excel中打印工作簿的对话框。

![todo:image_alt_text](printing-workbooks_1.png)

**图表：** 打印对话框

## 使用 Aspose.Cells 打印工作簿

Aspose.Cells for Java提供了[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)类的[**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)方法。通过使用[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)方法，您可以提供打印机名称以及打印作业名称。

## 示例代码

### 打印所选工作表

以下代码片段演示了使用[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)方法打印所选工作表的方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### 打印整个工作簿

您还可以使用[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-)方法打印整个工作簿。以下代码片段演示了使用[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-)方法打印整个工作簿的方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## 相关文章

- [在使用 Aspose.Cells 打印时指定作业或文档名称](/cells/zh/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
