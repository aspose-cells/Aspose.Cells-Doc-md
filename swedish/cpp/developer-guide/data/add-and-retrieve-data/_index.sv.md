---
title: Lägg till och hämta data
type: docs
weight: 20
url: /sv/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

I [Åtkomst till celler i ett kalkylblad](/cells/sv/cpp/accessing-cells-of-a-worksheet/), diskuterade vi grundläggande tillvägagångssätt för att komma åt celler på ett kalkylblad. Den här artikeln använder en av dessa tillvägagångssätt för att lägga till olika typer av data i celler.

{{% /alert %}} 
## **Lägga till data i celler**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. Varje objekt i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen representerar ett objekt av [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen.

Aspose.Cells tillåter utvecklare att lägga till data i cellerna i kalkylblad genom att anropa [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassens [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metod. Aspose.Cells tillhandahåller överlagrade versioner av [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metoden som låter utvecklare lägga till olika typer av data i celler. Genom att använda dessa överlagrade versioner av [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metoden är det möjligt att lägga till en Boolean, sträng, double, heltal eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Förbättra effektiviteten**
Om du använder [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metoden för att lägga till en stor mängd data i ett kalkylblad, bör du lägga till värden i cellerna, först efter rader och sedan efter kolumner. Detta tillvägagångssätt förbättrar avsevärt effektiviteten i dina applikationer.
## **Hämta data från celler**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som möjliggör åtkomst till kalkylblad i filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. Varje objekt i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen representerar ett objekt av [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen.

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen tillhandahåller flera metoder som låter utvecklare hämta värden från cellerna enligt deras datatyper. Dessa metoder inkluderar:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), returnerar cellens strängvärde.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), returnerar cellens dubbelvärde.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), returnerar cellens booleanvärde.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), returnerar cellens datum/tid-värde.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), returnerar cellens flytvärde.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), returnerar cellens heltalsvärde.

När ett fält inte är ifyllt, kastar celler med [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) eller [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) ett undantag.

Datatypen som finns i en cell kan också kontrolleras genom att använda [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassens [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metod. I själva verket är [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassens [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metod baserad på [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) uppräkningen vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|CellValueType_IsBool|Specificerar att cellvärde är Boolean.|
|CellValueType_IsDateTime|Specificerar att cellvärde är datum/tid.|
|CellValueType_IsNull|Representerar en tom cell.|
|CellValueType_IsNumeric|Specificerar att cellvärde är numeriskt.|
|CellValueType_IsString|Specificerar att cellvärde är sträng.|
|CellValueType_IsUnknown|Specificerar att cellvärde är okänt.|
Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
