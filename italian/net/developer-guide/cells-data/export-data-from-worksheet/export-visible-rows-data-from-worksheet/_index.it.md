---
title: Esporta dati di righe visibili dal foglio di lavoro
type: docs
weight: 10
url: /it/net/export-visible-rows-data-from-worksheet/
description: Scopri come esportare i dati delle righe visibili dal foglio di lavoro tramite Aspose.Cells for .NET API.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 È possibile esportare dati da fogli di lavoro in tabelle di dati utilizzando Aspose.Cells. A volte si desidera esportare solo i dati delle righe visibili. Aspose.Cells fornisce un modo per raggiungere questo obiettivo. Usa il[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)per specificare che si desidera esportare solo i dati delle righe visibili.

{{% /alert %}}

Questo esempio mostra come esportare i dati dal seguente foglio di lavoro. Le righe 5, 6 e 7 sono nascoste.

|**I dati di esempio nel foglio di lavoro, le righe 5, 6 e 7 sono nascoste**|
| :- |
|![cose da fare:immagine_alt_testo](export-visible-rows-data-from-worksheet_1.png)|

 Una volta esportati i dati in una tabella dati utilizzando il file[**Foglio di lavoro.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metodo con il[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)opzione, apparirà così. Le righe nascoste vengono tracciate come righe vuote

|**Le righe nascoste vengono esportate nella tabella dati come righe vuote**|
| :- |
|![cose da fare:immagine_alt_testo](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
