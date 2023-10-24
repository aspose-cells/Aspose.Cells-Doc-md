---
title: Direct calculation of custom function without writing it in a worksheet
description: This article introduces how to use Aspose.Cells library to directly calculate custom functions in Microsoft Excel without writing the function in a worksheet. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the custom function and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direct calculation of custom function without writing it in a worksheet**

This topic explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) method for this purpose.

Please see the following sample code that illustrates the usage of this method. We have used a custom function named MyCompany.CustomFunction() and we calculate its value as "Aspose.Cells." by ourselves and then this value is automatically concatenated with the value of cell A1 which is "Welcome to " by the calculation engine and the final calculated value returns as "Welcome to Aspose.Cells."". As you can see in a code that we have not written our custom function anywhere in a worksheet and it is calculated directly by our own custom logic.

### **Programming Sample**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Console Output**

Below is the console output of the above sample code.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Related Article**

{{% alert color="primary" %}}

[Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
