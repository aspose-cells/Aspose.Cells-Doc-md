---
title: AutoFit Rows for Merged Cells with Golang via C++
linktitle: AutoFit Rows for Merged Cells
type: docs
weight: 120
url: /go-cpp/autofit-rows-for-merged-cells/
description: Learn how to auto-fit rows for merged cells in Excel using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

Microsoft Excel provides a feature that allows you to auto-size the height of a cell according to its content. The feature is called auto‑fit rows. Microsoft Excel doesn't set auto‑fit operation on merged cells natively. Sometimes the feature becomes vital for a user who really needs to implement auto‑fit rows on merged cells too.

{{% /alert %}}

## **How to use AutoFitMergedCellsType for autofitting rows**

Aspose.Cells supports this feature through the [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/go-cpp/autofitmergedcellstype/) API. Using this API, it is possible to auto‑fit rows in a worksheet, including merged cells. Here is a list of all possible types of auto‑fitting merged cells:

- None
- FirstLine
- LastLine
- EachLine

## **Autofit Rows for Merged Cells**

Please see the following code; it creates a workbook object and adds multiple worksheets. Use different methods for autofit operations in each worksheet. The screenshot shows the results after the execution of the sample code.

<br>
<img src="result.png" width=80% />

## **C++ Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsForMergedCells.go" >}}
{{< app/cells/assistant language="go" >}}
