---
title: Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells
description: Den här artikeln beskriver hur du utökar standardberäkningsmotorn genom att implementera en anpassad beräkningsmotor med Aspose.Cells-biblioteket. Genom att ladda en befintlig Excel-fil eller skapa en ny kan vi använda metoderna som tillhandahålls av Aspose.Cells för att implementera en anpassad beräkningsmotor och få resultaten. Slutligen sparar vi den modifierade Excel-filen på disken.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Implementera Custom Calculation Engine**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-formler. Trots detta låter den dig också utöka standardberäkningsmotorn som ger dig större kraft och flexibilitet.

Följande egenskap och klasser används för att implementera denna funktion.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Följande kod implementerar Custom Calculation Engine. Den implementerar gränssnittet**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** som har en**[Calculate(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** metod. Denna metod kallas mot alla dina formler. Inuti denna metod fångar vi**TODAY** funktion och lägg till en dag till systemdatumet. Så om det aktuella datumet är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

###  **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Resultat**

Kontrollera konsolutgången för ovanstående exempelkod, värdet (datumtid) för A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

###  **Relaterad artikel**

{{% alert color="primary" %}}

[Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
