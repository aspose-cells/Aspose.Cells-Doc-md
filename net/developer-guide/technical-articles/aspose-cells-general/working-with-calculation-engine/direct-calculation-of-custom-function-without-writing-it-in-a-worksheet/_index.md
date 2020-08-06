---
title: Direct calculation of custom function without writing it in a worksheet
type: docs
weight: 90
url: /net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direct calculation of custom function without writing it in a worksheet**
This topic explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [Worksheet.CalculateFormula(string formula, CalculationOptions opts)](https://apireference.aspose.com/net/cells/aspose.cells.worksheet/calculateformula/methods/3) method for this purpose.

Please see the following sample code that illustrates the usage of this method. We have used a custom function named MyCompany.CustomFunction() and we calculate its value as "Aspose.Cells." by ourselves and then this value is automatically concatenated with the value of cell A1 which is "Welcome to " by the calculation engine and the final calculated value returns as "Welcome to Aspose.Cells."". As you can see in a code that we have not written our custom function anywhere in a worksheet and it is calculated directly by our own custom logic.
### **Programming Sample**


{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}
### **Console Output**
Below is the console output of the above sample code.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
### **Related Article**
{{% alert color="primary" %}} 

[Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells-html/)

{{% /alert %}}
