---
title: Showing Cell Range as the Data Labels with Golang via C++
linktitle: Showing Cell Range as the Data Labels
description: Learn how to show a range of cells as data labels in charts using Aspose.Cells for C++. Our guide will demonstrate how to link the labels to your data source and format them to provide accurate and meaningful information in your charts.
keywords: Aspose.Cells for C++, charting, data labels, cell range, data source, formatting, accuracy, meaningful information.
type: docs
weight: 130
url: /go-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, you can display a cell range for data labels. Aspose.Cells supports this feature.

{{% /alert %}}

## **Check-box to Show Cell Range as Data Labels**

To show the cell range as data labels in Microsoft Excel:

1. Select the series data labels and right-click to open the context menu.
1. Select **Format Data Labels**. Label options are displayed.
1. Select or clear the option **Label Contains - Value From Cells**.

The sample code below accesses a chart series data labels and sets the [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/go-cpp/datalabels/getshowcellrange/) property to **true** to select the **Label Contains - Value From Cells** option.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowingCellRangeAsTheDataLabels.go" >}}