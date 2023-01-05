---
title: Hantera intervall
linktitle: Avstånd
type: docs
weight: 105
url: /sv/net/managing-ranges/
---
## **Introduktion**

Excel kan du markera flera celler med en musruta, uppsättningen av markerade celler kallas "Omfång".

Du kan till exempel klicka med vänster musknapp i Cell "A1" i Excel och sedan dra till cell "C4". Det rektangulära området du valde kan också enkelt skapas som ett objekt genom att använda Aspose.Cells.

Så här skapar du intervall, sätter värde, ställer in stil och gör fler operationer till "Range"-objektet.

## **Hantera intervall med Aspose.Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling.

### **Skapa intervall**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Sätt värde i Cells i intervallet**

Säg att du har ett cellområde som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella intervallcellerna är ordnade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Följande exempel visar hur man matar in vissa värden i cellerna i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Fast stil för Cells i serien**

Följande exempel visar hur man ställer in stilen för cellerna i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Hämta aktuell region i intervallet**

 CurrentRegion är en egenskap som returnerar ett Range-objekt som representerar den aktuella regionen.

Den aktuella regionen är ett intervall som begränsas av valfri kombination av tomma rader och tomma kolumner. Skrivskyddad.

I excel kan du få CurrentRegion-området genom att:
1. Välj ett område (område1) med musrutan.
2. Klicka på "Hem - Redigera - Hitta & Välj - Gå till Special - Aktuell region", eller använd "Ctrl+Skift+*", du kommer att se att excel automatiskt hjälper dig att välja ett område (område2), nu har du gjort det, område2 är den aktuella regionen för intervall1.

Med Aspose.Cells kan du använda egenskapen "Range.CurrentRegion" för att utföra samma funktion.

Ladda ner följande testfil, öppna den i excel, använd musrutan för att välja ett område "A1:D7", klicka sedan på "Ctrl+Skift+*", du kommer att se området "A1:C3" valt.

[aktuell_region.xlsx](current_region.xlsx)

Kör nu följande exempel, se hur det fungerar i Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Förhandsämnen**
- [Autofyll intervall av Excel-fil](/cells/sv/net/autofill-ranges/)
- [Kopiera intervall för Excel](/cells/sv/net/copy-ranges-of-Excel/)
- [Kopiera endast intervalldata](/cells/sv/net/copy-range-data-only/)
- [Kopiera intervalldata med stil](/cells/sv/net/copy-range-data-with-style/)
- [Endast kopiera intervallstil](/cells/sv/net/copy-range-style-only/)
- [Skapa Union Range](/cells/sv/net/create-union-range/)
- [Klipp och klistra intervall](/cells/sv/net/cut-and-paste-cells/)
- [Ta bort intervall](/cells/sv/net/delete-ranges-from-Excel/)
- [Få adress Cell Räkneförskjutning Hela kolumnen och hela raden i serien](/cells/sv/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga intervall](/cells/sv/net/insert-ranges-to-Excel/)
- [Sammanfoga eller ta bort sammanslagningsintervall för Cells](/cells/sv/net/merge-or-unmerge-range-of-cells/)
- [Flytta intervallet Cells i ett kalkylblad](/cells/sv/net/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och kalkylblad med omfattning av namngivna intervall](/cells/sv/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett intervall](/cells/sv/net/search-and-replace-data-in-a-range/)
