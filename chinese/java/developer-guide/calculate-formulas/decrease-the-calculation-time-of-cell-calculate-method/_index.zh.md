---
title: 减少Cell.Calculate方法的计算时间
type: docs
weight: 860
url: /zh/java/decrease-the-calculation-time-of-cell-calculate-method/
---


可能的使用场景

通常，我们建议用户调用[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\))方法一次，然后获取各个单元格的计算值。但有时，用户不希望计算整个工作簿，只想计算单个单元格。Aspose.Cells提供了[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)属性，您可以将其设置为**false**，这将显著减少单个单元格的计算时间。因为当递归属性设置为**true**时，那么每次调用时都会重新计算单元格的依赖项。但是，当递归属性设置为**false**时，依赖单元格仅计算一次，在后续调用中不会再次计算。
## **减少Cell.Calculate()方法的计算时间**
以下示例代码说明了[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)属性的用法。请使用给定的[示例Excel文件](5472288.xlsx)执行此代码，并检查其控制台输出。您会发现将递归属性设置为**false**后，计算时间显著减少。请阅读注释以更好地了解此属性。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **控制台输出**
在我们的计算机上执行给定[示例Excel文件](5472288.xlsx)时，这是上述示例代码的控制台输出。请注意，您的输出可能不同，但在将递归属性设置为**false**后，经过的时间将始终小于将其设置为**true**。



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
