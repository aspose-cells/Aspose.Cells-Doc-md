---
title: Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells
type: docs
weight: 80
url: /sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Implementera Custom Calculation Engine**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta låter den dig också utöka standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används för att implementera denna funktion.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** som har en**[Calculate(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** metod. Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**Belopp** formeln och ökar dess värde med 30. Så om det beräknade värdet Aspose.Cells är 20, kommer vår anpassade motor att göra det till 50 genom att lägga till 30.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
