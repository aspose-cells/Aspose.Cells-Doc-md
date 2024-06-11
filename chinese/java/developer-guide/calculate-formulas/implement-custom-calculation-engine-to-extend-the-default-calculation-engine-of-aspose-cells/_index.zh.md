---
title: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
type: docs
weight: 590
url: /zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells具有强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认的计算引擎，从而为您提供更大的动力和灵活性。

在实现此功能中使用了以下属性和类。

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **实现自定义计算引擎**
以下代码实现了自定义计算引擎。它实现了接口[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)，该接口只有一个方法[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\))。此方法针对所有公式进行调用。在此方法中，我们捕获了**TODAY**函数，并将系统日期加一天。因此，如果当前日期是2023年07月27日，那么自定义引擎将计算TODAY()为2023年07月28日。

### **编程示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **结果**

请检查上述示例代码的控制台输出，具有自定义引擎的 A1 的值（日期时间）应该比没有自定义引擎的结果晚一天。

### **相关文章**
{{% alert color="primary" %}} 

- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
