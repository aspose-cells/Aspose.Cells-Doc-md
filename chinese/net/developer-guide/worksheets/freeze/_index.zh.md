---
title: 冻结Excel工作表的窗格
linktitle: 冻结窗格
type: docs
weight: 190
url: /zh/net/how-to-freeze-panes-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式冻结Excel工作表的窗格。
keywords: 冻结窗格，冻结窗口。
---

## **介绍**

在本文中，我们将学习如何冻结窗格。当您有大量数据位于共同标题下时，当滚动工作表时通常无法看到标题。每条记录包含许多数据。您可以冻结窗格，以便即使其余数据正在滚动，仍然可以看到冻结部分。您可以轻松地在顶部行或第一列中查看标题。冻结和取消冻结窗格只会更改数据的视图，而不更改数据本身。

## **在Excel中**

**![Excel中的冻结窗格](Freeze-panes.png)**


1. 如果要冻结窗格，冻结行和列，则首先选择单元格（例如B2）
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结窗格”
4. 如果向下或向右滚动，第一行和列将被冻结。

**![冻结窗格](Frozen-Panes.png)**

正如您所看到的，第一行和A列已被冻结，第二行为32，第二个可见列为D。 

冻结窗格使您能够查看大量数据而无需跟踪行或列标签。




## **使用Aspose.Cells for .Net冻结窗格**
使用Aspose.Cells for .Net简单冻结窗格。请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法来在选定单元格中冻结窗格。
1.构建工作簿以打开文件或创建一个空文件。
2.使用Worksheet.FreezePanes()方法冻结窗格。
3.保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

附上[示例源Excel文件](Freeze.xlsx)。
