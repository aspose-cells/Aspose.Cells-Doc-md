---
title: Calculation of Array Formula of Data Tables with Golang via C++
linktitle: Calculation of Array Formula of Data Tables
description: How to use Aspose.Cells library to calculate array formulas for a data table in Microsoft Excel with Golang via C++. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to calculate the array formula of the data table and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations, C++
type: docs
weight: 70
url: /go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

You can create a data table in Microsoft Excel using **Data > What‑If Analysis > Data Table**. Aspose.Cells now allows you to calculate the array formula of a data table. Please use [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) as usual for calculating any type of formulas.

{{% /alert %}}

In the following sample code, we used the [source Excel file](5115535.xlsx). If you change the value of cell **B1** to **100**, the values of the data table that are filled with yellow color will become **120**, as shown in the following images. The sample code generates the [output PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Here is the sample code used to generate the [output PDF](5115538.pdf) from the [source Excel file](5115535.xlsx). Please read the comments for more information.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}