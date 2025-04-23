---
title: Implementera anpassad beräkningsmotor för att utöka Aspose.Cells standardberäkningsmotor
type: docs
weight: 590
url: /sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementera anpassad beräkningsmotor**
Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) som har endast en metod [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate-com.aspose.cells.CalculationData-). Denna metod anropas för alla dina formler. Inuti denna metod fångar vi in ​​**TODAY**-funktionen och lägger till en dag till systemdatumet. Så om det aktuella datumet är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Resultat**

Vänligen kolla konsolens utmatning av den ovanstående provkoden, värdet (datumtid) av A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

### **Relaterad artikel**
{{% alert color="primary" %}} 

- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
