---
title: Adatta tutte le colonne del foglio di lavoro sulla singola pagina PDF
type: docs
weight: 160
url: /it/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Scopri come adattare tutte le colonne del foglio di lavoro alla singola pagina PDF con Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

 volte vuoi generare un file PDF che adatti tutte le colonne di un foglio di lavoro su un'unica pagina. IL[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) La proprietà fornisce questa funzionalità in un modo molto facile da usare. Calcoli complessi come l'altezza e la larghezza dell'output PDF vengono gestiti internamente e si basano sui dati nel foglio di lavoro.

{{% /alert %}}

##  **Adatta le colonne del foglio di lavoro alla singola pagina PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)garantisce che tutte le colonne di un foglio di lavoro vengano visualizzate in una singola pagina PDF, sebbene le righe possano espandersi su più pagine a seconda dei dati nel foglio di lavoro.

Il codice di esempio seguente mostra come utilizzare[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)proprietà per eseguire il rendering di un foglio di lavoro di grandi dimensioni di 100 colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Quando un determinato foglio di lavoro ha molte colonne, il file PDF visualizzato potrebbe mostrare il contenuto in dimensioni molto ridotte. È ancora leggibile anche se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metodo appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si garantirà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
