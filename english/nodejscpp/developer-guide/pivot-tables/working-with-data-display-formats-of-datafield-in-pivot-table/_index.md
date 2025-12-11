---
title: Working with data display formats of DataField in Pivot Table
type: docs
weight: 140
url: /nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ supports all the data display formats of DataField.

{{% /alert %}}

## **"Rank Smallest to Largest" and "Rank Largest to Smallest" display format option**

Aspose.Cells provides the ability to set the display format option for pivot fields. For this, the API provides the [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) property. To rank largest to smallest, you may set the [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) property to [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). The following code snippet demonstrates setting the display format options.

Sample source and output files can be downloaded from here for testing the sample code:

[Source Excel File](101089332.xlsx)

[Output Excel File](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
