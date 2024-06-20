---
title: Lägg till och hämta data
type: docs
weight: 20
url: /sv/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

I [Åtkomst till kalkylbladets celler](/cells/sv/java/accessing-cells-of-a-worksheet/), diskuterade vi grundläggande tillvägagångssätt för att få åtkomst till celler i ett kalkylblad. Den här artikeln använder en av dessa tillvägagångssätt för att lägga till olika typer av data i celler.

{{% /alert %}} 
## **Lägga till data i celler**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells tillåter utvecklare att lägga till data i celler i kalkylblad genom att använda klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)s [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)-egenskap. Genom att använda [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)-egenskapen är det möjligt att lägga till boolska, sträng, dubbel, heltal eller datum/tid etc. värden till cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Förbättra effektiviteten**
{{% alert color="primary" %}} 

Om du använder [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)-egenskapen för att lägga till en stor mängd data i ett kalkylblad, bör du lägga till värden i cellerna först efter rader och sedan efter kolumner. Denna metod förbättrar avsevärt effektiviteten hos dina applikationer.

{{% /alert %}} 

När du arbetar med kalkylblad kan användare lägga till olika typer av data i cellerna. Dessa data kan inkludera booleska, heltal, flyttal, text eller datum/tid-värden. Du kan hämta lämpliga värden från cellerna enligt deras datatyper med hjälp av Aspose.Cells.
## **Hämta data från celler**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)som representerar en Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)tillhandahåller flera egenskaper som låter utvecklare hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), cellens strängvärde.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), returnerar cellens dubbelvärde.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), cellens booleska värde.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), cellens datum/tidsvärde.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), cellens flytvärde.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), cellens heltalsvärde.

Dessutom kan datatypen för data som finns i en cell också kontrolleras genom att använda egenskapen [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) i klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Faktum är att egenskapen [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) i klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) är baserad på uppräkningen [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) vars fördefinierade värden listas nedan

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)| Anger att cellvärdet är booleskt.
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)| Anger att cellvärdet är datum/tid.
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)| Representerar att cellen innehåller ett felvärde.
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)| Representerar en tom cell.
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)| Anger att cellvärdet är numeriskt.
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)| Anger att cellvärdet är en sträng.
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)| Anger att cellvärdet är okänt.
Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
