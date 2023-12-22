---
title: Exportera data från kalkylblad i .NET
linktitle: Exportera data från arbetsblad
type: docs
weight: 180
url: /sv/net/export-data-from-worksheet/
description: Den här artikeln förklarar hur du exporterar eller importerar data från kalkylblad till datatabell med C#.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
##  Översikt

Den här artikeln förklarar hur du exporterar dina kalkylbladsdata till DataTable med C#. Den täcker följande ämnen

 _Formatera_:**Excel**
- [C# Excel till DataTable](#csharp-excel-to-datatable)
- [C# Konvertera Excel till DataTable](#csharp-convert-excel-to-datatable)
- [C# Importera Excel till DataTable](#csharp-import-excel-to-datatable)
- [C# Exportera till DataTable från Excel](#csharp-export-to-datatable-from-excel)

 _Formatera_:**XLS**
- [C# XLS till DataTable](#csharp-xls-to-datatable)
- [C# Konvertera XLS till DataTable](#csharp-convert-xls-to-datatable)
- [C# Importera XLS till DataTable](#csharp-import-xls-to-datatable)
- [C# Exportera till DataTable från XLS](#csharp-export-to-datatable-from-xls)

 _Formatera_:**XLSX**
- [C# XLSX till DataTable](#csharp-xlsx-to-datatable)
- [C# Konvertera XLSX till DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importera XLSX till DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exportera till DataTable från XLSX](#csharp-export-to-datatable-from-xlsx)

 _Formatera_:**ODS**
- [C# ODS till DataTable](#csharp-ods-to-datatable)
- [C# Konvertera ODS till DataTable](#csharp-convert-ods-to-datatable)
- [C# Importera ODS till DataTable](#csharp-import-ods-to-datatable)
- [C# Exportera till DataTable från ODS](#csharp-export-to-datatable-from-ods)

##  **Hur man exporterar Excel-data med C#**

{{% alert color="primary" %}}

Den här artikeln diskuterar några dataexporttekniker som utvecklare har tillgång till via Aspose.Cells.

{{% /alert %}}

##  **Hur man exporterar data från arbetsblad**

 Aspose.Cells underlättar inte bara sina användare att importera data till kalkylblad från externa datakällor utan låter dem också exportera sina kalkylbladsdata till en[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Som vi vet det[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) är en del av ADO.NET och används för att lagra data. När uppgifterna är lagrade i en[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , den kan användas på vilket sätt som helst enligt användarnas krav. Utvecklare kan också lagra dessa data (lagrade i[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) direkt till en databas om de så önskar. Så vi kan se att det blir lättare för utvecklarna att manipulera kalkylbladsdata om de exporteras till en[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **Hur man exporterar data till datatabell med Aspose.Cells**

 Utvecklare kan enkelt exportera sina kalkylbladsdata till en[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) objekt genom att anropa antingen[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) eller[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)klass. Båda metoderna används i olika scenarier, vilka diskuteras mer i detalj nedan.

##  **Kolumner som innehåller starkt skrivna data**

 Vi vet att ett kalkylblad lagrar data som en sekvens av rader och kolumner. Om alla värden i kolumnerna i ett kalkylblad är starkt skrivna (det betyder att alla värden i en kolumn måste ha samma datatyp) kan vi exportera kalkylbladets innehåll genom att anropa[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) klass.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metod använder följande parametrar för att exportera kalkylbladsdata som[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objekt:

- *Radnummer**, radnumret för den första celldatan kommer att exporteras från.
- *Kolumnnummer**, kolumnnumret för den första cellen som data kommer att exporteras från.
- *Antal rader**, antalet rader som ska exporteras.
- *Antal kolumner**, antalet kolumner som ska exporteras.
- *Exportera kolumnnamn**, en boolesk egenskap som indikerar om data i den första raden i kalkylbladet ska exporteras som kolumnnamn för[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)eller inte.

_Steg: Exportera data till DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Steg:</em> Excel till DataTable i C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Steg:</em> XLS till DataTable i C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Steg:</em> XLSX till DataTable i C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Steg:</em> ODS till DataTable i C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Steg:</em> Konvertera Excel till DataTable i C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Steg:</em> Konvertera XLS till DataTable i C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Steg:</em> Konvertera XLSX till DataTable i C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Steg:</em> Konvertera ODS till DataTable i C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Steg:</em> Importera Excel till DataTable i C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Steg:</em> Importera XLS till DataTable i C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Steg:</em> Importera XLSX till DataTable i C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Steg:</em> Importera ODS till DataTable i C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Steg:</em> Exportera till DataTable från Excel i C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Steg:</em> Exportera till DataTable från XLS till C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Steg:</em> Exportera till DataTable från XLSX till C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Steg:</em> Exportera till DataTable från ODS till C#</strong></a>

_Kodsteg:_

1.  Ladda in din Excel-fil[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook/) objekt.
   - [Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook/) objekt kan ladda Excel-filformat t.ex. XLS, XLSX, XLSM, ODS etc.
 3. Öppna den första[Arbetsblad](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) i Excel-filen.
4. Välj ditt exportområde, t.ex. 7 rader och 2 kolumner från den första cellen i *Datatabell**.
 5. Använd[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) metod för att exportera data till DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **Kolumner som innehåller icke-starkt typade data**

 Om alla värden i kolumnerna i ett kalkylblad inte är starkt skrivna (det betyder att värdena i en kolumn kan ha olika datatyper) så kan vi exportera kalkylbladets innehåll genom att anropa[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) klass.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)metoden tar samma uppsättning parametrar som den för[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)metod för att exportera kalkylbladsdata som en[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **Hur man exporterar intervall med flagga för att hoppa över kolumnnamn**

 Data från ett intervall kan exporteras till[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) där en flagga är tillgänglig för att hoppa över rubrikraden i den exporterade datan. Följande kod exporterar en rad data till[**Datatabell**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) med ett argument[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) vilket innehåller[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) flagga. Den är inställd på**Sann** om rubrikinformation finns där kommer den därför inte att inkluderas i data och ställas in på**falsk** om ingen rubrik finns där och alla rader ska betraktas som data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **Förhandsämnen**
- [Exportera Excel-data till DataTable utan någon formatering](/cells/sv/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportera HTML strängvärde för Cells till datatabellen](/cells/sv/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportera synliga raddata från kalkylblad](/cells/sv/net/export-visible-rows-data-from-worksheet/)
- [Ignorera dolda kolumner när du exporterar kalkylbladsdata till datatabell](/cells/sv/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Byt namn på dubbletter av kolumner automatiskt när du exporterar kalkylbladsdata](/cells/sv/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
