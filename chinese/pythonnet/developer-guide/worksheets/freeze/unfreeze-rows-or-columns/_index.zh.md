---
title: 取消冻结行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: 本文将教你如何使用 Aspose.Cells for Python via .NET API 编程方式取消 Excel 工作表的行、列或窗格冻结。
keywords: Python Excel 库，Python 取消冻结窗格，Python 如何取消冻结行，Python 如何取消冻结列，Python 如何取消冻结窗口。
---

## **介绍**

在本文章中，我们将学习如何取消冻结行、列和窗格。如果Excel文件中的工作表已经冻结，有时我们希望取消冻结工作表或调整冻结的行、列或窗格。


## **如何在 Excel 中取消冻结行或列**

1. 单击“查看”选项卡 > 冻结窗格 > 取消冻结窗格。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**




## **使用 Aspose.Cells for Python Excel 库，如何取消冻结行、列或窗格**
使用 Aspose.Cells for Python via .NET 轻松取消窗格冻结。请使用 [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) 方法解冻窗格。

1. 构造工作簿以打开冻结文件。
2. 使用Worksheet.UnFreezePanes()方法取消窗格的冻结。
3.保存文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

附有[示例源Excel文件](Frozen.xlsx)。
