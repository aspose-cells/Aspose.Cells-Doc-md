---
title: Calculation of Array Formula of Data Tables
description: How to use Aspose.Cells library to calculate array formulas for a data table in Microsoft Excel. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to calculate the array formula of the data table and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /net/calculation-of-array-formula-of-data-tables/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can create Data Table in Microsoft Excel using Data > What-If Analysis > Data Table.... Aspose.Cells now allows you to calculate the array formula of a data table. Please use [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) as normal for calculating any type of formulas.

{{% /alert %}}

In the following sample code, we used the [source excel file](5115535.xlsx). If you change the value of cell B1 to 100, the values of the Data Table which are filled with Yellow color will become 120 as shown in the following images. The sample code generates the [output PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Here is the sample code used to generate the [output PDF](5115538.pdf) from the [source excel file](5115535.xlsx). Please read the comments for more information.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
