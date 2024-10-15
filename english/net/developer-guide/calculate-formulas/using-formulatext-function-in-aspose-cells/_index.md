---
title: Using FormulaText function in Aspose.Cells
description: This article introduces how to use the FormulaText function in Aspose.Cells library to process formulas in Microsoft Excel. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to get and set the formula text of the cell and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText is an Excel 2013 and later function. It is not supported by previous versions like Excel 2010 or 2007 etc. As its name suggests, it prints the text of the formula which is present in a given cell. This article will show you how to make use of this function using Aspose.Cells.

{{% /alert %}} 

The following sample code shows the usage of FormulaText with Aspose.Cells. The code first writes a formula in cell A1 and then prints the text of the formula using FormulaText in cell A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}