---
title: Exportera data från arbetsblad i .NET
linktitle: Exportera data från arbetsblad
type: docs
weight: 180
url: /sv/net/export-data-from-worksheet/
description: Den här artikeln förklarar hur man exporterar eller importerar data från arbetsblad till en tabell med hjälp av C#.
keywords: C# Exportera data från arbetsblad, C# Exportera data till DataTable, Kolumner med starkt typade data, Kolumner med icke starkt typade data, C# Exportera område med flagga för att hoppa över kolumnnamn, C# Hur man exporterar område med rubrik.
---

## Översikt

Den här artikeln förklarar hur du exporterar dina arbetsbladsdata till en DataTable med hjälp av C#. Den täcker följande ämnen

_Format_: **Excel**
- [C# Excel till DataTable](#csharp-excel-to-datatable)
- [C# Konvertera Excel till DataTable](#csharp-convert-excel-to-datatable)
- [C# Importera Excel till DataTable](#csharp-import-excel-to-datatable)
- [C# Exportera till DataTable från Excel](#csharp-export-to-datatable-from-excel)

_Format_: **XLS**
- [C# XLS till DataTable](#csharp-xls-to-datatable)
- [C# Konvertera XLS till DataTable](#csharp-convert-xls-to-datatable)
- [C# Importera XLS till DataTable](#csharp-import-xls-to-datatable)
- [C# Exportera till DataTable från XLS](#csharp-export-to-datatable-from-xls)

_Format_: **XLSX**
- [C# XLSX till DataTable](#csharp-xlsx-to-datatable)
- [C# Konvertera XLSX till DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importera XLSX till DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exportera till DataTable från XLSX](#csharp-export-to-datatable-from-xlsx)

_Format_: **ODS**
- [C# ODS till DataTable](#csharp-ods-to-datatable)
- [C# Konvertera ODS till DataTable](#csharp-convert-ods-to-datatable)
- [C# Importera ODS till DataTable](#csharp-import-ods-to-datatable)
- [C# Exportera till DataTable från ODS](#csharp-export-to-datatable-from-ods)

## **Hur man Exporterar Excel Data Med C#**

{{% alert color="primary" %}}

Den här artikeln diskuterar några dataskyddstekniker som utvecklare har tillgång till via Aspose.Cells.

{{% /alert %}}

## **Hur man Exporterar Data från Arbetsblad**

Aspose.Cells underlättar inte bara för sina användare att importera data till arbetsblad från externa datakällor utan tillåter dem också att exportera sitt arbetsbokdata till en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). Eftersom vi vet att [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) är en del av ADO.NET och används för att hålla data. När datan är lagrad i en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) kan den användas på alla sätt enligt användarnas krav. Utvecklare kan också lagra denna data (lagrad i [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) direkt till en databas om de önskar. Så vi kan se att det blir enklare för utvecklare att manipulera arbetsbokdatan om den exporteras till en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Hur man Exporterar Data till DataTable Med Aspose.Cells**

Utvecklare kan enkelt exportera sin arbetsbokdata till en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) objekt genom att antingen anropa [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) eller [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metod av klassen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Båda metoderna används i olika scenarier, vilket diskuteras nedan mer detaljerat.

## **Kolumner Innehållande Starkt Skriven Data**

Vi vet att en kalkylblad lagrar data som en sekvens av rader och kolumner. Om alla värden i kolumnerna på ett kalkylblad är starkt skrivna (det betyder att alla värden i en kolumn måste ha samma datatyp) då kan vi exportera kalkylbladsinnehållet genom att anropa [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metoden av klassen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metoden tar följande parametrar för att exportera kalkylbladsdata som en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) objekt:

- **Radnummer**, radnumret för den första celldatan som kommer att exporteras från.
- **Kolumnnummer**, kolumnnumret för den första cellen datan kommer att exporteras från.
- **Antal rader**, antalet rader att exportera.
- **Antal kolumner**, antalet kolumner att exportera.
- **Exportera kolumnnamn**, en boolesk egenskap som anger om datan i den första raden på kalkylbladet bör exporteras som kolumnnamn för [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) eller inte.

_Steg: Exportera Data till DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Steg:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Steg:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Steg:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Steg:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Steg:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Steg:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Steg:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Steg:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Steg:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Steg:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Steg:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Steg:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Steg:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Steg:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Steg:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Steg:</em> Export to DataTable from ODS in C#</strong></a>

_Kodsteg:_

1. Ladda din Excel-fil i [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-objektet.
   - [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-objekt kan läsa Excel-filformat som t.ex. XLS, XLSX, XLSM, ODS etc.
3. Använd det första [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)-objektet i Excel-filen.
4. Välj ditt exportområde t.ex. 7 rader och 2 kolumner som startar från 1:a cellen av **DataTable**.
5. Använd [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)-metoden för att exportera data till DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Kolumner som innehåller icke-strongly typed data**

Om alla värden i kolumnerna i ett kalkylblad inte är starkt typade (vilket innebär att värdena i en kolumn kan ha olika datatyper) kan vi exportera kalkylbladets innehåll genom att anropa [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-klassen. [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-metoden tar samma uppsättning parametrar som [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)-metoden för att exportera kalkylbladsdata som ett [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)-objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Hur man exporterar intervall med rubrik**

Data från ett intervall kan exporteras till [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) där en flagga finns för att hoppa över rubrikraden i den exporterade datan. Följande kod exporterar ett datointervall till [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) med ett argument [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) som innehåller en [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)-flagga. Den är inställd på **true** om rubrikinformationen finns, och den kommer därför inte inkluderas i datan och inställd på **false** om ingen rubrik finns och alla rader ska betraktas som data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Fortsatta ämnen**
- [Exportera Excel-data till DataTable utan formatering](/cells/sv/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportera HTML-strängvärde av celler till DataTable](/cells/sv/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportera synliga raddata från kalkylblad](/cells/sv/net/export-visible-rows-data-from-worksheet/)
- [Ignorera dolda kolumner vid export av kalkylbladsdata till data-tabell](/cells/sv/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Ändra namn automatiskt på dubbletter av kolumner vid export av kalkylbladsdata](/cells/sv/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
