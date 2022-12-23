---
title: 打印工作簿
type: docs
weight: 20
url: /zh/java/printing-workbooks/
description: 如何使用 Java 打印工作表和工作簿。本文提供 Java 代码以使用 Aspose.Cells for Java API 打印工作表和工作簿。
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

本文档旨在让开发人员了解（以紧凑的方式）如何打印电子表格。

{{% /alert %}}

## 使用场景

完成电子表格创建后，您可能需要根据需要打印一份工作表的硬拷贝。打印时，MS Excel 假定您要打印整个工作表区域，除非您指定了您的选择。以下屏幕截图显示了使用 Excel 打印工作簿的对话框。

![待办事项：图片_替代_文本](printing-workbooks_1.png)

**数字：**打印对话框

## 使用 Aspose.Cells 打印工作簿

Aspose.Cells for Java 提供了一个[**到打印机**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) 的方法[**图纸渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)班级。通过使用[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) 方法，您可以提供打印机名称以及打印作业名称。

## 示例代码

### 打印选定的工作表

下面的代码片段演示了使用[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)方法来打印您选择的工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### 打印整个工作簿

您还可以使用[**工作簿渲染到打印机**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) 方法来打印整个工作簿。下面的代码片段演示了使用[**工作簿渲染到打印机**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)方法来打印整个工作簿。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## 相关文章

- [使用 Aspose.Cells 打印时指定作业或文档名称](/cells/zh/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
