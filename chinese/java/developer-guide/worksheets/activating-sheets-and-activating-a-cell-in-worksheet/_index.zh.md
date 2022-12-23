---
title: 激活工作表并在工作表中激活 Cell
type: docs
weight: 5
url: /zh/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

有时，当用户在 Excel 中打开 Microsoft Excel 文件时，您需要激活并显示特定的工作表。同样，您可能想要激活特定单元格并设置滚动条以显示活动单元格。 Aspose.Cells 能够完成所有这些任务，如下所示。

- 一个**活动表**是您正在处理的工作表：选项卡上的活动工作表名称默认为粗体。
- 一个**活性细胞**是一个选定的单元格，当您开始键入时，数据将被输入到该单元格中。一次只有一个细胞处于活动状态。活动单元格以粗边框突出显示。

{{% /alert %}}

## **激活工作表和激活 Cell**

Aspose.Cells 提供用于激活工作表和单元格的特定 API 调用。例如，[**工作表集合.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)属性对于在工作簿中设置活动工作表很有用。同样，[**工作表.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)属性可用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条位于要显示特定数据的行和列索引位置，请使用[**工作表.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)和[**工作表.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)特性。

以下示例显示如何激活工作表并在其中创建活动单元格。执行代码时会生成以下输出。滚动条滚动使第 2 行和第 2 列成为它们的第一个可见行和列。

**将 B2 单元格设置为活动单元格**

![待办事项：图片_替代_文本](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java 在 Excel 中设置活动工作表的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

在**评估**模式，即；如果没有设置有效的许可证，活动工作表将始终是包含评估水印的工作表。此行为只能通过在应用程序启动时设置许可证来覆盖。

{{% /alert %}}
