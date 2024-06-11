---
title: 冻结Excel工作表的第一列或多列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/net/how-to-freeze-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式冻结Excel工作表的左侧列。
keywords: 冻结左侧列，冻结第一列，锁定列
---

{{% alert color="primary" %}}

在本文中，我们将学习如何冻结左侧列。
当一行中有大量数据时，水平滚动工作表时无法看到左侧列。您可以冻结和锁定第一列，以便在其余数据滚动时仍然可见冻结部分。您可以轻松查看左侧的标题。

{{% /alert %}}

## **Excel中的冻结列**

**![在Excel中冻结左侧列](freeze-columns.png)**


1. 如果您想冻结左侧列，则首先选择需要冻结的列下面的列
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结第一列”
4. 如果向下滚动，第一列始终在左侧视图中。

**![冻结列](frozen-columns.png)**

如您所见，第1列被冻结，当您水平滚动时，第1列始终在视图顶部锁定。

冻结列可让您查看长数据，无需追踪第一列。




## **使用Aspose.Cells for .Net的冻结列**
使用Aspose.Cells for .Net很容易冻结第一列。 
请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法来冻结选定列。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一列。
3.保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

附上[示例源Excel文件](Freeze.xlsx)。
