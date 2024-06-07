---
title: Excel工作表的分割屏幕
linktitle: 拆分窗口
type: docs
weight: 190
url: /zh/net/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API编程方式将工作表分割成两个或四个部分以将某些行和/或列显示在单独窗格中。
keywords: 冻结顶部行，冻结顶部行。
---

{{% alert color="primary" %}}

在本文中，我们将学习如何通过将工作表分割成两个或四个部分来显示某些行和/或列。
在处理大型数据集时，我们需要同时查看工作表的几个区域，以便比较数据的不同子集。
分割屏幕功能可以满足您的需求。

{{% /alert %}}

## **如何在Excel中拆分屏幕**
要将工作表分割成两个或四个部分，请按以下操作：

1. 选择要分割的行/列/单元格之前的行/列/单元格。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **在列上垂直拆分工作表**

要在电子表格的两个区域之间垂直分隔，选择要在其右侧出现拆分的列，然后在Excel中单击“拆分”按钮。

通过Aspose.Cells for .Net，以编程方式在列上垂直拆分工作表非常容易，我们只需要选择顶部行中的一个单元格作为活动单元格，然后
使用[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **在行上水平拆分工作表**
要在Excel中水平分隔您的窗口，请选择要在其中发生分割的行下方的行。

通过Aspose.Cells for .Net，以编程方式在行上水平拆分工作表非常容易，我们只需要选择左侧列中的一个单元格作为活动单元格，然后
使用[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **将工作表分割成四个部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分您的屏幕。

通过Aspose.Cells for .Net，以编程方式在列上垂直拆分工作表非常容易，我们只需要选择非第一行和列中的一个单元格作为活动单元格，然后
使用[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for .Net提供了一个[**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/)方法来移除拆分设置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
