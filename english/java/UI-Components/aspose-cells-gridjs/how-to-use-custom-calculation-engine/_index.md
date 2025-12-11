---  
title: Working with custom calculation engine for GridJs  
type: docs  
weight: 250  
url: /java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/  
keywords: GridJs,custom,calculation,customcalculation  
description: This article describes how to use the custom calculation engine for the Aspose.Cells.GridJs library.  
aliases:  
  - /java/aspose-cells-gridjs/customcalculation/  
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Implement Custom Calculation Engine**  

Aspose.Cells.GridJs has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine, which provides greater power and flexibility.  

The following property and classes are used in implementing this feature.  

- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)  
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)  

The following code implements the custom calculation engine. It implements the interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) which has a [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) method. This method is called for all of your formulas. Inside this method, we capture the **MYTESTFUNC** formula and multiply the first parameter’s value by 2.  

### **Programming Sample**  

```java
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
// In the Startup.cs, when you initialize, set the CalculateEngine
MyCalculation ce = new MyCalculation();
GridJsWorkbook.CalculateEngine = ce;
```
