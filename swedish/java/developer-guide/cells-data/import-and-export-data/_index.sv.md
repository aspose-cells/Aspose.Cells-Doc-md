---
title: Importera och exportera data
type: docs
weight: 130
url: /sv/java/import-and-export-data/
---

{{% alert color="primary" %}}

Den här artikeln diskuterar några tekniker för dataimport och -export som utvecklare har tillgång till genom Aspose.Cells.

{{% /alert %}}

## Importera data i arbetsboken

Data representerar världen som den är. För att förstå data analyserar vi den och får en förståelse för världen. Data blir till information.

Det finns många sätt att utföra analys: att lägga in data i kalkylblad och manipulera den på olika sätt är en vanlig metod. Med Aspose.Cells är det enkelt att skapa kalkylblad som tar data från olika externa källor och förbereder dem för analys.

Den här artikeln diskuterar några metoder för dataimport som utvecklare har tillgång till genom Aspose.Cells.

### Importera data med Aspose.Cells

När du öppnar en Excel-fil med Aspose.Cells importeras automatiskt all data i filen. Aspose.Cells kan också importera data från andra datakällor:

- [Array](/cells/sv/java/import-and-export-data/).
- [Arraylist](/cells/sv/java/import-and-export-data/).
- [Resultatuppsättning](/cells/sv/java/import-and-export-data/).
- [JSON](/cells/sv/java/import-and-export-data/)

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller samlingen [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samling. [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samlingen ger mycket användbara metoder för att importera data från andra datakällor. I den här artikeln förklaras hur dessa metoder kan användas.

#### Importera från Array

För att importera data till ett kalkylblad från en array, anropa importArray-metoden i [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samlingen. Det finns många överbelastade versioner av importArray-metoden, men en vanlig överbelastning tar följande parametrar:

- **Array**, arrayobjektet som du importerar innehåll från.
- **Radnummer**, radnumret för den första cellen som datan kommer att importeras till.
- **Kolumnnummer**, kolumnnumret för den första cellen som datan kommer att importeras till.
- **Är vertikal**, ett booleskt värde som specificerar om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importera från flerdimensionella arrayer

För att importera data till ett kalkylblad från flerdimensionella arrayer, anropa den relevanta importArray-överbelastningen i [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samlingen:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importera från en ArrayList

För att importera data från en *ArrayList* till kalkylblad, anropa [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)-metoden i [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samlingen. [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)-metoden tar följande parametrar:

- **ArrayList**, *ArrayList*-objekt vars innehåll kommer att importeras.
- **Radnummer**, radnumret för den första cellen i cellintervallen från vilken innehåll kommer att importeras.
- **Kolumnnummer**, kolumnnumret för den första cellen från vilken data kommer att importeras.
- **Är vertikal**, är ett booleskt värde som specifierar om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importera från anpassade objekt till sammanfogat område

För att importera data från en samling objekt till en arbetsbok som innehåller sammanfogade celler, använd [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) egenskap. Om Excel-mallen har sammanfogade celler, ange värdet för [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) egenskap till true. Skicka med objektet [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) tillsammans med listan över kolumner/egenskaper till metoden för att visa din önskade lista med objekt. Följande kodexempel demonstrerar användningen av [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) egenskap för att importera data från anpassade objekt till sammanfogade celler. Se den bifogade [käll-Excel](90112035.xlsx)-filen och den [utdata-Excel](90112036.xlsx)-filen som referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importera data från JSON

Aspose.Cells tillhandahåller en [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-klass för bearbetning av JSON. [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-klassen har en [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)-metod för att importera JSON-data. Aspose.Cells tillhandahåller också en [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)-klass som representerar alternativen för JSON-layout. [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)-metoden accepterar [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) som en parameter. [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)-klassen tillhandahåller följande egenskaper.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Anger om arrayen ska behandlas som en tabell eller inte.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Hämtar eller anger ett värde som indikerar om strängen i JSON ska konverteras till numeriskt eller datum.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Hämtar och anger formatet för datumvärdet.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indikerar om titeln ska ignoreras om objektets egenskap är en array.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indikerar om nullvärdet ska ignoreras eller inte.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indikerar om titeln ska ignoreras om objektets egenskap är ett objekt.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Hämtar och anger formatet för numeriska värden.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Hämtar och anger stilen för titeln.

Det angivna kodexemplet demonstrerar användningen av [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)- och [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)-klasserna för att importera JSON-data.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exportera data från arbetsblad

Aspose.Cells låter inte bara sina användare importera data till arbetsblad från externa datakällor utan tillåter dem också att exportera arbetsbladsdata till en array.

### Exportera data med hjälp av Aspose.Cells - Exportera data till Array

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samling.

Data kan enkelt exporteras till ett Array-objekt med hjälp av [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-klassens [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-)-metod.

#### Kolumner som innehåller starkt typade data

Kalkylblad lagrar data som en sekvens av rader och kolumner. Använd [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-)-metoden för att exportera data från ett kalkylblad till en array. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) tar följande parametrar för att exportera kalkylbladsdata som ett *Array*-objekt:

- Radnummer, radnumret för den första cellen från vilken data ska exporteras.
- Kolumnnummer, kolumnnumret för den första cellen från vilken data ska exporteras.
- Antal rader, antalet rader att exportera.
- Antal kolumner, antalet kolumner att exportera.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Fortsatta ämnen**
- [Importera data från ResultSet-objektet i Microsoft Access-databas till kalkylbladet](/cells/sv/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Ange formelfält vid import av data till kalkylbladet](/cells/sv/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
