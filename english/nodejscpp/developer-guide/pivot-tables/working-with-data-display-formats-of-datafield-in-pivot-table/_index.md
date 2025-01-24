---
title: Working with data display formats of DataField in Pivot Table
type: docs
weight: 140
url: /nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: How to work with data display formats of DataField in Pivot Table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, Work with data display formats of DataField in Pivot Table.
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ supports all the data display formats of DataField.

{{% /alert %}}

## **How to Set "Rank Smallest to Largest" and "Rank Largest to Smallest" display format option**

Aspose.Cells for Node.js via C++ provides the ability to set the display format option for pivot fields. For this, the API provides the [**PivotField.getShowValuesSetting().setCalculationType(PivotFieldDataDisplayFormat)**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) method. To rank largest to smallest, you may call the [**PivotField.getShowValuesSetting().setCalculationType(PivotFieldDataDisplayFormat)**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) method to set [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). The following code snippet demonstrates setting the display format options.

Sample source and output files can be downloaded from here for testing the sample code:

[Source Excel File](101089332.xlsx)

[Output Excel File](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}
