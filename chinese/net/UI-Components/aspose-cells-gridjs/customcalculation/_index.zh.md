---
title: 使用GridJs的自定义计算引擎工作
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs，custom，calculation，customcalculation
description: 本文描述了如何为Aspose.Cells.GridJs库使用自定义计算引擎。
---

## **实现自定义计算引擎**

Aspose.Cells.GridJs具有强大的计算引擎，几乎可以计算所有Microsoft Excel公式。尽管如此，它还允许您扩展默认的计算引擎，从而为您提供更大的动力和灵活性。

实现此功能时，使用以下属性和类。


- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

以下代码实现了自定义计算引擎。它实现了接口**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**，该接口具有**[Calculate(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)**方法。该方法在所有公式上调用。在此方法内，我们捕获了**MYTESTFUNC**公式，并将其第一个参数值乘以2。

### **编程示例**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

