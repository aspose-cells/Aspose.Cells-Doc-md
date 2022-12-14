---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/java/managing-page-breaks/
---
{{% alert color="primary" %}}

En sidbrytning är en plats i texten där en sida slutar och nästa börjar. Microsoft Excel kan lägga till sidbrytningar i valfri vald cell i ett kalkylblad.
Sidan slutar i cellen där sidbrytningen läggs till och all data efter sidbrytningen skrivs ut på nästa sida. I enkla ord, sidbrytningar delar upp kalkylblad på flera sidor. Det är också möjligt att lägga till sidbrytningar till kalkylblad under körning med Aspose.Cells. Aspose.Cells stöder två typer av sidbrytningar:

- horisontell
- vertikal.

Den här artikeln beskriver hur man lägger till horisontella eller vertikala sidbrytningar i kalkylblad med Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells & Sidbrytningar**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass som ger ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att lägga till sidbrytningar, använd[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) och[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)egenskaper.

 De[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) och[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)egenskaper är i själva verket samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar. Hur dessa metoder används diskuteras nedan.

## **Lägga till sidbrytningar**

 För att lägga till en sidbrytning i ett kalkylblad, infoga vertikala och horisontella sidbrytningar i den angivna cellen genom att anropa[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) samlingar'**Lägg till** metoder. Varje**Lägg till**metoden tar cellnamnet där sidbrytningen ska läggas till.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

I lägena för förhandsgranskning av sidbrytningar eller förhandsgranskning av utskrifter kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

## **Rensa alla sidbrytningar**

 För att rensa alla sidbrytningar i ett kalkylblad, anropa[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) samlingar'**Klar**metoder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Ta bort specifik sidbrytning**

 För att ta bort en specifik sidbrytning i kalkylbladet ringer du[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) och[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) samlingar'**ta bortAt** metoder. Varje**ta bortAt**metod kommer att ta bort indexet för sidbrytningen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Viktigt att veta** : När du ställer in anpassningen till sidegenskaper (det vill säga[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) och[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) i sidinställningarna påverkas sidbrytningsinställningarna, så om du skriver ut kalkylbladet beaktas inte sidbrytningsinställningarna även om de fortfarande finns i filen.

{{% /alert %}}
