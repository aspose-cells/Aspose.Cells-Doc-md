---
title: 分割Excel工作表
linktitle: 分割屏幕
type: docs
weight: 190
url: /zh/net/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式将工作表分割成两个或四个部分，并在各自窗格中显示特定行和/或列。
keywords: 冻结顶部行，冻结顶部行。
---

## **介绍**

在本文章中，我们将学习如何将工作表分割成两个或四个部分，将特定的行和/或列显示在单独的窗格中。在处理大量数据集时，我们需要一次看到同一工作表的几个区域，以比较数据的不同子集。分割屏幕功能可以满足您的需要。

## **如何在Excel中分割屏幕**
要将工作表分割成两个或四个部分，请按照以下操作：

1. 选择要分割的行/列/单元格之前的位置。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **在列上垂直拆分工作表**

要在电子表格的两个区域垂直分隔，选择要在其右侧出现分隔的列，并在Excel中单击“拆分”按钮。

通过Aspose.Cells for .Net编写程序在列上垂直拆分工作表非常容易，我们只需将顶行中的一个单元格选择为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **在行上水平拆分工作表**
要在Excel中水平分隔您的Excel窗口，请选择要在其下方发生分隔的行。

通过Aspose.Cells for .Net编写程序在行上水平拆分工作表非常容易，我们只需将左列中的一个单元格选择为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **将工作表分成四部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分屏幕。

通过Aspose.Cells for .Net编写程序在列上垂直拆分工作表非常容易，我们只需选中第一行和列之外的一个单元格作为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) 方法进行拆分。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for .Net提供了一个 [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) 方法来移除拆分设置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
{{< app/cells/assistant language="csharp" >}}
