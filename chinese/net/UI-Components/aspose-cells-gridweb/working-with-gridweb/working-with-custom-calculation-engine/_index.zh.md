---
title: 使用自定义计算引擎
type: docs
weight: 70
url: /zh/net/working-with-custom-calculation-engine/
---
## **实施自定义计算引擎**

Aspose.Cells.Gridweb有一个强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更强大的功能和灵活性。

以下属性和类用于实现此功能。

 
- **[网格抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[网格计算数据](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

以下代码实现自定义计算引擎。它实现了接口**[网格抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**它有一个**[计算（GridCalculationData 数据）](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)**方法。针对您的所有公式调用此方法。在这个方法中，我们捕获**我的测试功能**公式并将其第一个参数值乘以 2。

### **编程范例**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

