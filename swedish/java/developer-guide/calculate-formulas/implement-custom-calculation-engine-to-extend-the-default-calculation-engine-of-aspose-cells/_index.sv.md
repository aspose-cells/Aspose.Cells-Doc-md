---
title: Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells
type: docs
weight: 590
url: /sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta låter den dig också utöka standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används för att implementera denna funktion.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculation Engine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Beräkningsdata](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Implementera Custom Calculation Engine**
Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet[AbstractCalculation Engine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) som bara har en metod[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**TODAY** funktion och lägg till en dag till systemdatumet. Så om det aktuella datumet är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

###  **Programmeringsexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Resultat**

Kontrollera konsolutgången för ovanstående exempelkod, värdet (datumtid) för A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

###  **Relaterad artikel**
{{% alert color="primary" %}} 

- [Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
