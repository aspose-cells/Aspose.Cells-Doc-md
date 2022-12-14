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
## **Implementera Custom Calculation Engine**
Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet[AbstractCalculation Engine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) som bara har en metod[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**BELOPP** formeln och ökar dess värde med 30. Så om det beräknade värdet Aspose.Cells är 20, kommer vår anpassade motor att göra det till 50 genom att lägga till 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Relaterad artikel**
{{% alert color="primary" %}} 

- [Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
