---
title: Esporta i dati delle righe visibili dal foglio di calcolo
type: docs
weight: 10
url: /it/net/export-visible-rows-data-from-worksheet/
description: Scopri come esportare i dati delle righe visibili dal foglio di calcolo attraverso la API Aspose.Cells for .NET.
keywords: Esporta i dati delle righe visibili nella DataTable, esporta i dati delle righe non nascosti nella DataTable, esporta i dati delle righe nella DataTable ed escludi le righe nascoste, Ignora le righe nascoste durante l esportazione dei dati del foglio di calcolo nella DataTable
---

{{% alert color="primary" %}}

Puoi esportare i dati dai fogli di calcolo nelle tabelle utilizzando Aspose.Cells. A volte vuoi esportare solo i dati delle righe visibili. Aspose.Cells fornisce un modo per raggiungere questo. Utilizza il [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) per specificare che desideri esportare solo i dati delle righe visibili.

{{% /alert %}}

Questo esempio mostra come esportare i dati dal foglio di calcolo seguente. Le righe 5, 6 e 7 sono nascoste.

|**Dati di esempio nel foglio di lavoro, le righe 5, 6 e 7 sono nascoste**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Una volta che i dati sono esportati in una tabella utilizzando il metodo [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) con l'opzione [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), apparirà così. Le righe nascoste sono visualizzate come righe vuote

|**Le righe nascoste vengono esportate nella tabella dei dati come righe vuote**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
