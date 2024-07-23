---
title: Working with custom calculation engine for GridJs
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: This article describes how to use the custom calculation engine for  Aspose.Cells.GridJs library.
aliases:
  - /net/aspose-cells-gridjs/customcalculation/
  - /net/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Implement Custom Calculation Engine**

Aspose.Cells.GridJs has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

 
- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

The following code implements the Custom Calculation Engine. It implements the interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) which has a [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) method. This method is called against all of your formulas. Inside this method, we capture the **MYTESTFUNC** formula and multiply by 2 for its first parameter value .

### **Programming Sample**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
