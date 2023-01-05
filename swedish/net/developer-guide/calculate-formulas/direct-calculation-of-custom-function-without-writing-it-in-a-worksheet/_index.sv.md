---
title: Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad
type: docs
weight: 90
url: /sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad**

 Det här avsnittet förklarar hur du direkt kan beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Vänligen använd[**Worksheet.CalculateFormula(strängformel, alternativ för beräkningsalternativ)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)metod för detta ändamål.

Se följande exempelkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany.CustomFunction() och vi beräknar dess värde som "Aspose.Cells." av oss själva och sedan sammanlänkas detta värde automatiskt med värdet för cell A1 som är "Välkommen till " av beräkningsmotorn och det slutgiltiga beräknade värdet returneras som "Välkommen till Aspose.Cells." Som du kan se i en kod som vi har inte skrivit vår anpassade funktion någonstans i ett kalkylblad och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsolutgång**

Nedan är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
