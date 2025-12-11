---
title: Calculation of Excel 2016 MINIFS and MAXIFS functions with Golang via C++
description: This article introduces how to use the Aspose.Cells library to calculate MINIFS and MAXIFS functions in Microsoft Excel 2016 using C++.
keywords: Aspose.Cells, Excel, 2016, MINIFS function, MAXIFS function, calculation
type: docs
weight: 300
url: /go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possible Usage Scenarios**
Microsoft Excel 2016 supports MINIFS and MAXIFS functions. These functions are not supported in Excel 2013 or earlier versions. Aspose.Cells also supports the calculation of these functions. The following screenshot illustrates the usage of these functions. Please read the red comments inside the screenshot to understand how these functions work.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calculation of Excel 2016 MINIFS and MAXIFS functions**
The following sample code loads the [sample Excel file](5115149.xlsx) and calls the [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) method to perform the formula calculation via Aspose.Cells, and then saves the results in the [output PDF](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}