---
title: Specify Maximum Rows of Shared Formula with Golang via C++
linktitle: Specify Maximum Rows of Shared Formula
type: docs
weight: 40
url: /go-cpp/specify-maximum-rows-of-shared-formula/
description: Learn how to specify the maximum rows of shared formula in Excel files using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**

The default maximum rows of the shared formula are 64. It could be any number, e.g., 1000. The performance of the shared formula changes with different numbers of rows. Therefore, Aspose.Cells provides the [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrowsofsharedformula/) property that can be used to specify the maximum rows of the shared formula. The shared formula will be split into several shared formulae if the total rows of the shared formula are greater than it, as shown in the following screenshot.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Specify Maximum Rows of Shared Formula**

The following sample code explains the usage of the [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrowsofsharedformula/) property. It sets the maximum rows of the shared formula to 5, adds the shared formula in cell D1 for 100 rows, and saves to the *output Excel file*. If you extract the contents of the output Excel file and check the *sheet1.xml*, you will see the shared formula splits after every 5 rows, as highlighted in the above screenshot.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyMaximumRowsOfSharedFormula.go" >}}
{{< app/cells/assistant language="go" >}}
