---
title: 使用自定义计算引擎处理GridJs
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs,custom,calculation,customcalculation
description: 本文介绍了如何使用Aspose.Cells.GridJs库的自定义计算引擎。
---

## **实现自定义计算引擎**

Aspose.Cells.GridJs具有强大的计算引擎，几乎可以计算所有Microsoft Excel公式。除此之外，它还允许您扩展默认的计算引擎，从而提供更大的功能和灵活性。

在实现此功能中使用了以下属性和类。


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

以下代码实现了自定义计算引擎。它实现了[**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)接口，具有[**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)方法。调用此方法以处理所有公式。在此方法中，我们捕获了**MYTESTFUNC**公式并为其第一个参数值乘以2。

### **编程示例**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

