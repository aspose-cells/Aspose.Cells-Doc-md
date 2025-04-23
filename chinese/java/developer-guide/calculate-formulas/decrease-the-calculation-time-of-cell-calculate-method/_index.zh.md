---
title: 减少Cell.Calculate方法的计算时间
type: docs
weight: 860
url: /zh/java/decrease-the-calculation-time-of-cell-calculate-method/
---


可能的使用场景

通常，我们建议用户调用 [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) 方法一次，然后获取各个单元格的计算值。但有时，用户不想计算整个工作簿，只想计算单个单元格。Aspose.Cells 提供了 [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) 属性，您可以将其设置为 **false**，这将显著减少单个单元格的计算时间。当递归属性设置为 **true** 时，所有单元格的依赖项在每次调用时都将重新计算。当设置为 **false** 时，依赖单元格只会计算一次，后续调用不会再次计算。
## **减少Cell.Calculate()方法的计算时间**
以下示例代码演示了[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)属性的使用。请使用提供的[sample excel file](5472288.xlsx)执行此代码，并检查其控制台输出。您会发现，将递归属性设置为**false**后，计算时间显著减少。还请阅读注释以更好地理解此属性。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **控制台输出**
这是在我们的计算机上使用给定的[sample excel file](5472288.xlsx)执行上述示例代码的控制台输出。请注意，您的输出可能有所不同，但在将递归属性设置为**false**后，经过的时间总是少于将其设置为**true**。



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
