---
title: 减少Cell.Calculate方法的计算时间
description: 本文介绍如何使用Aspose.Cells库来减少Microsoft Excel中单元格计算方法的计算时间。 通过加载现有的Excel文件或创建一个新文件，我们可以使用Aspose.Cells提供的方法来优化单元格计算方法并提高其性能。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 单元格计算方法, 优化, 性能, 减少计算时间
type: docs
weight: 100
url: /zh/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能的使用场景**

通常，我们建议用户调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)方法一次，然后获取单个单元格的计算值。 但有时，用户不想计算整个工作簿。 他们只想计算单个单元格。 Aspose.Cells提供[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)属性，您可以设置为**false**并且它将显著减少单个单元格的计算时间。 因为当递归属性设置为**true**时，每次调用都会重新计算单元格的依赖项。 但当递归属性为**false**时，依赖单元格仅计算一次，并且后续调用时不会再次计算。

## **减少Cell.Calculate()方法的计算时间**

以下示例代码说明了[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)属性的用法。 请使用所提供的[sample excel file](5113710.xlsx)执行此代码并检查其控制台输出。 您会发现将递归属性设置为**false**后，计算时间明显减少。 请阅读注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **控制台输出**

这是在我们的机器上使用给定的[sample excel file](5113710.xlsx)执行以上示例代码的控制台输出。 请注意，您的输出可能不同，但在将递归属性设置为**false**后经过的时间将始终少于将其设置为**true**。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
