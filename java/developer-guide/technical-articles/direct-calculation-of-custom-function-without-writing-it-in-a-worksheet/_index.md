---
title: Direct calculation of custom function without writing it in a worksheet
type: docs
weight: 650
url: /java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

This article explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) method for this purpose.

{{% /alert %}} 
#### **Direct calculation of custom function without writing it in a worksheet**
Please see the following sample code that illustrates the usage of this method. We have used a custom function named *MyCompany.CustomFunction()* and we calculate its value as "Aspose.Cells." by ourselves and then this value is automatically concatenated with the value of cell A1 which is "Welcome to " by the calculation engine and the final calculated value returns as "Welcome to Aspose.Cells.". As you can see in a code that we have not written our custom function anywhere in a worksheet and it is calculated directly by our own custom logic.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
#### **Console Output**
Below is the console output of the above sample code.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
#### **Related Article**
{{% alert color="primary" %}} 

- [Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
