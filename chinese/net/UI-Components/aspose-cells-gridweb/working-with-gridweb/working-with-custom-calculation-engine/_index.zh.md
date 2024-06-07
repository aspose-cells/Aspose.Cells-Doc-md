---
title: 使用自定义计算引擎工作
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb、自定义、计算、CalculationEngine、GridAbstractCalculationEngine
description: 本文介绍了如何使用 GridAbstractCalculationEngine 来自定义 GridWeb 中的计算过程。
---

## **实现自定义计算引擎**

Aspose.Cells.GridWeb 具有强大的计算引擎，可以计算几乎所有 Microsoft Excel 的公式。此外，它还允许您扩展默认计算引擎，为您提供更大的功率和灵活性。

实现此功能时，使用以下属性和类。


- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)**

下面的代码实现了自定义计算引擎。它实现了接口 **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)**，该接口有一个 **[Calculate(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** 方法。该方法针对所有公式调用。在该方法中，我们捕获 **MYTESTFUNC** 公式，将其第一个参数值乘以 2。

### **编程示例**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

