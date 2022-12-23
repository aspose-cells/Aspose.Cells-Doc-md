---
title: Importera och exportera data
type: docs
weight: 130
url: /sv/java/import-and-export-data/
---
{{% alert color="primary" %}}

Den här artikeln diskuterar några tekniker för dataimport och -export som utvecklare har tillgång till via Aspose.Cells.

{{% /alert %}}

## Importera data till arbetsblad

Data representerar världen som den är. För att förstå data analyserar vi dem och får en förståelse för världen. Data förvandlas till information.

Det finns många sätt att utföra analys: att lägga in data i kalkylblad och manipulera dem på olika sätt är en vanlig metod. Med Aspose.Cells är det enkelt att skapa kalkylblad som tar data från en rad externa källor och förbereder dem för analys.

Den här artikeln diskuterar några dataimporttekniker som utvecklare har tillgång till via Aspose.Cells.

### Importera data med Aspose.Cells

När du öppnar en Excel-fil med Aspose.Cells importeras all data i filen automatiskt. Aspose.Cells kan också importera data från andra datakällor:

- [Array](/cells/sv/java/import-and-export-data/).
- [Array lista](/cells/sv/java/import-and-export-data/).
- [Resultatet satt](/cells/sv/java/import-and-export-data/).
- [JSON](/cells/sv/java/import-and-export-data/)

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller samlingen[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)samling ger mycket användbara metoder för att importera data från andra datakällor. Den här artikeln förklarar hur dessa metoder kan användas.

#### Importerar från Array

 För att importera data till ett kalkylblad från en array, anropar du importArray-metoden för[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)samling. Det finns många överbelastade versioner av importArray-metoden men en typisk överbelastning kräver följande parametrar:

- **Array**, arrayobjektet som du importerar innehåll från.
- **Radnummer**radnumret för den första cellen som data kommer att importeras till.
- **Kolumnnummer**, kolumnnumret för den första cellen som data kommer att importeras till.
- **Är vertikal**, ett booleskt värde som anger om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importera från flerdimensionella arrayer

 För att importera data till ett kalkylblad från flerdimensionella arrayer, anropa den relevanta importArray-överbelastningen av[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)samling:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importera från en ArrayList

 För att importera data från en*ArrayList* till kalkylblad, ring[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) metod för[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling. De[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) metod tar följande parametrar:

- **ArrayList** , den*ArrayList*objekt vars innehåll kommer att importeras.
- **Radnummer**, radnumret för den första cellen i cellintervallet från vilken innehållet kommer att importeras.
- **Kolumnnummer**, kolumnnumret för den första cellen från vilken data kommer att importeras.
- **Är vertikal**är ett booleskt värde som anger om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importera från anpassade objekt till sammanslaget område

För att importera data från en samling objekt till ett kalkylblad som innehåller sammanslagna celler, använd[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)fast egendom. Om Excel-mallen har sammanslagna celler, ställ in värdet på[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)egendom till sann. Skicka[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)objekt tillsammans med listan över kolumner/egenskaper till metoden för att visa din önskade lista med objekt. Följande kodexempel visar användningen av[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)egenskap för att importera data från anpassade objekt till sammanslagna celler. Se den bifogade[käll Excel](90112035.xlsx)filen och[utgång Excel](90112036.xlsx)fil för referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importera data från JSON

 Aspose.Cells tillhandahåller en[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) klass för bearbetning JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) klass har en[**Importera data**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) metod för att importera JSON data. Aspose.Cells tillhandahåller också en[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)klass som representerar alternativen för JSON layout. De[**Importera data**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) metod accepterar[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) som en parameter. De[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) klass ger följande egenskaper.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indikerar i arrayen bör bearbetas som en tabell eller inte.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Hämtar eller ställer in ett värde som anger om strängen i JSON ska konverteras till numerisk eller datum.
- [**Datumformat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Hämtar och ställer in formatet för datumvärdet.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indikerar om titeln ska ignoreras om objektets egenskap är en array
- [**IgnoreraNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indikerar om nollvärdet ska ignoreras eller inte.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indikerar om titeln ska ignoreras om objektets egenskap är ett objekt.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Hämtar och ställer in formatet för numeriskt värde.
- [**Titelstil**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Hämtar och ställer in stilen för titeln.

 Exempelkoden nedan visar användningen av[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) och[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) klasser för att importera JSON data.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exportera data från arbetsblad

Aspose.Cells låter inte bara sina användare importera data till kalkylblad från externa datakällor utan låter dem också exportera kalkylbladsdata till en array.

### Exportera data med Aspose.Cells - Exportera data till array

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling.

 Data kan enkelt exporteras till ett Array-objekt med hjälp av[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) klass'[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) metod.

#### Kolumner som innehåller starkt skrivna data

 Kalkylark lagrar data som en sekvens av rader och kolumner. Använd[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) metod för att exportera data från ett kalkylblad till en array.[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) tar följande parametrar för att exportera kalkylbladsdata som en*Array* objekt:

- Radnummer, radnumret för den första cellen som data kommer att exporteras från.
- Kolumnnummer, kolumnnumret för den första cellen varifrån data kommer att exporteras
- Antal rader, antalet rader som ska exporteras.
- Antal kolumner, antalet kolumner som ska exporteras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Förhandsämnen**
- [Importera data från Microsoft Access Database ResultSet Object till arbetsbladet](/cells/sv/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Ange formelfält när du importerar data till kalkylblad](/cells/sv/java/specify-formula-fields-while-importing-data-to-worksheet/)
