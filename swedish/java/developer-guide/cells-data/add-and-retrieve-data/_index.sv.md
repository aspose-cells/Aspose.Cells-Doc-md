---
title: Lägg till och hämta data
type: docs
weight: 20
url: /sv/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 I[Åtkomst till Cells i ett arbetsblad](/cells/sv/java/accessing-cells-of-a-worksheet/)diskuterade vi grundläggande metoder för att komma åt celler i ett kalkylblad. Den här artikeln använder en av dessa metoder för att lägga till olika typer av data till celler.

{{% /alert %}} 
## **Lägger till data till Cells**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

 Aspose.Cells tillåter utvecklare att lägga till data till celler i kalkylblad genom att anropa[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass'[satt värde](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)fast egendom. Genom att använda[satt värde](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)egenskap, är det möjligt att lägga till booleska, sträng-, dubbel-, heltals- eller datum/tid, etc. värden till cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Förbättring av effektiviteten**
{{% alert color="primary" %}} 

 Om du använder[satt värde](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)egenskap för att lägga till en stor mängd data till ett kalkylblad, bör du lägga till värden i cellerna, först efter rader och sedan efter kolumner. Detta tillvägagångssätt förbättrar effektiviteten av dina applikationer avsevärt.

{{% /alert %}} 

När du arbetar med kalkylblad kan användare lägga till olika typer av data i cellerna. Dessa dataposter kan inkludera booleska, heltals-, flyttals-, text- eller datum-/tidsvärden. Du kan få lämpliga värden från cellerna enligt deras datatyper med Aspose.Cells.
## **Hämtar data från Cells**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Excel-fil.[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

 De[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)class tillhandahåller flera egenskaper som gör att utvecklare kan hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [Strängvärde](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), cellens strängvärde.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), returnerar cellens dubbla värde.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), cellens booleska värde.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), cellens värde för datum/tid.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), cellens flytvärde.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), cellens heltalsvärde.

 Dessutom kan typen av data som finns i en cell också kontrolleras med hjälp av[Typ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) egendom av[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass. Faktum är att[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass'[Typ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) egendom bygger på[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)uppräkning vars fördefinierade värden är listade nedan:

|**Cell Värdetyper**|**Beskrivning**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Anger att cellvärdet är booleskt.|
|[ÄR_DATUM_TID](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Anger att cellvärdet är datum/tid.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Representerar att cellen innehåller ett felvärde|
|[ÄR INGET](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Representerar en tom cell.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Anger att cellvärdet är numeriskt.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Anger att cellvärdet är en sträng.|
|[ÄR_OKÄNT](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Anger att cellvärdet är okänt.|
Du kan också använda de fördefinierade cellvärdetyperna ovan för att jämföra med typen av data som finns i varje cell.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
