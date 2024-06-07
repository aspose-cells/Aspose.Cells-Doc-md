---
title: 冻结Excel工作表的第一列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/net/how-to-freeze-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API编程来程序化地冻结Excel工作表的左侧列。
keywords: 冻结左侧列, 冻结首列, 锁定列
---

{{% alert color="primary" %}}

在本文中，我们将学习如何冻结左侧列。
当您的一行数据量很大，因此在水平滚动工作表时无法看到左侧列时，您可以冻结和锁定首列，这样即使其余数据被滚动，您也可以看到已冻结的部分。您可以轻松查看左侧列的标题。

{{% /alert %}}

## **在Excel中冻结列**

**![Excel中冻结左侧列](freeze-columns.png)**


1. 如果要冻结左侧列，则首先选择需要被冻结的列下面的列
2. 单击“查看” > “冻结窗格”
3. 在下拉菜单中，点击"冻结首列"。
4. 如果向下滚动，则首列始终在左侧视图中。

**![列冻结](frozen-columns.png)**

正如您所看到的，第一列被冻结，当您水平滚动时，第一列始终锁定在视图顶部。

冻结列让您无需记住第一列，即可查看长数据。




## **在Aspose.Cells for .Net中冻结列**
使用Aspose.Cells for .Net简单冻结首列。 
请使用 [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) 方法冻结列
1. 构建工作簿以打开文件或创建一个空文件。
2.使用Worksheet.FreezePanes()方法冻结首列。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

附上[示例源Excel文件](Freeze.xlsx)。
