---
title: 如何在没有Excel的情况下检查冻结状态。
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/net/how-to-check-frozen-state-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式检查Excel工作表的冻结状态。

---

{{% alert color="primary" %}}

在本文中，我们将学习如何以编程方式检查Excel工作表的冻结状态。
我们可以简单地找出MS Excel中的工作表是否被冻结或分割。但是否有一种方法可以找出它是冻结的还是分割的？
我们可以使用Aspose.Cells for .Net来实现。
{{% /alert %}}

## **窗格是否冻结**
使用Aspose.Cells for .Net，我们可以检查窗格是否被冻结以及锁定了多少行和列。

请使用 [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) 属性来检查窗格的状态 
并通过 [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/) 方法获取锁定的行和列。
1.构建工作簿以打开文件。
2.检查工作表是否被冻结。
3.获取锁定的行和列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
