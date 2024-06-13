---
title: Working with custom calculation engine
type: docs
weight: 70
url: /net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb,custom,calculation,CalculationEngine,GridAbstractCalculationEngine
description: This article introduces how to use GridAbstractCalculationEngine to customize the calculation process in GridWeb.
---

## **Implement Custom Calculation Engine**

Aspose.Cells.Gridweb has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

 
- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

The following code implements the Custom Calculation Engine. It implements the interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) which has a [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate) method. This method is called against all of your formulas. Inside this method, we capture the **MYTESTFUNC** formula and multiply by 2 for its first parameter value .

### **Programming Sample**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

