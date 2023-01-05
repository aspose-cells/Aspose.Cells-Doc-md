---
title: Arbeta med anpassad beräkningsmotor för GridJs
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/customcalculation/
description: Den här artikeln beskriver hur du använder den anpassade beräkningsmotorn för biblioteket Aspose.Cells.GridJs.
---
## **Implementera Custom Calculation Engine**

Aspose.Cells.GridJs har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta låter den dig också utöka standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används för att implementera denna funktion.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** som har en**[Calculate(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** metod. Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**MYTESTFUNK** formeln och multiplicera med 2 för dess första parametervärde.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
