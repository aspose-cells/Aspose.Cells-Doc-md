---
title: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 160
url: /it/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Scopri come adattare tutte le colonne del foglio di lavoro in una singola pagina PDF con Aspose.Cells per l API Python via .NET.
keywords: Adatta tutte le colonne del foglio di lavoro in una singola pagina PDF, adatta le colonne del foglio di lavoro in una singola pagina PDF usando Python, salva tutte le colonne in una singola pagina PDF in Python, salva tutte le colonne in una singola pagina PDF in Python
---

{{% alert color="primary" %}}

A volte si desidera generare un file PDF che adatti tutte le colonne di un foglio di lavoro in una sola pagina. La proprietà [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) fornisce questa funzionalità in modo molto semplice da utilizzare. Calcoli complessi come l'altezza e la larghezza dell'output PDF sono gestiti internamente e si basano sui dati presenti nel foglio di lavoro.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) garantisce che tutte le colonne in un foglio di lavoro siano rese in un'unica pagina PDF, anche se le righe possono espandersi su più pagine a seconda dei dati presenti nel foglio di lavoro.

Il codice di esempio qui sotto mostra come utilizzare la proprietà [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) per rendere un ampio foglio di lavoro con 100 colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Quando un dato foglio di lavoro ha molte colonne, il file PDF generato potrebbe mostrare il contenuto in dimensioni molto ridotte. È comunque leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di rappresentare il foglio di calcolo nel formato PDF. Così facendo, garantirai che i valori dipendenti dalla formula vengano ricalcolati e i valori corretti vengano rappresentati nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
