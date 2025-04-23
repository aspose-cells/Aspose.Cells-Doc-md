---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/java/managing-page-breaks/
---

{{% alert color="primary" %}}

En sidbrytning är en plats i texten där en sida slutar och den nästa börjar. Microsoft Excel kan lägga till sidbrytningar vid valfri cell i ett kalkylblad.
Sidan slutar vid den cell där sidbrytningen har lagts till och all data efter sidbrytningen skrivs ut på nästa sida. Med enkla ord delar sidbrytningar kalkylblad i flera sidor. Det går också att lägga till sidbrytningar till kalkylblad dynamiskt med hjälp av Aspose.Cells. Aspose.Cells stödjer två typer av sidbrytning:

- horisontell
- vertikal.

I den här artikeln beskrivs hur du lägger till horisontella eller vertikala sidbrytningar i kalkylblad med Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells och sidbrytningar**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) som tillhandahåller en mängd egenskaper och metoder för att hantera kalkylblad. För att lägga till sidbrytningar, använd klassernas [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) och [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) egenskaper.

Egenskaperna [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) och [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) är faktiskt samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för hantering av horisontella och vertikala sidbrytningar. Hur dessa metoder används diskuteras nedan.

## **Lägga till sidbrytningar**

För att lägga till en sidbrytning i ett kalkylblad, infoga horisontella och vertikala sidbrytningar i den angivna cellen genom att anropa samlingarnas [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) **Lägg till** -metoder. Varje **Lägg till** -metod tar cellnamnet där sidbrytningen ska läggas till.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

I sidbrytning förhandsgranskning eller utskriftsförhandsgranskning kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

## **Rensa alla sidbrytningar**

För att rensa alla sidbrytningar i ett kalkylblad, anropa samlingarnas [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) **Rensa** -metoder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Ta bort en specifik sidbrytning**

För att ta bort en specifik sidbrytning i kalkylbladet, anropa samlingarnas [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) **tar bort vid** -metoder. Varje **tar bort vid** -metod tar indexet för sidbrytningen som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Viktigt att veta**: När du ställer in anpassningen till sidans passning (det vill säga [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) och [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) i sidans inställningar), påverkas sidbrytningen, så om du skriver ut kalkylbladet, tas inte sidbrytningsinställningarna i beaktande även om de fortfarande finns i filen.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
