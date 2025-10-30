---
title: Direkt beräkning av anpassad funktion utan att skriva den i ett kalkylblad med Golang via C++
linktitle: Direktberäkning av anpassad funktion
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att direkt beräkna anpassade funktioner i Microsoft Excel utan att skriva funktionen i en arbetsbok. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att beräkna den anpassade funktionen och få resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, anpassade funktioner, direkt beräkning, ingen anledning att skriva, arbetsböcker
type: docs
weight: 90
url: /sv/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad**

Denna artikel förklarar hur du kan direkt beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Använd metod [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) för detta ändamål.

Vänligen se följande exempel kod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany::CustomFunction() och vi beräknar dess värde som "Aspose.Cells." själva och sedan kombineras detta automatiskt med värdet av cell A1 som är "Välkommen till" av beräkningsmotorn och det slutgiltiga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i ett kalkylblad och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Konsoloutput**

Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Implementera anpassad beräkningsmotor för att utöka den standardmässiga beräkningsmotorn för Aspose.Cells](/cells/sv/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
