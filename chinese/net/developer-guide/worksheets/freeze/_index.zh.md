---
title: 冻结Excel工作表的窗格
linktitle: 冻结窗格
type: docs
weight: 190
url: /zh/net/how-to-freeze-panes-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式冻结Excel工作表的窗格。
keywords: 冻结窗格，冻结窗口。
---

{{% alert color="primary" %}}

本文中，我们将学习如何冻结窗格。
当您有大量数据在一个常见标题下，当您向下滚动工作表时无法看到该标题。而且每个记录包含许多数据。您可以冻结窗格，以便即使其余数据在滚动时也能看到该冻结部分。您可以轻松查看顶部行或第一列中的标题。冻结和取消冻结窗格只会改变数据的视图，而不会改变数据本身。

{{% /alert %}}

## **在Excel中**

**![Excel中的冻结窗格](Freeze-panes.png)**


1. 如果您要冻结窗格、冻结行和列，首先选择一个单元格(比如B2)
2. 单击“查看” > “冻结窗格”
3. 在下拉菜单上，单击“冻结窗格”
4. 如果向下或向右滚动，第一行和第一列会被冻结

**![Fonzen panes](Frozen-Panes.png)**

如您所见，第一行和A列被冻结，第二行为32，第二可见列为D。 

冻结窗格能让您查看大量数据，而无需关注行或列标签。




## **使用Aspose.Cells for .Net进行冻结窗格**
使用Aspose.Cells for .Net很简单冻结窗格。请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法在选定单元格处冻结窗格。
1. 构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结窗格。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

附上[示例源Excel文件](Freeze.xlsx)。
