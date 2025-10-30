---
title: Hantera data i Excel filer
linktitle: Cellers data
type: docs
weight: 110
url: /sv/nodejs-cpp/view-and-edit-excel-data/
description: Denna artikel beskriver hur man kan visa och redigera data i Excel filer med Aspose.Cells biblioteket för Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Hantera data i Excel fil, lägg till data i Excel fil, hämta data från Excel, hur man förbättrar effektiviteten vid dataintryck, hantera celldata, uppdatera celler, hämta cellernas data, infoga celler
---

{{% alert color="primary" %}}

I [Åtkomst av celler i ett kalkylblad](/cells/sv/nodejs-cpp/accessing-cells-of-a-worksheet/) diskuterades grundläggande metoder för att komma åt celler i ett kalkylblad. Denna artikel använder en av dessa metoder för att lägga till olika typer av data i celler.

{{% /alert %}}

## **Hur man lägger till data i celler**

Aspose.Cells for Node.js via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.

Aspose.Cells tillåter utvecklare att lägga till data till cellerna i kalkylbladen genom att anropa [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-metod. Aspose.Cells erbjuder överlagrade versioner av [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-metoden som låter utvecklare lägga till olika typer av data i celler. Med dessa överlagrade versioner av [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-metoden kan man lägga till ett Boolean-värde, sträng, double, heltal eller datum/tid m.m. i en cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Hur man förbättrar effektiviteten**

Om du använder [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-metoden för att lägga mycket data i en arbetsblad, bör du lägga till värden till cellerna först radvis och sedan kolumnvis. Detta förbättrar kraftigt effektiviteten i dina applikationer.

## **Hur man hämtar data från celler**

Aspose.Cells for Node.js via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till arbetsblad i filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.

Klassen [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) tillhandahåller flera egenskaper som gör att utvecklare kan hämta värden från celler baserat på deras datatyp. Dessa egenskaper inkluderar:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): returnerar cellens värde som sträng.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): returnerar cellens dubbla värde.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): returnerar cellens booleanvärde.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): returnerar cellens datum/tid-värde.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): returnerar cellens flyttal värde.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): returnerar cellens heltalsvärde.

När ett fält inte är ifyllt, kastar celler med [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) eller [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) ett fel.

Typen av data som finns i en cell kan också kontrolleras med [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)-metod. Faktum är att [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)-metod är baserad på [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype)-uppräkningen vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|IsBool| Specificerar att cellvärdet är Booleskt.
|IsDateTime| Specificerar att cellvärdet är datum/tid.
|IsNull| Representerar en tom cell.
|IsNumeric| Specificerar att cellvärdet är numeriskt.
|IsString| Specificerar att cellvärdet är en sträng.
|IsUnknown| Specificerar att cellvärdet är okänt.

Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

När man arbetar med kalkylblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera Boolean, heltal, flyttal, text eller datum/tid. Med Aspose.Cells kan du få rätt värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Fortsatta ämnen**
- [Tillgång till celler i ett arbetsblad](/cells/sv/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Konvertera text numerisk data till nummer](/cells/sv/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Skapa delsummering](/cells/sv/nodejs-cpp/creating-subtotals/)
- [Datafiltrering](/cells/sv/nodejs-cpp/data-filtering/)
- [Data sortering](/cells/sv/nodejs-cpp/sort-data-of-excel/)
- [Data validering](/cells/sv/nodejs-cpp/data-validation/)
- [Hitta eller Sök Data](/cells/sv/nodejs-cpp/find-or-search-data/)
- [Få cellsträngvärde med och utan formatering](/cells/sv/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Lägg till HTML Rich Text i cellen](/cells/sv/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Hur och var man använder uppräknare](/cells/sv/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Mät bredden och höjden på cellvärdet i enheten pixlar](/cells/sv/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Läsa cellvärden i flera trådar samtidigt](/cells/sv/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertering mellan cellnamn och rad/kolumnindex](/cells/sv/nodejs-cpp/names-and-indices/)
- [Fylla data först per rad och sedan per kolumn](/cells/sv/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Åtkomst och uppdatering av delar av riktad text från cellen](/cells/sv/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
