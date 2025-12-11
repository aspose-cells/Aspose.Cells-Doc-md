---
title: Settings for workbook
type: docs
weight: 250
url: /net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: This article describes the workbook settings in GridWeb.
keywords: GridWeb,settings
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

There are some settings we can specify by setting **GridWorkbookSettings**:

- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

| **Name** | **Description** |
| :- | :- |
| MaxIteration | Gets or sets the maximum number of iterations to resolve a circular reference; the default value is 100. |
| Iteration | Gets or sets whether to use iteration to resolve circular references. |
| ForceFullCalculate | Gets or sets whether to fully calculate every time a calculation is triggered. |
| CreateCalcChain | Gets or sets whether to create a calculated formulas chain. Default is false. |
| ReCalculateOnOpen | Gets or sets whether to recalculate all formulas when opening a file. |
| PrecisionAsDisplayed | True if calculations in this workbook will be done using only the precision of the numbers as they're displayed. |
| Date1904 | Gets or sets a value that indicates whether the workbook uses the 1904 date system. |
| CheckCustomNumberFormat | Gets or sets whether to check custom number format when setting Style.Custom. |
| Author | Gets and sets the author of the file. |

For example, the following code sets **ReCalculateOnOpen** to false to stop the calculation when opening the file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

The following code sets the author for the file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
