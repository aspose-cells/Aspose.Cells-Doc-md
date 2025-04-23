---
title: 取消冻结行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/net/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API来以编程方式取消Excel工作表中的行、列或窗格。
keywords: 取消冻结窗格，取消冻结行，取消冻结列，取消冻结窗口。
---

## **介绍**

在本文章中，我们将学习如何取消冻结行、列和窗格。如果Excel文件中的工作表已经冻结，有时我们希望取消冻结工作表或调整冻结的行、列或窗格。


## **在Excel中**

1. 单击“查看”选项卡 > 冻结窗格 > 取消冻结窗格。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**




## **使用Aspose.Cells for .Net取消行、列或窗格的冻结**
使用Aspose.Cells for .Net很容易取消窗格的冻结。请使用[**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)方法取消窗格的冻结。

1. 构造工作簿以打开冻结文件。
2. 使用Worksheet.UnFreezePanes()方法取消窗格的冻结。
3.保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

附有[示例源Excel文件](Frozen.xlsx)。
{{< app/cells/assistant language="csharp" >}}
