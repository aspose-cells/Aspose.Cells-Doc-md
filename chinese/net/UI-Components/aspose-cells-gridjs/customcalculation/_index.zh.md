---
title: 使用 GridJs 的自定义计算引擎
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/customcalculation/
description: 本文介绍如何使用Aspose.Cells.GridJs库的自定义计算引擎。
---
## **实施自定义计算引擎**

Aspose.Cells.GridJs有一个强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更强大的功能和灵活性。

以下属性和类用于实现此功能。

 
- **[网格抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[网格计算数据](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

以下代码实现自定义计算引擎。它实现了接口**[网格抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**它有一个**[计算（GridCalculationData 数据）](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)**方法。针对您的所有公式调用此方法。在这个方法中，我们捕获**我的测试功能**公式并将其第一个参数值乘以 2。

### **编程范例**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
