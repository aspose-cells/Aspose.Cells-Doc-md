---
title: Implementera en anpassad beräkningsmotor för att utöka den standarda beräkningsmotorn i Aspose.Cells med Golang via C++
linktitle: Implementera anpassad beräkningsmotor
description: Denna artikel beskriver hur man utökar den default beräkningsmotorn genom att implementera en anpassad beräkningsmotor med Aspose.Cells biblioteket med Golang via C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda Aspose.Cells metoder för att implementera en anpassad beräkningsmotor och få resultaten. Slutligen sparar vi den ändrade Excel filen till disk.
keywords: Aspose.Cells, Excel, Anpassad beräkningsmotor, utökar den standardmässiga beräkningsmotorn, C++
type: docs
weight: 80
url: /sv/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) som har en [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/)-metod. Denna metod anropas mot alla dina formler. Inne i denna metod fångar vi **TODAY**-funktionen och lägger till en dag till systemdatumet. Så om dagens datum är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **Resultat**

Vänligen kolla konsolens utmatning av den ovanstående provkoden, värdet (datumtid) av A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

### **Relaterad artikel**

{{% alert color="primary" %}}

[Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad](/cells/sv/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
