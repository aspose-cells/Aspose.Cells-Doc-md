---
title: Arbetar med anpassad beräkningsmotor för GridJs
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs,custom,calculation,customcalculation
description: Denna artikel beskriver hur man använder den anpassade beräkningsmotorn för Aspose.Cells.GridJs bibliotek.
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells.GridJs har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta kan du också utöka den förvalda beräkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) som har en [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) metod. Denna metod anropas mot alla dina formler. Inuti denna metod fångar vi **MYTESTFUNC**-formeln och multiplicerar med 2 för dess första parameter värde.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

