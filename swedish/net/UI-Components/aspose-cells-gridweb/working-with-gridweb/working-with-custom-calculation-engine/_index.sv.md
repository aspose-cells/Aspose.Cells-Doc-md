---
title: Arbetar med anpassat beräkningsmotor
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, anpassad, beräkning, CalculationEngine, GridAbstractCalculationEngine
description: Den här artikeln introducerar hur man använder GridAbstractCalculationEngine för att anpassa beräkningsprocessen i GridWeb.
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells.Gridweb har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta kan du också utöka den standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) som har en [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate) metod. Denna metod anropas mot alla dina formler. Inuti denna metod fångar vi **MYTESTFUNC**-formeln och multiplicerar med 2 för dess första parameter värde.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

