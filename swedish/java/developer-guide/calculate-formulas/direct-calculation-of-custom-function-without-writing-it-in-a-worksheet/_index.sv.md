---
title: Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad
type: docs
weight: 650
url: /sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Den här artikeln förklarar hur du kan direkt beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Använd [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) metoden för detta ändamål.

{{% /alert %}} 
## **Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad**
Se följande provkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter *MyCompany.CustomFunction()* och vi beräknar dess värde som "Aspose.Cells." själva och sedan läggs detta värde automatiskt samman med värdet av cell A1 som är "Welcome to " av beräkningsmotorn och det slutliga beräknade värdet returneras som "Welcome to Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i ett kalkylblad och den beräknas direkt med vår egen anpassade logik.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsoloutput**
Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Relaterad artikel**
{{% alert color="primary" %}} 

- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
