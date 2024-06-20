---
title: Hantera områden
linktitle: Områden
type: docs
weight: 105
url: /sv/net/managing-ranges/
---

## **Introduktion**

I Excel kan du markera flera celler med musen, det markerade celluppsättningen kallas "Område".

Till exempel kan du klicka med vänster musknapp i cellen "A1" i Excel och sedan dra till cellen "C4". Det rektangulära område du markerat kan också enkelt skapas som en objekt genom att använda Aspose.Cells.

Så här skapar du området, anger värde, ställer in stil och utför fler operationer på "Området" objektet.

## **Hantera områden med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling.

### **Skapa område**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Sätt värde i cellerna i området**

Säg att du har ett område med celler som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella områdscellerna är arrangerade sekventiellt: Område[0,0], Område[0,1], Område[0,2], Område[1,0], Område[1,1], Område[1,2], Område[2,0], Område[2,1], Område[2,2], Område[3,0], Område[3,1], Område[3,2].

Följande exempel visar hur man anger värden i cellerna i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Ställ in stil på cellerna i området**

Följande exempel visar hur man ställer in stil på cellerna i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Hämta aktuellt område av området**

CurrentRegion är en egenskap som returnerar ett områdesobjekt som representerar det aktuella området. 

Det aktuella området är ett område som begränsas av en kombination av tomma rader och tomma kolumner. Endast läsbar.

I Excel kan du få aktuellt område genom att:
1. Välj ett område (område1) med muslådan.
2. Klicka på "Hem - Redigering - Sök och markera - Gå till speciellt - Aktuellt område", eller använd "Ctrl+Skift+*", du kommer att se att Excel automatiskt hjälper dig att välja ett område (område2), nu har du gjort det, område2 är det aktuella området för område1.

Med Aspose.Cells kan du använda egenskapen "Range.CurrentRegion" för att utföra samma funktion.

Ladda ner följande testfil, öppna den i Excel, använd muslådan för att välja ett område "A1:D7", klicka sedan på "Ctrl+Skift+*", du kommer att se att område "A1:C3" är valt.

[current_region.xlsx](current_region.xlsx)

Kör nu följande exempel, se hur det fungerar i Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Fortsatta ämnen**
- [Autofyllt område i Excel-fil](/cells/sv/net/autofill-ranges/)
- [Kopiera områden i Excel](/cells/sv/net/copy-ranges-of-Excel/)
- [Kopiera områdesdata endast](/cells/sv/net/copy-range-data-only/)
- [Kopiera områdesdata med stil](/cells/sv/net/copy-range-data-with-style/)
- [Kopiera områdesstil endast](/cells/sv/net/copy-range-style-only/)
- [Skapa unionsspann](/cells/sv/net/create-union-range/)
- [Klipp och klistra område](/cells/sv/net/cut-and-paste-cells/)
- [Radera områden](/cells/sv/net/delete-ranges-from-Excel/)
- [Få adresscellsantal offset hela kolumnen och hela raden för området](/cells/sv/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga områden](/cells/sv/net/insert-ranges-to-Excel/)
- [Sammanfoga eller dela upp cellområde](/cells/sv/net/merge-or-unmerge-range-of-cells/)
- [Flytta cellområde i ett kalkylblad](/cells/sv/net/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och arbetsbladsspecifika namngivna områden](/cells/sv/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett område](/cells/sv/net/search-and-replace-data-in-a-range/)
