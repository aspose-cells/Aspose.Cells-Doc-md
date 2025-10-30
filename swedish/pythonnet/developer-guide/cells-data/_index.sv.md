---
title: Hantera data i Excel filer
linktitle: Cellers data
type: docs
weight: 110
url: /sv/python-net/view-and-edit-excel-data/
description: Denna artikel beskriver hur man visar och redigerar data i Excel filer med hjälp av Aspose.Cells för Python via .NET biblioteket.
keywords: Python Excel bibliotek, Aspose.Cells för Python Hantera data i Excel fil, Python lägga till data i Excel fil, Python hämta data från Excel fil, Python Hur man förbättrar effektiviteten hos att lägga till data, Python hantera cellsdata, Python uppdatera cellsdata, Python hämta cellsdata, Python sätta in cellsdata.
---

{{% alert color="primary" %}}

I [Åtkomst celler av ett Arbetsblad](/cells/sv/python-net/accessing-cells-of-a-worksheet/), diskuterade vi grundläggande tillvägagångssätt för att komma åt celler i ett arbetsblad. Denna artikel använder en av dessa tillvägagångssätt för att lägga till olika typer av data i celler.

{{% /alert %}}

## **Hur man lägger till data i celler**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells för Python via .NET tillåter utvecklare att lägga till data i cellerna i arbetsblad genom att anropa [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassens [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)-metod. Aspose.Cells för Python via .NET tillhandahåller överbelastade versioner av [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)-metoden som låter utvecklare lägga till olika typer av data i celler. Genom att använda dessa överbelastade versioner av [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)-metoden är det möjligt att lägga till en boolesk, sträng, dubbel, heltal eller datum/tid, etc. värden i cellen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Hur man förbättrar effektiviteten**

Om du använder metoden [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) för att lägga till en stor mängd data i ett arbetsblad, bör du först lägga till värden i cellerna rad för rad och sedan kolumn för kolumn. Detta tillvägagångssätt förbättrar avsevärt effektiviteten för dina applikationer.

## **Hur man hämtar data från celler**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som tillåter åtkomst till arbetsblad i filen. Ett ark representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) tillhandahåller flera egenskaper som låter utvecklare hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): returnerar cellens strängvärde.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): returnerar cellens dubbelvärde.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): returnerar cellens booleanvärde.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): returnerar cellens datum/tid-värde.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): returnerar cellens flyttalsvärde.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): returnerar cellens heltalsvärde.

När en värdetyp inte är ifylld, kastar celler med [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) eller [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) ett undantag.

Datatypen som finns i en cell kan också kontrolleras genom att använda egenskapen [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) i klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Faktum är att egenskapen [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) i klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) är baserad på uppräkningen [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|IS_BOOL|Anger att cellvärdet är Boolesk.|
|IS_DATE_TIME|Anger att cellvärdet är datum/tid.|
|IS_NULL|Representerar en tom cell.|
|IS_NUMERIC|Anger att cellvärdet är numeriskt.|
|IS_STRING|Anger att cellvärdet är en sträng.|
|IS_ERROR|Anger att cellvärdet är ett felvärde.|
|IS_UNKNOWN|Anger att cellvärdet är okänt.|

Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

När man arbetar med arbetsblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera booleska, heltal, flyttal, text- eller datum/tidsvärden. Med Aspose.Cells för Python via .NET kan du få lämpliga värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Fortsatta ämnen**
- [Tillgång till celler i ett arbetsblad](/cells/sv/python-net/accessing-cells-of-a-worksheet/)
- [Konvertera text numerisk data till nummer](/cells/sv/python-net/convert-text-numeric-data-to-number/)
- [Skapa delsummering](/cells/sv/python-net/creating-subtotals/)
- [Datafiltrering](/cells/sv/python-net/data-filtering/)
- [Data sortering](/cells/sv/python-net/sort-data-of-excel/)
- [Data validering](/cells/sv/python-net/data-validation/)
- [Få cellsträngvärde med och utan formatering](/cells/sv/python-net/get-cell-string-value-with-format-strategy/)
- [Lägg till HTML Rich Text i cellen](/cells/sv/python-net/adding-html-rich-text-inside-the-cell/)
- [Hitta eller Sök Data](/cells/sv/python-net/find-or-search-data/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/python-net/insert-hyperlinks-to-excel/)
- [Mät bredden och höjden på cellvärdet i enheten pixlar](/cells/sv/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Konvertering mellan cellnamn och rad/kolumnindex](/cells/sv/python-net/names-and-indices/)
- [Fylla data först per rad och sedan per kolumn](/cells/sv/python-net/populate-data-first-by-row-then-by-column/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Åtkomst och uppdatering av delar av riktad text från cellen](/cells/sv/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
