---
title: 分割Excel工作表
linktitle: 分割屏幕
type: docs
weight: 190
url: /zh/python-net/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何通过拆分工作表，将其分成两部分或四部分，并以编程方式显示特定的行和/或列，使用 Aspose.Cells for Python via .NET API。
keywords: Python Excel 库，Python 冻结顶部行，Python 冻结顶部行，Python 纵向拆分工作表（基于列），Python 横向拆分工作表（基于行），Python 将工作表拆成四部分，Python 如何移除拆分。
---

## **介绍**

在本文章中，我们将学习如何将工作表分割成两个或四个部分，将特定的行和/或列显示在单独的窗格中。在处理大量数据集时，我们需要一次看到同一工作表的几个区域，以比较数据的不同子集。分割屏幕功能可以满足您的需要。

## **如何在Excel中分割屏幕**
要将工作表分割成两个或四个部分，请按照以下操作：

1. 选择要分割的行/列/单元格之前的位置。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **如何纵向拆分工作表（基于列）**

要在电子表格的两个区域垂直分隔，选择要在其右侧出现分隔的列，并在Excel中单击“拆分”按钮。

使用 Aspose.Cells for Python via .NET，轻松进行纵向拆分，只需在顶部行选择一个单元格作为活动单元格，然后
使用 [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **如何横向拆分工作表（基于行）**
要在Excel中水平分隔您的Excel窗口，请选择要在其下方发生分隔的行。

使用 Aspose.Cells for Python via .NET，轻松进行横向拆分，只需在左侧列选择一个单元格作为活动单元格，然后
使用 [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **如何将工作表拆分成四部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分屏幕。

使用 Aspose.Cells for Python via .NET 可以轻松实现编程方式沿列垂直拆分工作表，我们只需将非第一行和列的一个单元格设为活动单元格，然后
使用 [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for Python via .NET 提供 [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) 方法用于移除拆分设置。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
