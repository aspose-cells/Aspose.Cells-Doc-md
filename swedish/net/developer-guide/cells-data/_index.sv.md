---
title: Hantera data i Excel filer
linktitle: Cellers data
type: docs
weight: 110
url: /sv/net/view-and-edit-excel-data/
description: Den här artikeln beskriver hur man visar och redigerar data i Excel filer med Aspose.Cells biblioteket.
keywords: Aspose.Cells C# Hantera data i Excel fil, lägg till data i Excel fil, hämta data från Excel fil, Hur man förbättrar effektiviteten vid att lägga till data, hantera cellers data, uppdatera cellers data, hämta cellers data, infoga cellers data
---

{{% alert color="primary" %}}

I [Att nå celler i ett kalkylblad](/cells/sv/net/accessing-cells-of-a-worksheet/), diskuterade vi grundläggande metoder för att nå celler i ett kalkylblad. Den här artikeln använder en av dessa metoder för att lägga till olika typer av data i celler.

{{% /alert %}}

## **Hur man lägger till data i celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en samling av typen [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en samling av typen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Varje objekt i samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representerar en instans av klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells möjliggör för utvecklare att lägga till data i cellerna i arbetsblad genom att anropa metoden [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) i klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Aspose.Cells tillhandahåller överbelastade versioner av metoden [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) som låter utvecklare lägga till olika typer av data i cellerna. Genom att använda dessa överbelastade versioner av metoden [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) är det möjligt att lägga till en boolean, sträng, dubbel, heltal eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Hur man förbättrar effektiviteten**

Om du använder metoden [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) för att lägga till en stor mängd data i ett arbetsblad, bör du först lägga till värden i cellerna rad för rad och sedan kolumn för kolumn. Detta tillvägagångssätt förbättrar avsevärt effektiviteten för dina applikationer.

## **Hur man hämtar data från celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en samling av typen [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) som möjliggör åtkomst till arbetsbladen i filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en samling av typen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Varje objekt i samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representerar en instans av klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) tillhandahåller flera egenskaper som låter utvecklare hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): returnerar cellens strängvärde.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): returnerar cellens dubbelvärde.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): returnerar cellens booleanvärde.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): returnerar cellens datum/tid-värde.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): returnerar cellens flyttalsvärde.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): returnerar cellens heltalsvärde.

När en värdetyp inte är ifylld, kastar celler med [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) eller [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) ett undantag.

Datatypen som finns i en cell kan också kontrolleras genom att använda egenskapen [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) i klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Faktum är att egenskapen [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) i klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) är baserad på uppräkningen [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|IsBool| Specificerar att cellvärdet är Booleskt.
|IsDateTime| Specificerar att cellvärdet är datum/tid.
|IsNull| Representerar en tom cell.
|IsNumeric| Specificerar att cellvärdet är numeriskt.
|IsString| Specificerar att cellvärdet är en sträng.
|IsUnknown| Specificerar att cellvärdet är okänt.

Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

När man arbetar med arbetsblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera booleska, heltal, flyttal, text eller datum/tid-värden. Med Aspose.Cells kan du hämta lämpliga värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Fortsatta ämnen**
- [Tillgång till celler i ett arbetsblad](/cells/sv/net/accessing-cells-of-a-worksheet/)
- [Konvertera text numerisk data till nummer](/cells/sv/net/convert-text-numeric-data-to-number/)
- [Skapa delsummering](/cells/sv/net/creating-subtotals/)
- [Datafiltrering](/cells/sv/net/data-filtering/)
- [Data sortering](/cells/sv/net/sort-data-of-excel/)
- [Data validering](/cells/sv/net/data-validation/)
- [Exportera data från arbetsblad](/cells/sv/net/export-data-from-worksheet/)
- [Hitta eller Sök Data](/cells/sv/net/find-or-search-data/)
- [Få cellsträngvärde med och utan formatering](/cells/sv/net/get-cell-string-value-with-and-without-formatting/)
- [Lägg till HTML Rich Text i cellen](/cells/sv/net/adding-html-rich-text-inside-the-cell/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/net/insert-hyperlinks-to-excel/)
- [Importera data till arbetsblad](/cells/sv/net/import-data-into-worksheet/)
- [Hur och var man använder uppräknare](/cells/sv/net/how-and-where-to-use-enumerators/)
- [Mät bredden och höjden på cellvärdet i enheten pixlar](/cells/sv/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Läsa cellvärden i flera trådar samtidigt](/cells/sv/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertering mellan cellnamn och rad/kolumnindex](/cells/sv/net/names-and-indices/)
- [Fylla data först per rad och sedan per kolumn](/cells/sv/net/populate-data-first-by-row-then-by-column/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Åtkomst och uppdatering av delar av riktad text från cellen](/cells/sv/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
