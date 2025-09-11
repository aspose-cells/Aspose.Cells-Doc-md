---
title: Showing Cell Range as the Data Labels
description: Learn how to show a range of cells as data labels in charts using Aspose.Cells for Python via .NET. Our guide will demonstrate how to link the labels to your data source and format them to provide accurate and meaningful information in your charts.
keywords: Aspose.Cells for Python via .NET, charting, data labels, cell range, data source, formatting, accuracy, meaningful information.
type: docs
weight: 130
url: /python-net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, you can display a cell range for data labels. Aspose.Cells for Python via .NET supports this feature.

{{% /alert %}}

## **Check-box to Show Cell Range as Data Labels**

To show the cell range as data labels in Microsoft Excel:

1. Select the series data labels and right-click to open the context menu.
1. Select **Format Data Labels**. Label options are displayed.
1. Select or clear the option **Label Contains - Value From Cells**.

The sample code below accesses a chart series data labels and sets the [**DataLabels.show_cell_range**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/show_cell_range) property to **true** to select the **Label Contains - Value From Cells** option.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ShowCellRangeAsDataLabels.py" >}}
{{< app/cells/assistant language="python-net" >}}