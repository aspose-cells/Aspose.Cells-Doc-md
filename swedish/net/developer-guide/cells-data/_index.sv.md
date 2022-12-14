---
title: Hantera data för Excel-filer.
linktitle: Cells Data
type: docs
weight: 110
url: /sv/net/view-and-edit-excel-data/
description: Den här artikeln beskriver hur du visar och redigerar data i Excel-filer med Aspose.Cells-biblioteket.
---
{{% alert color="primary" %}}

 I[Åtkomst till Cells i ett arbetsblad](/cells/sv/net/accessing-cells-of-a-worksheet/)diskuterade vi grundläggande metoder för att komma åt celler i ett kalkylblad. Den här artikeln använder en av dessa metoder för att lägga till olika typer av data till celler.

{{% /alert %}}

## **Lägger till data till Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 Aspose.Cells tillåter utvecklare att lägga till data till cellerna i kalkylblad genom att anropa[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metod. Aspose.Cells tillhandahåller överbelastade versioner av[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metod som låter utvecklare lägga till olika typer av data till celler. Genom att använda dessa överbelastade versioner av[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metod är det möjligt att lägga till ett booleskt, sträng-, dubbel-, heltal eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Förbättring av effektiviteten**

 Om du använder[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metod för att lägga en stor mängd data till ett kalkylblad, bör du lägga till värden i cellerna, först efter rader och sedan efter kolumner. Detta tillvägagångssätt förbättrar effektiviteten av dina applikationer avsevärt.

## **Hämtar data från Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till kalkylblad i filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 De[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)class tillhandahåller flera egenskaper som gör att utvecklare kan hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [**Strängvärde**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): returnerar strängvärdet för cellen.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): returnerar cellens dubbla värde.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): returnerar cellens booleska värde.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): returnerar cellens datum/tidsvärde.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): returnerar flytvärdet för cellen.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)returnerar cellens heltalsvärde.

 När ett fält inte är ifyllt, celler med[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) eller[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)ger ett undantag.

Typen av data som finns i en cell kan också kontrolleras med hjälp av[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) fast egendom. Faktum är att[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) egendom är baserad på[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)uppräkning vars fördefinierade värden är listade nedan:

|**Cell Värdetyper**|**Beskrivning**|
|:- |:- |
|IsBool|Anger att cellvärdet är booleskt.|
|IsDateTime|Anger att cellvärdet är datum/tid.|
|Är inget|Representerar en tom cell.|
|IsNumeric|Anger att cellvärdet är numeriskt.|
|IsString|Anger att cellvärdet är en sträng.|
|Är okänd|Anger att cellvärdet är okänt.|

Du kan också använda de fördefinierade cellvärdetyperna ovan för att jämföra med den typ av data som finns i varje cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

När du arbetar med kalkylblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera booleska värden, heltal, flyttal, text eller datum/tid. Med Aspose.Cells kan du få lämpliga värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Förhandsämnen**
- [Åtkomst till Cells i ett arbetsblad](/cells/sv/net/accessing-cells-of-a-worksheet/)
- [Konvertera numeriska textdata till nummer](/cells/sv/net/convert-text-numeric-data-to-number/)
- [Skapa delsummor](/cells/sv/net/creating-subtotals/)
- [Datafiltrering](/cells/sv/net/data-filtering/)
- [Datasortering](/cells/sv/net/sort-data-of-excel/)
- [Datavalidering](/cells/sv/net/data-validation/)
- [Exportera data från arbetsblad](/cells/sv/net/export-data-from-worksheet/)
- [Hitta eller sök data](/cells/sv/net/find-or-search-data/)
- [Hämta Cell String Value med och utan formatering](/cells/sv/net/get-cell-string-value-with-and-without-formatting/)
- [Lägga till HTML Rich Text i Cell](/cells/sv/net/adding-html-rich-text-inside-the-cell/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/net/insert-hyperlinks-to-excel/)
- [Importera data till arbetsblad](/cells/sv/net/import-data-into-worksheet/)
- [Hur och var man använder enumerators](/cells/sv/net/how-and-where-to-use-enumerators/)
- [Mät bredden och höjden för Cell-värdet i pixelenhet](/cells/sv/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Läser Cell Värden i flera trådar samtidigt](/cells/sv/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertering mellan cellnamn och rad-/kolumnindex](/cells/sv/net/names-and-indices/)
- [Fyll i data först efter rad och sedan efter kolumn](/cells/sv/net/populate-data-first-by-row-then-by-column/)
- [Bevara enstaka citatprefix för Cell värde eller intervall](/cells/sv/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Få åtkomst till och uppdatera delarna av Rich Text på Cell](/cells/sv/net/access-and-update-the-portions-of-rich-text-of-cell/)



