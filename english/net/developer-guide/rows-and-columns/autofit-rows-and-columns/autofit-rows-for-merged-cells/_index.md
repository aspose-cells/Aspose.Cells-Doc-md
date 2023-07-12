---
title: AutoFit Rows for Merged Cells
type: docs
weight: 120
url: /net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel provides a feature that allows you to auto-size the height of a cell according to its content. The feature is called auto-fit rows. Microsoft Excel doesn't set auto-fit operation on merged cells natively. Sometimes the feature becomes vital for a user who really needs to implement auto-fit rows on merged cells too.

{{% /alert %}}

## **How to use AutoFitMergedCellsType for autofitting rows**
Aspose.Cells supports this feature through the [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/) API. Using this API, it is possible to auto-fit rows in a worksheet including merged cells. Here is a list of all possible types of auto fitting merged cells:

- None
- FirstLine
- LastLine
- EachLine

## **Autofit Rows for Merged Cells**

Please see the following code, it creates a workbook object and add multiple worksheets. Use different methods for autofit operations in each worksheet. The screenshot shows the results after the execution of the sample code.

![todo:image_alt_text](autofit_mergedcells.png)

## **C# Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
