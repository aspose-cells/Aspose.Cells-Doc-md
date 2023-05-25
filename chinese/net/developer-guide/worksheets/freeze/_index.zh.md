---
title: 冻结 Excel 工作表的窗格
linktitle: 冻结窗格
type: docs
weight: 190
url: /zh/net/how-to-freeze-panes-of-excel-worksheet
description: 在本文中，您将学习如何使用 C# 库和 .NET API 以编程方式冻结 Excel 工作表的窗格。
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

在本文中，我们将学习如何冻结窗格。
当您在一个公共标题下有大量数据时，向下滚动工作表时您将看不到标题。每条记录包含很多数据。您可以冻结窗格，以便即使在滚动其余数据时也能看到冻结的部分。您可以轻松地在顶行或第一列中看到标题。冻结和解冻窗格只会更改数据的视图，而不会更改数据本身。

{{% /alert %}}

##  **在 Excel 中**

**![冻结 Excel 中的窗格](Freeze-panes.png)**


1. 如果要冻结窗格来冻结行和列，则首先选择一个单元格（如B2）
2. 单击视图 > 冻结窗格。
3. 在下拉菜单中，单击冻结窗格。
4. 如果向下或向右滚动，第一行和第一列将被冻结。

**![Fonzen panges](Frozen-Panes.png)**

如您所见，第一行和 A 列已冻结，第二行显示为 32，第二个可见列为 D。

冻结窗格让您无需跟踪行或列标签即可查看大数据。




##  **使用 Aspose.Cells for .Net 冻结窗格**
使用 Aspose.Cells for .Net 冻结窗格很简单。请使用[**工作表.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)在选定的 Cell 处冻结窗格的方法。
1. 构造工作簿以打开文件或创建一个空文件。
2. 使用 Worksheet.FreezePanes() 方法冻结窗格。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

随附的[示例源 Excel 文件](Freeze.xlsx).
