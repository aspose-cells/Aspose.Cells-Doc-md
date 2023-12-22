---
title: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
type: docs
weight: 590
url: /zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells拥有强大的计算引擎，可以计算几乎所有Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更大的功能和灵活性。

以下属性和类用于实现此功能。

- [计算选项.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [抽象计算引擎](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [计算数据](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **实施自定义计算引擎**
以下代码实现了自定义计算引擎。它实现了接口[抽象计算引擎](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)它只有一种方法[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)）。针对您的所有公式调用此方法。在这个方法中，我们捕获**TODAY**函数并向系统日期添加一天。因此，如果当前日期是 27/07/2023，则自定义引擎会将 TODAY() 计算为 28/07/2023。

###  **编程示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **结果**

请检查上述示例代码的控制台输出，使用自定义引擎的 A1 的值（日期时间）应该比不使用自定义引擎的结果晚一天。

###  **相关文章**
{{% alert color="primary" %}} 

- [自定义函数直接计算，无需将其写入工作表](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
