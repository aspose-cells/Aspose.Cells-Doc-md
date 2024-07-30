---
title: 如何在没有Excel的情况下检查冻结状态
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/python-net/how-to-check-frozen-state-of-excel-worksheet
description: 在本文中，您将学习如何使用Aspose.Cells for Python via .NET API以编程方式检查Excel工作表的冻结状态。
keywords: Python Excel库, Python如何在没有Excel的情况下检查冻结状态
---

## **介绍**

在本文中，我们将学习如何以编程方式检查Excel工作表的冻结状态。我们可以简单地找出工作表是否在MS Excel中冻结或分割。但是有没有办法以CSharp找出它是否被冻结或分割。我们可以使用Aspose.Cells for Python via .NET来实现。

## **如何检查冻结状态**
使用Aspose.Cells for Python via .NET，我们可以检查窗口是否被冻结以及有多少行和列被锁定。

请使用 [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) 属性来检查窗格的状态 
并通过 [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) 方法获取锁定的行和列。
1.构建工作簿以打开文件。
2.检查工作表是否被冻结。
3.获取锁定的行和列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
