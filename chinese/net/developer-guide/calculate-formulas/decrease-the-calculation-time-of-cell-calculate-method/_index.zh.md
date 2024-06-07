---
title: 减少Cell.Calculate方法的计算时间
description: 本文介绍如何使用Aspose.Cells库减少Microsoft Excel中单元格计算方法的计算时间。通过加载现有的Excel文件或创建新文件，我们可以使用Aspose.Cells提供的方法优化单元格计算方法并提高性能。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、单元格计算方法、优化、性能、减少计算时间
type: docs
weight: 100
url: /zh/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能的使用场景**

通常，我们建议用户调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)方法一次，然后获取单个单元格的计算值。但有时用户不想计算整个工作簿。他们只想计算一个单元格。Aspose.Cells提供了一个[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)属性，您可以将其设置为**false**，这将大大减少单个单元格的计算时间。因为当递归属性设置为**true**时，每次调用时都会重新计算所有依赖的单元格。但当递归属性为**false**时，依赖单元格仅计算一次，并且在后续调用时不再计算。

## **减少Cell.Calculate()方法的计算时间**

以下示例代码演示了[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)属性的用法。请使用给定的[示例Excel文件](5113710.xlsx)执行此代码并检查其控制台输出。您将发现将递归属性设置为**false**显著减少了计算时间。请阅读注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **控制台输出**

这是在我们的机器上使用给定的[示例Excel文件](5113710.xlsx)执行上述示例代码时的控制台输出。请注意，您的输出可能不同，但设置递归属性为**false**后的经过时间始终小于将其设置为**true**。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
