---
title: Implementera anpassad beräkningsmotor för att utöka Aspose.Cells standardberäkningsmotor
description: Den här artikeln beskriver hur man utökar standardberäkningsmotorn genom att implementera en anpassad beräkningsmotor med hjälp av Aspose.Cells biblioteket. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att implementera en anpassad beräkningsmotor och få resultaten. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, Anpassad beräkningsmotor, utökar standardberäkningsmotorn
type: docs
weight: 80
url: /sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) som har en [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)-metod. Denna metod anropas mot alla dina formler. Inne i denna metod fångar vi **TODAY**-funktionen och lägger till en dag till systemdatumet. Så om dagens datum är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Resultat**

Vänligen kolla konsolens utmatning av den ovanstående provkoden, värdet (datumtid) av A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

### **Relaterad artikel**

{{% alert color="primary" %}}

[Direkt beräkning av anpassad funktion utan att skriva den i en arbetsbok](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
