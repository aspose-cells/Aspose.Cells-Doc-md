---
title: 冻结 Excel 工作表的第一列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/net/how-to-freeze-columns-of-excel-worksheet
description: 在本文中，您将了解如何使用 C# 库和 .NET API 以编程方式冻结 Excel 工作表的左列。
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

在本文中，我们将学习如何冻结左列。
当您的行中有大量数据时，当水平向下滚动工作表时您将无法看到左侧的列。您可以冻结并锁定第一列，以便即使在滚动其余数据时也可以看到冻结的部分。您可以轻松地在左列中看到标题。

{{% /alert %}}

##  **冻结 Excel 中的列**

**![冻结 Excel 中的左列](freeze-columns.png)**


1. 如果要冻结左侧列，请先选择需要冻结的列下的列
2. 单击视图 > 冻结窗格。
3. 在下拉菜单中，单击“冻结第一个列”。
4. 如果向下滚动，第一列始终位于左侧视图中。

**![Fonzen 专栏](frozen-columns.png)**

正如您所看到的，第一列被冻结，当您水平滚动时，第一列始终锁定在视图的顶部。

冻结列可让您查看长数据，而无需跟踪第一列。




##  **使用 Aspose.Cells for .Net 冻结列**
对于 .Net，使用 Aspose.Cells 冻结第一列很简单。
请使用[**工作表.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法在选定的列上对列进行收费。
1. 构造工作簿以打开文件或创建空文件。
2. 使用 Worksheet.FreezePanes() 方法冻结第一列。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

随附的[示例源 Excel 文件](Freeze.xlsx).
