---
title: Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att direkt beräkna anpassade funktioner i Microsoft Excel utan att skriva funktionen i en arbetsbok. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att beräkna den anpassade funktionen och få resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, anpassade funktioner, direkt beräkning, ingen anledning att skriva, arbetsböcker
type: docs
weight: 90
url: /sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad**

Den här artikeln förklarar hur du kan direkt beräkna dina anpassade funktioner utan först att skriva dem i en arbetsbok. Använd [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)-metoden för detta ändamål.

Se följande exempelkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany.CustomFunction() och beräknar dess värde som "Aspose.Cells." på egen hand och sedan konkateneras detta värde automatiskt med värdet för cell A1, vilket är "Välkommen till " av beräkningsmotorn och det slutliga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i en arbetsbok och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsoloutput**

Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Implementera anpassad beräkningsmotor för att utöka standardberäkningsmotorn i Aspose.Cells](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
