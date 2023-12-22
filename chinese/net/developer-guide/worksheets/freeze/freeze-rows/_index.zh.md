---
title: 冻结 Excel 工作表的顶行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/net/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将了解如何使用 C# 库和 .NET API 以编程方式冻结 Excel 工作表的顶行。
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

在本文中，我们将学习如何冻结顶行。
当公共标题下有大量数据时，向下滚动工作表时将无法看到标题。您可以冻结顶行，这样即使其余数据正在滚动，您也可以看到冻结的部分。您可以轻松地在顶行中看到标题。

{{% /alert %}}

##  **冻结 Excel 中的行**

**![冻结 Excel 中的顶行](Freeze-Rows.png)**


1. 如果要冻结顶行，请先选择需要冻结的行下方的行
2. 单击视图 > 冻结窗格。
3. 在下拉菜单中，单击“冻结顶行”。
4. 如果向下滚动，第一行始终位于顶视图中。

**![Fonzen 行](Frozen-Row.png)**

正如您所看到的，第一行被冻结，当您向下滚动时，第一行始终保留在视图的顶部。

冻结行可让您查看大数据，而无需跟踪行标签。




##  **使用 Aspose.Cells for .Net 冻结行**
对于 .Net，使用 Aspose.Cells 冻结行很简单。
请使用[**工作表.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法在所选行处收取行费用。
1. 构造工作簿以打开文件或创建空文件。
2. 使用 Worksheet.FreezePanes() 方法冻结第一行。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

随附的[示例源 Excel 文件](../Freeze.xlsx).
