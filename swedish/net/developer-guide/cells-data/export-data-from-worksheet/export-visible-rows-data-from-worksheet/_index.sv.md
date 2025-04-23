---
title: Exportera synliga raders data från arbetsblad
type: docs
weight: 10
url: /sv/net/export-visible-rows-data-from-worksheet/
description: Lär dig hur man exporterar synliga raders data från arbetsblad genom Aspose.Cells for .NET API.
keywords: Exportera synliga raders data till DataTable, Exportera dolda raders data till DataTable, Exportera raders data till DataTable och exkludera dolda rader, Ignorera dolda rader vid export av arbetsbladsdata till datatabell
---

{{% alert color="primary" %}}

Du kan exportera data från kalkylblad till datatabeller med hjälp av Aspose.Cells. Ibland vill du exportera endast synliga raders data. Aspose.Cells tillhandahåller ett sätt att uppnå detta. Använd [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) för att ange att du endast vill exportera synliga raders data.

{{% /alert %}}

Detta exempel visar hur man exporterar data från följande kalkylblad. Raderna 5, 6 och 7 är dolda.

| **Provdata i kalkylblad, rader 5, 6 och 7 är dolda** |
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

När data har exporterats till en datatabell med hjälp av metoden [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) och alternativet [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), kommer det se ut så här. Dolda rader visas som tomma rader

| **Dolda rader exporteras till datatabellen som tomma rader** |
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
