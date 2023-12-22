---
title: Excel 工作表分屏
linktitle: 分屏
type: docs
weight: 190
url: /zh/net/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将了解如何使用 C# Library 和 .NET API 以编程方式将工作表拆分为两个或四个部分，从而在单独的窗格中显示某些行和/或列。
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

在本文中，我们将学习如何通过将工作表拆分为两个或四个部分来在单独的窗格中显示某些行和/或列。
在处理大型数据集时，我们需要一次查看同一工作表的几个区域以比较不同的数据子集。
分屏功能可以满足您的需求。

{{% /alert %}}

##  **Excel中如何分屏**
要将工作表拆分为两个或四个部分，请执行以下操作：

1. 选择要在其之前放置拆分的行/列/单元格。
2. 在“视图”选项卡的“Windows”组中，单击“拆分”按钮。

**![分屏](Split-Screen.png)**

##  **按列垂直拆分工作表**

要垂直分隔电子表格的两个区域，请选择要显示拆分的列右侧的列，然后单击 Excel 中的“拆分”按钮。

使用 Aspose.Cells for .Net 可以很容易地以编程方式在列上垂直分割工作表，我们只需选择顶行中的一个单元格作为活动单元格，然后
与[**工作表.拆分**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **按行水平拆分工作表**
要水平分隔 Excel 窗口，请选择 Excel 中要进行拆分的行下方的行。

使用 Aspose.Cells for .Net 可以轻松地以编程方式按行水平拆分工作表，我们只需选择左列中的一个单元格作为活动单元格，然后
与[**工作表.拆分**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **将工作表分成四个部分**
要同时查看同一工作表的四个不同部分，请在 Excel 中垂直和水平分割屏幕。

使用 Aspose.Cells for .Net 可以很容易地以编程方式在列上垂直拆分工作表，我们只需选择不在第一行和第一列中的一个单元格作为活动单元格，然后
与[**工作表.拆分**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **如何消除裂痕**
要删除工作表拆分，只需再次单击“拆分”按钮即可。

 Aspose.Cells 为.Net提供了一个[**工作表.删除分割**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/)删除分割设置的方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}