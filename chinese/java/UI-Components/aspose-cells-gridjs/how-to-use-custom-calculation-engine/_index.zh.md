---
title: 使用自定义计算引擎处理GridJs
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: 本文介绍了如何使用Aspose.Cells.GridJs库的自定义计算引擎。
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **实现自定义计算引擎**

Aspose.Cells.GridJs具有强大的计算引擎，几乎可以计算所有Microsoft Excel公式。除此之外，它还允许您扩展默认的计算引擎，从而提供更大的功能和灵活性。

在实现此功能中使用了以下属性和类。


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

以下代码实现了自定义计算引擎。它实现了[**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)接口，具有[**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)方法。调用此方法以处理所有公式。在此方法中，我们捕获了**MYTESTFUNC**公式并为其第一个参数值乘以2。

### **编程示例**

```JAVA
class MyCalculation : GridAbstractCalculationEngine
        {
           public override void calculate(GridCalculationData data)
            {
                if (!"MYTESTFUNC".Equals(data.FunctionName.ToUpper()))
                {
                    return;
                }
                data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));
            }
        }
// in the startup.cs when you do initialization ,set the CalculateEngine		
  MyCalculation ce = new MyCalculation();
  GridJsWorkbook.CalculateEngine = ce;

```
