---  
title: Showing Cell Range as Data Labels  
description: Learn how to show a range of cells as data labels in charts using Aspose.Cells for .NET. This guide demonstrates how to link the labels to your data source and format them to provide accurate and meaningful information in your charts.  
keywords: Aspose.Cells for .NET, charting, data labels, cell range, data source, formatting, accuracy, meaningful information.  
type: docs  
weight: 130  
url: /net/showing-cell-range-as-the-data-labels/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

In Microsoft Excel 2013, you can display a cell range for data labels. Aspose.Cells supports this feature.  

{{% /alert %}}  

## **Check box to Show Cell Range as Data Labels**  

To show the cell range as data labels in Microsoft Excel:  

1. Select the series data labels and right‑click to open the context menu.  
2. Select **Format Data Labels**. Label options are displayed.  
3. Select or clear the **Label Contains – Value From Cells** option.  

The sample code below accesses the data labels of a chart series and sets the [**DataLabels.ShowCellRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/showcellrange) property to **true** to enable the **Label Contains – Value From Cells** option.  

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ShowCellRangeAsDataLabels-ShowCellRangeAsDataLabels.cs" >}}  
{{< app/cells/assistant language="csharp" >}}
