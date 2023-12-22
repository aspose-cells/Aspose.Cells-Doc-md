---
title: Importera data till arbetsblad
type: docs
weight: 170
url: /sv/net/import-data-into-worksheet/
description: Lär dig hur du importerar data till kalkylblad via Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

Den här artikeln diskuterar några dataimporttekniker som utvecklare har tillgång till via Aspose.Cells.

{{% /alert %}}

##  **Hur man importerar data till arbetsblad**

När du öppnar en Excel-fil med Aspose.Cells importeras all data i filen automatiskt. Aspose.Cells kan också importera data från andra datakällor.

Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling ger användbara metoder för att importera data från olika datakällor. Den här artikeln förklarar hur dessa metoder kan användas.

##  **Hur man importerar data till Excel med ICellsDataTable-gränssnittet**
 Genomföra[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) att slå in dina olika datakällor och använd sedan[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) för att importera data till Excel-kalkylblad.
###  **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Genomförandet av*CustomerDataSource*, *Customer* och *CustomerList* klasser ges nedan

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Hur man importerar data till Excel från Array**

 För att importera data till ett kalkylblad från en array, anropa[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling. Det finns många överbelastade versioner av[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)metod men en typisk överbelastning tar följande parametrar:

- *Array**, arrayobjektet som du importerar innehåll från.
- *Radnummer**, radnumret för den första cellen som data kommer att importeras till.
- *Kolumnnummer**, kolumnnumret för den första cellen som data kommer att importeras till.
- *Är vertikal**, ett booleskt värde som anger om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **Hur man importerar data till Excel från ArrayList**

 För att importera data från en*ArrayList* till kalkylblad, ring[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)metod. ImportArray-metoden tar följande parametrar:

-  *Arraylista**, representerar*ArrayList*objektet du importerar.
- *Radnummer**, representerar radnumret för den första cellen som data kommer att importeras till.
- *Kolumnnummer**, representerar kolumnnumret för den första cellen som data kommer att importeras till.
- *Är vertikal**, ett booleskt värde som anger om data ska importeras vertikalt eller horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Hur man importerar data till Excel från anpassade objekt**

 För att importera data från en samling objekt till ett kalkylblad, använd[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Ange en lista med kolumner/egenskaper till metoden för att visa önskad lista med objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Hur man importerar data till Excel från anpassade objekt till sammanslagna område**

För att importera data från en samling objekt till ett kalkylblad som innehåller sammanslagna celler, använd[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) fast egendom. Om Excel-mallen har sammanslagna celler, ställ in värdet på[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)egendom till sann. Skicka[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) objekt tillsammans med listan över kolumner/egenskaper till metoden för att visa din önskade lista med objekt. Följande kodexempel visar användningen av[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) egenskap för att importera data från anpassade objekt till sammanslagna celler. Se den bifogade[käll Excel](90112033.xlsx) filen och[utgång Excel](90112034.xlsx) fil för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **Hur man importerar data till Excel från DataTable**

För att importera data från en *DataTable*, anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) metod. Det finns många överbelastade versioner av[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)metod men en typisk överbelastning tar följande parametrar:

-  *Datatabell**, den*Datatabell* objekt som du importerar innehållet från.
-  *Visas fältnamn**, anger om namnen på*Datatabell*kolumner ska importeras till kalkylbladet som en första rad eller inte.
- *Startcell**, representerar namnet på startcellen (till exempel "A1") varifrån innehållet i *DataTable* ska importeras.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Hur man importerar data till Excel från dynamiskt objekt som datakälla**

Aspose.Cells tillhandahåller funktioner för att arbeta med dynamiska objekt som datakälla. Det hjälper till att använda datakälla där egenskaper läggs dynamiskt till objekten. När egenskaperna har lagts till i objektet, betraktar Aspose.Cells den första posten som mallen och hanterar resten därefter. Det betyder att om någon dynamisk egenskap endast läggs till ett första objekt och inte till andra objekt, anser Aspose.Cells att alla objekt i samlingen bör vara desamma.

det här exemplet används en mallmodell som initialt endast innehåller två variabler. Denna lista konverteras till Lista över dynamiska objekt. Sedan läggs ytterligare ett fält till i den och läses slutligen in i arbetsboken. Arbetsboken väljer endast de värden som finns i mallen XLSX-filen. Den här mallarbetsboken använder smarta markörer som också innehåller parametrar. Parametrar låter dig ändra hur informationen är upplagd. Detaljer om Smart Markers kan erhållas från följande artikel:

[Använda smarta markörer](/cells/sv/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **Hur man importerar data till Excel från DataColumn (.NET)**

A *Datatabell*eller*DataView*objektet består av en eller flera kolumner. Utvecklare kan också importera data från vilken kolumn/kolumn som helst i*Datatabell*eller*DataView*genom att ringa till[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling. De[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)metod accepterar en parameter av typen[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). De[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) klass ger en[**Kolumnindex**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)egenskap som accepterar en rad kolumnindex.

Exempelkoden nedan visar användningen av[**ImportTableOptions.ColumnIndex**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)för att importera selektiva kolumner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **Hur man importerar data till Excel från DataView (.NET)**

 För att importera data från en *DataView*, ring[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metod. Det finns många överbelastade versioner av[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)metod men den för DataView tar följande parametrar:

- **DataView:** De*DataView*objekt som du håller på att importera innehåll från.
- **Första raden:**radnumret för den första cellen som data kommer att importeras till.
- **Första kolumnen:**kolumnnumret för den första cellen som data kommer att importeras till.
- **Importera tabellalternativ:**Importalternativen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **Hur man importerar data till Excel från DataGrid (.NET)**

 Det är möjligt att importera data från en*Datanätet* genom att ringa till[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling. Det finns många överbelastade versioner av[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)metod men en typisk överbelastning tar följande parametrar:

-  *Data rutnät**, den*Datanätet*objekt som du importerar innehåll från.
- *Radnummer**, radnumret för den första cellen som data kommer att importeras till.
- *Kolumnnummer**, kolumnnumret för den första cellen som data kommer att importeras till.
- *Infoga rader**, en boolesk egenskap som indikerar om extra rader ska läggas till i kalkylbladet för att passa data eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **Hur man importerar data till Excel från GridView**

 För att importera data från en*GridView* kontroll, ring till[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling.

Aspose.Cells tillåter oss att respektera HTML formaterade värden när vi importerar data till kalkylarket. När HTML-tolkning är aktiverad när data importeras, konverterar Aspose.Cells HTML till motsvarande cellformatering.

##  **Hur man importerar HTML-formaterad data till Excel**

 Aspose.Cells tillhandahåller en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)klass som ger mycket användbara metoder för att importera data från externa datakällor. Den här artikeln visar hur du tolkar HTML-formaterad text medan du importerar data och konverterar HTML till formaterade cellvärden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **Hur man importerar data till Excel från JSON**

Aspose.Cells tillhandahåller en[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klass för bearbetning JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klass har en[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) metod för att importera JSON data. Aspose.Cells tillhandahåller också en[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) klass som representerar alternativen för JSON layout. De[**Importera data**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)metoden accepterar[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)som en parameter. De[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)klass ger följande egenskaper.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indikerar i arrayen bör bearbetas som en tabell eller inte.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Hämtar eller ställer in ett värde som anger om strängen i JSON ska konverteras till numerisk eller datum.
- [**Datumformat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Hämtar och ställer in formatet för datumvärdet.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indikerar om titeln ska ignoreras om objektets egenskap är en array
- [**IgnoreraNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indikerar om nollvärdet ska ignoreras eller inte.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indikerar om titeln ska ignoreras om objektets egenskap är ett objekt.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Hämtar och ställer in formatet för numeriskt värde.
- [**Titelstil**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Hämtar och ställer in stilen för titeln.

Exempelkoden nedan visar användningen av[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) och[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)klasser för att importera JSON data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Förhandsämnen**
- [Ange formelfält när du importerar data till kalkylblad](/cells/sv/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Flytta första raden nedåt när du infogar Cells datatabellrader](/cells/sv/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
