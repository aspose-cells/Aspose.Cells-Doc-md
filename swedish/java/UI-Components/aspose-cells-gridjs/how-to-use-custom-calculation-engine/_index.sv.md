---
title: Arbetar med anpassad beräkningsmotor för GridJs
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: Denna artikel beskriver hur man använder den anpassade beräkningsmotorn för Aspose.Cells.GridJs bibliotek.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells.GridJs har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta kan du också utöka den förvalda beräkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) som har en [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) metod. Denna metod anropas mot alla dina formler. Inuti denna metod fångar vi **MYTESTFUNC**-formeln och multiplicerar med 2 för dess första parameter värde.

### **Programmeringsexempel**

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
