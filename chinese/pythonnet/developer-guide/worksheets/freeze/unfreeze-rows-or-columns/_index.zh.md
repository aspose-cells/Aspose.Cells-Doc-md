---
title: 取消冻结行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用Aspose.Cells for Python via .NET的API以程序方式取消Excel工作表的行、列或窗格冻结。
keywords: Python Excel库，Python取消窗格冻结，Python如何取消行冻结，Python如何取消列冻结，Python如何取消窗口冻结。
---

## **介绍**

在本文章中，我们将学习如何取消冻结行、列和窗格。如果Excel文件中的工作表已经冻结，有时我们希望取消冻结工作表或调整冻结的行、列或窗格。


## **如何在Excel中取消行或列冻结**

1. 单击“查看”选项卡 > 冻结窗格 > 取消冻结窗格。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**




## **如何用Aspose.Cells for Python Excel库取消行、列或窗格冻结**
使用Aspose.Cells for Python via .NET解冻窗格很简单。请使用[**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/)方法解除窗格冻结。

1. 构造工作簿以打开冻结文件。
2. 使用Worksheet.UnFreezePanes()方法取消窗格的冻结。
3.保存文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

附有【示例源Excel文件】(Frozen.xlsx)。
