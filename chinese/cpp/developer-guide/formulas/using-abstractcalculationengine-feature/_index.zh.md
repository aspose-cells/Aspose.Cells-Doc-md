---
title: 使用AbstractCalculationEngine功能
type: docs
weight: 20
url: /zh/cpp/using-abstractcalculationengine-feature/
---

##功能仍在开发中，敬请期待。


## **介绍**
本文介绍如何使用[AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)功能来实现Aspose.Cells API的自定义函数。

<!--

AbstractCalculationEngine接口允许您添加自定义公式计算函数，以扩展Aspose.Cells核心计算引擎，从而满足特定要求。该功能可用于在模板文件或代码中定义自定义（用户定义）函数，其中可实现和使用Aspose.Cells API对待任何其他默认的Microsoft Excel函数一样。
## **使用AbstractCalculationEngine功能**
以下示例代码实现AbstractCalculationEngine接口，评估并返回两个自定义函数MySampleFunc()和YourSampleFunc()的值。 这些自定义函数分别位于单元格A1和A2中。 然后调用Workbook.CalculateFormula(const CalculationOptions& options)方法来调用AbstractCalculationEngine .Calculate(CalculationData& data)方法。 然后，在控制台上打印A1和A2的值。 有关更多帮助，请参阅下面示例代码的控制台输出。 
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **控制台输出**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
