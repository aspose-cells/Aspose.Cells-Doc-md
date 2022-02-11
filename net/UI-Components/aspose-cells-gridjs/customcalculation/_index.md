---
title: Working with custom calculation engine for GridJs
type: docs
weight: 250
url: /net/aspose-cells-gridjs/customcalculation/
---

## **Implement Custom Calculation Engine**

Aspose.Cells.GridJs has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

 
- **[GridAbstractCalculationEngine](https://apireference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://apireference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

The following code implements the Custom Calculation Engine. It implements the interface **[GridAbstractCalculationEngine](https://apireference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** which has a **[Calculate(GridCalculationData data)](https://apireference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** method. This method is called against all of your formulas. Inside this method, we capture the **MYTESTFUNC** formula and multiply by 2 for its first parameter value .

### **Programming Sample**

```C#
class MyCalculation : GridAbstractCalculationEngine
        {
           public override void Calculate(GridCalculationData data)
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