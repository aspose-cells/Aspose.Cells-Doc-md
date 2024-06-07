---
title: 使用AbstractCalculationEngine功能
type: docs
weight: 20
url: /zh/cpp/using-abstractcalculationengine-feature/
---

## 功能仍在开发中，请继续关注。


## **介绍**
本文介绍了如何使用AbstractCalculationEngine功能使用Aspose.Cells API实现自定义函数。

<!--

The AbstractCalculationEngine interface 允许您添加自定义公式计算函数，以扩展 Aspose.Cells 核心计算引擎，以满足特定要求。此功能可用于在模板文件或代码中定义自定义（用户定义）函数，其中可以实现并使用 Aspose.Cells API 对其进行评估，就像对任何其他默认 Microsoft Excel 函数进行评估一样。
## **使用AbstractCalculationEngine功能**
以下示例代码实现了 AbstractCalculationEngine 接口，用于评估并返回两个自定义函数 MySampleFunc() 和 YourSampleFunc() 的值。这些自定义函数分别位于单元格 A1 和 A2 中。然后，调用 Workbook.CalculateFormula(const CalculationOptions& options) 方法来调用 AbstractCalculationEngine.Calculate(CalculationData& data) 方法的实现。然后，将A1和A2的值打印到控制台上。请参见下面示例代码的控制台输出，以获取更多帮助。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **控制台输出**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
