---
title: Importera data till kalkylblad
type: docs
weight: 170
url: /sv/net/import-data-into-worksheet/
description: Lär dig hur du importerar data till kalkylblad genom Aspose.Cells for .NET API.
keywords: C# Importera data till kalkylblad, Importera data till Excel med ICellsDataTable gränssnittet, Importera data från Array, Importera data från ArrayList, Importera data från anpassade objekt, Importera data från anpassade objekt till sammanfogat område, Importera data från DataTable, Importera data från dynamiskt objekt som datakälla, Importera data från DataColumn, Importera data från DataView, Importera data från DataGrid, Importera data från GridView, Importera HTML formaterade data, Importera data från JSON
---

{{% alert color="primary" %}}

Den här artikeln diskuterar några metoder för dataimport som utvecklare har tillgång till genom Aspose.Cells.

{{% /alert %}}

## **Hur man importerar data till kalkylblad**

När du öppnar en Excel-fil med Aspose.Cells importeras automatiskt all data i filen. Aspose.Cells kan också importera data från andra datakällor.

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-kollektion som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-kollektion. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-kollektionen tillhandahåller användbara metoder för att importera data från olika datakällor. Den här artikeln förklarar hur dessa metoder kan användas.

## **Hur man importerar data till Excel med ICellsDataTable-gränssnittet**
Implementera [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) för att paketera olika datakällor, använd sedan [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) för att importera data till Excel-kalkylblad.
### **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Implementationen av klasserna *CustomerDataSource*, *Customer*, och *CustomerList* ges nedan

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Hur man importerar data till Excel från Array**

För att importera data till en kalkylblad från en array, anropa [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-kollektionen. Det finns många överbelastade versioner av [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)-metoden, men en vanlig överbelastning tar följande parametrar:

- **Array**, arrayobjektet som du importerar innehåll från.
- **Radnummer**, radnumret för den första cellen som datan kommer att importeras till.
- **Kolumnnummer**, kolumnnumret för den första cellen som datan kommer att importeras till.
- **Är vertikal**, ett booleskt värde som specificerar om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Hur man importerar data till Excel från ArrayList**

För att importera data från en *ArrayList* till kalkylblad, anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-kollektionens [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)-metod. Metoden ImportArray tar följande parametrar:

- **Array list**, representerar *ArrayList*-objektet du importerar.
- **Radnummer**, representerar radnumret för den första cellen som datan kommer att importeras till.
- **Kolumnnummer**, representerar kolumnnumret för den första cellen som datan kommer att importeras till.
- **Är vertikal**, ett booleskt värde som specificerar om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Hur man importerar data till Excel från anpassade objekt**

För att importera data från en samling av objekt till en kalkylblad, använd [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Tillhandahåll en lista med kolumner/egenskaper till metoden för att visa önskad lista med objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Hur man importerar data till Excel från anpassade objekt och kontrollerar sammanslagna områden**

För att importera data från en samling av objekt till ett kalkylblad som innehåller sammanfogade celler, använd [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) egenskap. Om Excel-mallen har sammanfogade celler, ställ in värdet på [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) egenskapen till true. Skicka med objektet [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) tillsammans med listan av kolumner/egenskaper till metoden för att visa önskad lista med objekt. Följande kodprov visar användningen av [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) egenskapen för att importera data från anpassade objekt till sammanfogade celler. Se den bifogade [käll Excel-filen](90112033.xlsx) och [utdata Excel-filen](90112034.xlsx) för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Hur man importerar data till Excel från DataTable**

För att importera data från en *DataTable*, anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionens [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)metod. Det finns många överbelastade versioner av [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) metoden men en vanlig överbelastning tar följande parametrar:

- **Datatabell**, *DataTable*-objektet som du importerar innehållet från.
- **Visa fältnamn**, anger om namnen på *DataTable*-kolumnerna ska importeras till kalkylbladet som en första rad eller inte.
- **Startcell**, representerar namnet på startcellen (till exempel "A1") från vilken du ska importera innehållet från *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Hur man importerar data till Excel från dynamiskt objekt som datakälla**

Aspose.Cells erbjuder funktioner för att arbeta med dynamiska objekt som datakälla. Det hjälper till att använda en datakälla där egenskaper läggs till dynamiskt till objekten. När egenskaperna har lagts till objektet, betraktar Aspose.Cells första posten som mallen och hanterar resten därefter. Det betyder att om någon dynamisk egenskap läggs till endast i en första post och inte till andra objekt, betraktar Aspose.Cells att alla poster i samlingen ska vara desamma.

I det här exemplet används en mallmodell som inledningsvis innehåller endast två variabler. Denna lista konverteras till lista med dynamiska objekt. Sedan läggs några ytterligare fält till den och slutligen laddas den in i arbetsboken. Arbetsboken hämtar endast de värden som finns i mall-XLSX-filen. Denna mallarbetsbok använder även Smarta Markeringar som också innehåller parametrar. Det går att få detaljer om Smarta Markeringar från följande artikel:

[Användning av Smarta Markeringar](/cells/sv/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Hur man importerar DataColumn till Excel**

En *DataTable* eller *DataView*-objekt består av en eller flera kolumner. Utvecklare kan också importera data från en eller flera kolumner i *DataTable* eller *DataView* genom att anropa [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metoden för [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionen. [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metoden accepterar en parameter av typ [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) klassen tillhandahåller en [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) egenskap som accepterar en array av kolumnindex.

Det angivna kodexemplet nedan visar användningen av [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) för att importera selektiva kolumner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Hur man importerar DataView till Excel**

För att importera data från en *DataView*, anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionens [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metod. Det finns många överbelastade versioner av [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metoden men den för DataView tar följande parametrar:

- **DataView:** *DataView*-objektet som du ska importera innehåll från.
- **Första rad:** radnumret för den första cellen som datan ska importeras till.
- **Första kolumn:** kolumnnumret för den första cellen som datan ska importeras till.
- **ImportTableOptions:** importalternativen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Hur man importerar DataGrid till Excel**

Det går att importera data från en *DataGrid* genom att anropa [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metoden för [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionen. Det finns många överbelastade versioner av [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metoden men en vanlig överbelastning tar följande parametrar:

- **Datagrid**, *DataGrid*-objektet som du importerar innehåll från.
- **Radnummer**, radnumret för den första cellen som datan ska importeras till.
- **Kolumnnummer**, kolumnnumret för den första cellen som datan ska importeras till.
- **Infoga rader**, en boolesk egenskap som anger om extra rader ska läggas till kalkylbladet för att passa datan eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Hur man importerar GridView till Excel**

För att importera data från en *GridView*-kontroll, anropa [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) metoden för [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionen.

Aspose.Cells tillåter oss att respektera HTML-formaterade värden vid import av data till kalkylarket. När HTML-tolkning är aktiverad vid import av data, konverterar Aspose.Cells HTML till motsvarande cellformatering.

## **Hur man importerar HTML-formaterade data till Excel**

Aspose.Cells tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) klass som har mycket användbara metoder för att importera data från externa datakällor. Den här artikeln visar hur man tolkar HTML-formaterad text vid import av data och konverterar HTML till formaterade cellvärden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Hur man importerar data till Excel från JSON**

Aspose.Cells tillhandahåller en [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klass för bearbetning av JSON. [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klass har en [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) metod för att importera JSON-data. Aspose.Cells tillhandahåller också en [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) klass som representerar alternativen för JSON-layout. Metoden [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) accepterar [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) som parameter. [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) klassen tillhandahåller följande egenskaper.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Anger om arrayen ska behandlas som en tabell eller inte.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Får eller ställer in ett värde som indikerar om strängen i JSON ska konverteras till numeriska eller datum.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Hämtar och anger formatet för datumvärdet.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indikerar om titeln ska ignoreras om objektets egenskap är en array
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indikerar om nullvärdet ska ignoreras eller inte.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indikerar om titeln ska ignoreras om objektets egenskap är ett objekt.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Hämtar och anger formatet för numeriska värden.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Hämtar och anger stilen för titeln.

Det givna kodexemplet nedan visar användningen av [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) och [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) klasserna för att importera JSON-data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Fortsatta ämnen**
- [Ange formelfält vid import av data till kalkylbladet](/cells/sv/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Flytta första raden ner när du lägger till rader med data till cellerna](/cells/sv/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
