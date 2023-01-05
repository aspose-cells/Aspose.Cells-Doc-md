---
title: 减少Cell.Calculate方法的计算时间
type: docs
weight: 860
url: /zh/java/decrease-the-calculation-time-of-cell-calculate-method/
---
可能的使用场景

通常，我们建议用户拨打[工作簿.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) 方法一次，然后获取单个单元格的计算值。但有时，用户不想计算整个工作簿。他们只想计算单个单元格。 Aspose.Cells提供[计算选项.递归](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)您可以设置的属性**错误的**它将显着减少单个单元格的计算时间。因为当递归属性设置为**真的**，然后在每次调用时重新计算单元格的所有依赖项。但是当递归属性设置为**错误的**，则相关单元格仅计算一次，并且不会在后续调用中再次计算。
## **减少 Cell.Calculate() 方法的计算时间**
下面的示例代码说明了[计算选项.递归](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)财产。请使用给定的执行此代码[示例 excel 文件](5472288.xlsx)并检查其控制台输出。您会发现将递归属性设置为**错误的**大大减少了计算时间。另请阅读评论以更好地了解此属性。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **控制台输出**
这是使用给定的执行时上述示例代码的控制台输出[示例 excel 文件](5472288.xlsx)在我们的机器上。请注意，您的输出可能会有所不同，但将递归属性设置为**错误的**将永远小于将其设置为**真的**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
