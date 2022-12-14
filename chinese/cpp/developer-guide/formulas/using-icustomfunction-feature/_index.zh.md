---
title: 使用 ICustomFunction 功能
type: docs
weight: 20
url: /zh/cpp/using-icustomfunction-feature/
---
## **介绍**
本文介绍了如何使用 ICustomFunction 功能通过 Aspose.Cells API 实现自定义函数。

ICustomFunction 接口允许您添加自定义公式计算函数以扩展 Aspose.Cells 核心计算引擎以满足某些需求。此功能对于在模板文件或代码中定义自定义（用户定义）函数很有用，在该代码中自定义函数可以像任何其他默认 Microsoft Excel 函数一样使用 Aspose.Cells API 实现和评估。
## **使用 ICustomFunction 功能**
以下示例代码实现了 ICustomFunction 接口，该接口计算并返回两个自定义函数的值，即 MySampleFunc() 和 YourSampleFunc()。这些自定义函数分别位于单元格 A1 和 A2 中。然后它调用 IWorkbook.CalculateFormula(false, ICustomFunction) 方法来调用 ICustomFunction.CalculateCustomFunction() 方法的实现。然后，它在控制台上打印 A1 和 A2 的值，这些值实际上是 ICustomFunction.CalculateCustomFunction() 返回的值。请参阅下面示例代码的控制台输出以获得更多帮助。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **控制台输出**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
