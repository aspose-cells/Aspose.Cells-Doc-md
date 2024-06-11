---
title: 激活工作表和工作表中的单元格
type: docs
weight: 5
url: /zh/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

有时，您需要在用户在Excel中打开Microsoft Excel文件时使特定工作表处于活动状态并显示。同样，您可能希望激活特定单元格并设置滚动条来显示活动单元格。Aspose.Cells可以像下面演示的那样执行所有这些任务。

- **活动工作表**是您正在处理的工作表：默认情况下，标签上活动工作表的名称是加粗的。
- **活动单元**是选定的单元，也是在开始输入时要输入数据的单元。一次只能有一个单元是活动单元。活动单元由粗边框突出显示。

{{% /alert %}}

## **激活工作表和激活单元**

Aspose.Cells提供了特定的API调用来激活工作表和单元。例如，[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)属性对于在工作簿中设置活动工作表非常有用。同样，[**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)属性可用于设置和获取工作表中的活动单元。

要确保水平或垂直滚动条位于要显示特定数据的行和列索引位置，请使用[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)和[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)属性。

以下示例显示了如何激活工作表并使其中的活动单元。执行代码时会生成以下输出。滚动条会滚动，以使第二行和第二列成为它们的第一个可见行和列。

**将B2单元设置为活动单元**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## 设置Excel中的活动工作表的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

在**评估**模式下，也就是说，没有设置有效许可证的情况下，活动工作表将始终是包含评估水印的工作表。只有在应用程序启动时设置许可证，才能覆盖此行为。

{{% /alert %}}
