---
title: 激活工作表和工作表中的单元格
type: docs
weight: 5
url: /zh/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

有时，当用户在Excel中打开Microsoft Excel文件时，您需要特定的工作表处于活动状态并显示。同样，您可能希望激活特定单元格并设置滚动条以显示活动单元格。正如下面演示的，Aspose.Cells能够完成所有这些任务。

- **活动工作表**是您正在处理的工作表：标签上的活动工作表名称默认为粗体。
- **活动单元格**是一个选定的单元格，当您开始输入数据时，数据将输入到该单元格中。一次只有一个单元格是活动的。活动单元格由粗边框突出显示。

{{% /alert %}}

## **激活工作表和激活单元格**

Aspose.Cells 提供了专门的 API 调用，用于激活工作表和单元格。例如，[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) 属性用于设置工作簿中的活动工作表。同样，[**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) 属性可用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条位于您想要显示特定数据的行和列索引位置，请使用 [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) 和 [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn) 属性。

以下示例展示了如何激活工作表并使其中的单元格成为活动单元格。执行代码时生成以下输出。滚动条已滚动以使第2行和第2列成为其第一个可见的行和列。

**将B2单元格设置为活动单元格**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## 在 Excel 中设置活动工作表的 Java 代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

在**评估**模式下，即在未设置有效许可证的情况下，活动工作表将始终包含评估水印。此行为只能通过在应用程序启动时设置许可证来覆盖。

{{% /alert %}}
