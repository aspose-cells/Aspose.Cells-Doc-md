---
title: 如何在没有 Excel 的情况下检查冻结状态。
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/python-net/how-to-check-frozen-state-of-excel-worksheet
description: 在本文中，您将学习如何使用 Aspose.Cells for Python via .NET API 编程方式检查 Excel 工作表的冻结状态。
keywords: Python Excel 库，Python 如何在没有 Excel 的情况下检查冻结状态，Python 中检查冻结状态。
---

## **介绍**

在本文中，我们将学习如何通过编程方式检查 Excel 工作表的冻结状态。我们可以轻松在 MS Excel 中找到工作表是否冻结或拆分。但是否有办法用 CSharp 判断是否冻结或拆分。我们可以用 Aspose.Cells for Python via .NET 轻松实现。

## **如何检查冻结状态**
使用 Aspose.Cells for Python via .NET，我们可以检查窗口是否冻结，以及锁定了多少行列。

请使用 [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) 属性来检查窗格的状态 
并通过 [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) 方法获取锁定的行和列。
1.构建工作簿以打开文件。
2.检查工作表是否被冻结。
3.获取锁定的行和列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
