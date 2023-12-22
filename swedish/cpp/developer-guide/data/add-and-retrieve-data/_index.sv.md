---
title: Lägg till och hämta data
type: docs
weight: 20
url: /sv/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 I[Åtkomst till Cells i ett arbetsblad](/cells/sv/cpp/accessing-cells-of-a-worksheet/)diskuterade vi grundläggande metoder för att komma åt celler i ett kalkylblad. Den här artikeln använder en av dessa metoder för att lägga till olika typer av data till celler.

{{% /alert %}} 
##  **Lägger till data till Cells**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass ger en[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)klass.

 Aspose.Cells tillåter utvecklare att lägga till data till cellerna i kalkylblad genom att anropa[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klass[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metod. Aspose.Cells tillhandahåller överbelastade versioner av[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metod som låter utvecklare lägga till olika typer av data till celler. Genom att använda dessa överbelastade versioner av[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)metod är det möjligt att lägga till ett booleskt, sträng-, dubbel-, heltal eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Förbättring av effektiviteten**
 Om du använder[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)metod för att lägga en stor mängd data i ett kalkylblad, bör du lägga till värden i cellerna, först efter rader och sedan efter kolumner. Detta tillvägagångssätt förbättrar effektiviteten av dina applikationer avsevärt.
##  **Hämtar data från Cells**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som ger åtkomst till kalkylblad i filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass ger en[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)klass.

 De[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)class tillhandahåller flera metoder som tillåter utvecklare att hämta värden från cellerna enligt deras datatyper. Dessa metoder inkluderar:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), returnerar strängvärdet för cellen.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), returnerar cellens dubbla värde.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), returnerar cellens booleska värde.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), returnerar cellens datum/tidsvärde.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), returnerar flytvärdet för cellen.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)returnerar cellens heltalsvärde.

 När ett fält inte är ifyllt, celler med[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) eller[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)ger ett undantag.

 Typen av data som finns i en cell kan också kontrolleras med hjälp av[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klass[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metod. Faktum är att[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klass[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metoden är baserad på[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)uppräkning vars fördefinierade värden listas nedan:

|**Cell Värdetyper**|**Beskrivning**|
| :- | :- |
|CellValueType_IsBool|Anger att cellvärdet är booleskt.|
|CellValueType_IsDateTime|Anger att cellvärdet är datum/tid.|
|CellValueType_IsNull|Representerar en tom cell.|
|CellValueType_IsNumeric|Anger att cellvärdet är numeriskt.|
|CellValueType_IsString|Anger att cellvärdet är sträng.|
|CellValueType_IsOkänd|Anger att cellvärdet är okänt.|
Du kan också använda de fördefinierade cellvärdetyperna ovan för att jämföra med typen av data som finns i varje cell.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
