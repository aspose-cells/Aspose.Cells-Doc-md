---
title: Using AbstractCalculationEngine Feature
type: docs
weight: 20
url: /cpp/using-abstractcalculationengine-feature/
---


## **Introduction**
This article provides an understanding of how to use the [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) feature to implement custom functions with Aspose.Cells APIs.

The AbstractCalculationEngine interface allows you to add custom formula calculation functions to extend the Aspose.Cells core calculation engine in order to meet certain requirements. This feature is useful to define custom (user defined) functions in a template file or in a code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.

## **Using AbstractCalculationEngine Feature - 1**

The following sample code implements the AbstractCalculationEngine interface which evaluates and returns the values of the two custom functions i.e. MySampleFunc() and YourSampleFunc(). These custom functions are inside the cells A1 and A2 respectively. Then it calls the Workbook.CalculateFormula(const CalculationOptions& options) method to invoke the implementation of AbstractCalculationEngine .Calculate(CalculationData& data) method. Then, it prints the values of A1 and A2 on console. Please see the Console Output of the sample code below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **Console Output**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **Using AbstractCalculationEngine Feature - 2**

The following sample code reads a custom function from a sample file and calls the Workbook.CalculateFormula(const CalculationOptions& options) method to call the AbstractCalculationEngine .Calculate(CalculationData& data) method for further processing.

Sample file:[sample-file.xlsx](sample-file.xlsx)

## **Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
