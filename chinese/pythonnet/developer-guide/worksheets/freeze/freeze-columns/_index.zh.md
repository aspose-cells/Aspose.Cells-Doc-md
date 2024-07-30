---
title: 冻结Excel工作表的第一列或多列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/python-net/how-to-freeze-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用Aspose.Cells for Python via .NET API对Excel工作表的左列进行冻结。
keywords: Python Excel库, Python冻结左列, Python锁定列
---

## **介绍**

在本文章中，我们将学习如何冻结左侧列。当您在一行中有大量数据时，当水平滚动工作表时，您无法看到左边的列。您可以冻结和锁定第一列，以便在其余数据被滚动时仍然可以看到该冻结部分。您可以轻松看到左列的标题。


## **如何在Excel中冻结列**

**![在Excel中冻结左侧列](freeze-columns.png)**


1. 如果您想冻结左侧列，则首先选择需要冻结的列下面的列
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结第一列”
4. 如果向下滚动，第一列始终在左侧视图中。

**![冻结列](frozen-columns.png)**

如您所见，第1列被冻结，当您水平滚动时，第1列始终在视图顶部锁定。

冻结列可让您查看长数据，无需追踪第一列。




## **使用Aspose.Cells for Python Excel库冻结列的方法**
使用Aspose.Cells for Python via .NET，很容易冻结首列。请使用[**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)方法在所选列上冻结列。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一列。
3.保存文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

附上[示例源Excel文件](Freeze.xlsx)。
