---
title: Autopassa rader och kolumner
type: docs
weight: 20
url: /sv/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel låter användare automatiskt anpassa bredden och höjden på celler enligt dess innehåll. Den här funktionen är också tillgänglig via Aspose.Cells så att utvecklare kan automatiskt anpassa storleken på en cell under körning.

{{% /alert %}}

## **Autopassning**

Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Den här artikeln handlar om att använda[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass för att automatiskt anpassa rader eller kolumner.

### **AutoFit Row - Enkel**

 Det enklaste sättet att automatiskt anpassa bredden och höjden på en rad är att anropa[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) metod. De[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)metoden tar ett radindex (för raden som ska storleksändras) som en parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **AutoFit-rad i intervallet Cells**

 En rad består av många kolumner. Aspose.Cells tillåter utvecklare att automatiskt anpassa en rad baserat på innehållet i ett antal celler inom raden genom att anropa en överbelastad version av[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)metod. Den kräver följande parametrar:

- **Radindex**, indexet för raden som ska anpassas automatiskt.
- **Första kolumnindex**, indexet för radens första kolumn.
- **Sista kolumnindex**, indexet för radens sista kolumn.

 De[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)metod kontrollerar innehållet i alla kolumner i raden och anpassar sedan raden automatiskt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **AutoFit-kolumn i intervallet Cells**

 En kolumn består av många rader. Det är möjligt att automatiskt anpassa en kolumn baserat på innehållet i ett antal celler i kolumnen genom att anropa en överbelastad version av[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)metod som tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som ska anpassas automatiskt.
- **Första radens index**, indexet för kolumnens första rad.
- **Sista radens index**, indexet för kolumnens sista rad.

 De[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)metod kontrollerar innehållet i alla rader i kolumnen och anpassar sedan kolumnen automatiskt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **AutoFit-rader för sammanslagna Cells**

 Med Aspose.Cells är det möjligt att autopassa rader även för celler som har slagits samman med hjälp av[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)API.[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)klass ger[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) egenskap som kan användas för att automatiskt anpassa rader för sammanslagna celler.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)accepterar[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerable som har följande medlemmar.

- Ingen: Ignorera sammanslagna celler.
- FirstLine: Expanderar endast höjden på den första raden.
- LastLine: Expanderar endast höjden på den sista raden.
- Varje rad: utökar endast höjden på varje rad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Du kan också försöka använda de överbelastade versionerna av[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) metoder som accepterar ett intervall av rader/kolumner och en instans av[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) för att automatiskt anpassa de valda raderna/kolumnerna med dina önskade[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)följaktligen.

Signaturerna för ovannämnda metoder är följande:

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)alternativ)
1.  AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)alternativ)

{{% /alert %}}

## **Viktigt att veta**

{{% alert color="primary" %}}

Om en cell slås samman kommer inte AutoFit-metoderna att tillämpas, vilket är samma beteende som i Microsoft Excel. Du kan komma runt detta genom att använda Autofilter API. Dessutom, om texten i en cell är radbruten,[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) metod kommer inte heller att tillämpas. En annan sak du behöver veta är att*Autopassning*metoder är tidskrävande. Så du bör anropa dessa metoder så sällan som möjligt för att säkerställa effektiviteten i din applikation.

{{% /alert %}}

## **Förhandsämnen**
- [AutoFit-rader för sammanslagna Cells](/cells/sv/net/autofit-rows-for-merged-cells/)
