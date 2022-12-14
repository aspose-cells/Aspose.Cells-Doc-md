---
title: Lägg till och hämta data
type: docs
weight: 20
url: /sv/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 I[Åtkomst till Cells i ett arbetsblad](/cells/sv/cpp/accessing-cells-of-a-worksheet/)diskuterade vi grundläggande metoder för att komma åt celler i ett kalkylblad. Den här artikeln använder en av dessa metoder för att lägga till olika typer av data till celler.

{{% /alert %}} 
## **Lägger till data till Cells**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass ger en[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samling. Varje objekt i[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingen representerar ett föremål för[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)klass.

 Aspose.Cells tillåter utvecklare att lägga till data till cellerna i kalkylblad genom att anropa[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) klass[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) metod. Aspose.Cells tillhandahåller överbelastade versioner av[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) metod som låter utvecklare lägga till olika typer av data till celler. Genom att använda dessa överbelastade versioner av[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)metod är det möjligt att lägga till ett booleskt, sträng-, dubbel-, heltal eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Förbättring av effektiviteten**
 Om du använder[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)metod för att lägga en stor mängd data i ett kalkylblad, bör du lägga till värden i cellerna, först efter rader och sedan efter kolumner. Detta tillvägagångssätt förbättrar effektiviteten av dina applikationer avsevärt.
## **Hämtar data från Cells**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) samling som ger åtkomst till kalkylblad i filen. Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass ger en[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samling. Varje objekt i[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingen representerar ett föremål för[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)klass.

 De[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)class tillhandahåller flera metoder som tillåter utvecklare att hämta värden från cellerna enligt deras datatyper. Dessa metoder inkluderar:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), returnerar strängvärdet för cellen.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), returnerar cellens dubbla värde.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), returnerar cellens booleska värde.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), returnerar cellens datum/tidsvärde.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), returnerar flytvärdet för cellen.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), returnerar cellens heltalsvärde.

 När ett fält inte är ifyllt, celler med[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) eller[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)ger ett undantag.

Typen av data som finns i en cell kan också kontrolleras med hjälp av[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) klass[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) metod. Faktum är att[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) klass[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) metoden är baserad på[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)uppräkning vars fördefinierade värden är listade nedan:

|**Cell Värdetyper**|**Beskrivning**|
|:- |:- |
|CellValueType_IsBool|Anger att cellvärdet är booleskt.|
|CellValueType_IsDateTime|Anger att cellvärdet är datum/tid.|
|CellValueType_IsNull|Representerar en tom cell.|
|CellValueType_IsNumeric|Anger att cellvärdet är numeriskt.|
|CellValueType_IsString|Anger att cellvärdet är sträng.|
|CellValueType_IsOkänd|Anger att cellvärdet är okänt.|
Du kan också använda de fördefinierade cellvärdetyperna ovan för att jämföra med typen av data som finns i varje cell.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
