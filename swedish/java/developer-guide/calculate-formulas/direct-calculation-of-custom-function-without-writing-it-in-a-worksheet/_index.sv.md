---
title: Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad
type: docs
weight: 650
url: /sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Den här artikeln förklarar hur du direkt kan beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Vänligen använd[Worksheet.calculateFormula(strängformel, alternativ för beräkningsalternativ)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) metod för detta ändamål.

{{% /alert %}} 
## **Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad**
Se följande exempelkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter*MyCompany.CustomFunction()*och vi beräknar dess värde som "Aspose.Cells." av oss själva och sedan sammanlänkas detta värde automatiskt med värdet för cell A1 som är "Välkommen till " av beräkningsmotorn och det slutgiltiga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i en kod har vi inte skrivit vår anpassade funktion någonstans i ett kalkylblad och den beräknas direkt av vår egen anpassade logik.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsolutgång**
Nedan är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Relaterad artikel**
{{% alert color="primary" %}} 

- [Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
