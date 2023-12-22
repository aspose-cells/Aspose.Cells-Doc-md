---
title: Exportera synliga raddata från kalkylblad
type: docs
weight: 10
url: /sv/net/export-visible-rows-data-from-worksheet/
description: Lär dig hur du exporterar synliga raddata från kalkylblad via Aspose.Cells for .NET API.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Du kan exportera data från kalkylblad till datatabeller med Aspose.Cells. Ibland vill du endast exportera data från synliga rader. Aspose.Cells ger ett sätt att uppnå detta. Använd[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)för att ange att du endast vill exportera synliga raddata.

{{% /alert %}}

Det här exemplet visar hur du exporterar data från följande kalkylblad. Raderna 5, 6 och 7 är dolda.

|**Exempeldata i kalkylbladet, raderna 5, 6 och 7 är dolda**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 När data har exporterats till en datatabell med hjälp av[**Arbetsblad.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metod med[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)alternativ kommer det att se ut så här. Dolda rader plottas som tomma rader

|**Dolda rader exporteras till datatabellen som tomma rader**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
