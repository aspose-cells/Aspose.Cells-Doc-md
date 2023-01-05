---
title: Arbeta med anpassad beräkningsmotor
type: docs
weight: 70
url: /sv/net/working-with-custom-calculation-engine/
---
## **Implementera Custom Calculation Engine**

Aspose.Cells.Gridweb har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta låter den dig också utöka standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används för att implementera denna funktion.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** som har en**[Calculate(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** metod. Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**MYTESTFUNK** formeln och multiplicera med 2 för dess första parametervärde.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

