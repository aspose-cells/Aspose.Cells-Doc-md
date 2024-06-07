---
title: 打印工作簿
type: docs
weight: 20
url: /zh/java/printing-workbooks/
description: 如何使用Java打印工作表和工作簿。 本文提供了使用Aspose.Cells for Java API打印工作表和工作簿的Java代码。
keywords: 打印工作簿，打印工作表，打印工作簿工作表，打印工作簿，打印工作簿java，打印工作表java，打印Excel工作簿java，打印Excel工作表java，打印工作簿，打印工作表
---

{{% alert color="primary" %}}

本文档旨在以简明的方式为开发人员提供如何打印电子表格的理解。

{{% /alert %}}

## 使用场景

在创建电子表格完成后，您可能希望打印表的硬拷贝以满足您的需求。 在打印时，MS Excel假设您要打印整个工作表区域，除非指定选择。 以下屏幕截图显示了使用Excel打印工作簿的对话框。

![todo:image_alt_text](printing-workbooks_1.png)

**图:** 打印对话框框

## 使用Aspose.Cells打印工作簿

Aspose.Cells for Java提供了 [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) 类的 [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)）方法。 通过使用 [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)）方法，您可以提供打印机名称和打印任务名称。

## 示例代码

### 打印所选工作表

以下代码片段演示了使用 [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)）方法打印所选的工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### 打印整个工作簿

您还可以使用 [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)）方法打印整个工作簿。 以下代码片段演示了使用 [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)）方法打印整个工作簿。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## 相关文章

- [使用Aspose.Cells打印时指定作业或文档名称](/cells/zh/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
