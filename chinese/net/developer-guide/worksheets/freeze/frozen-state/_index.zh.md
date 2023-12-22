---
title: 如何不用 Excel 检查冻结状态。
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/net/how-to-check-frozen-state-of-excel-worksheet
description: 在本文中，您将了解如何使用 C# 库和 .NET API 以编程方式检查 Excel 工作表的冻结状态。
---
{{% alert color="primary" %}}

在本文中，我们将学习如何以编程方式检查 Excel 工作表的冻结状态。
我们可以简单地在 MS Excel 中查看工作表是否被冻结或拆分。但是有没有办法用CSharp来判断是冻结还是分裂。
对于 .Net，我们可以简单地使用 Aspose.Cells 来完成。
{{% /alert %}}

##  **窗玻璃结冰了吗**
使用Aspose.Cells for .Net，我们可以检查窗口是否被冻结以及有多少行和列被锁定。

请使用[**工作表.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/)属性来检查窗格的状态
并获取锁定的行和列[**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)方法。
1. 构造工作簿以打开文件。
2. 检查工作表是否被冻结。
3.获取锁定的行和列

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}