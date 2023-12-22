---
title: 使用 AbstractCalculationEngine 功能
type: docs
weight: 20
url: /zh/cpp/using-abstractcalculationengine-feature/
---
## 功能仍在开发中，敬请期待。


##  **介绍**
本文提供了如何使用[抽象计算引擎](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)使用 Aspose.Cells API 实现自定义功能的功能。

<!--

The AbstractCalculationEngine interface allows you to add custom formula calculation functions to extend the Aspose.Cells core calculation engine in order to meet certain requirements. This feature is useful to define custom (user defined) functions in a template file or in a code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.
## **Using AbstractCalculationEngine Feature**
The following sample code implements the AbstractCalculationEngine interface which evaluates and returns the values of the two custom functions i.e. MySampleFunc() and YourSampleFunc(). These custom functions are inside the cells A1 and A2 respectively. Then it calls the Workbook.CalculateFormula(const CalculationOptions& options) method to invoke the implementation of AbstractCalculationEngine .Calculate(CalculationData& data) method. Then, it prints the values of A1 and A2 on console. Please see the Console Output of the sample code below for more help.
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **Console Output**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->