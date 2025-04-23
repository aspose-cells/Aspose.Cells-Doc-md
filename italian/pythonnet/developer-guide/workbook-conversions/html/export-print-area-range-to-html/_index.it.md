---
title: Esportare l area di stampa in HTML
type: docs
weight: 60
url: /it/python-net/export-print-area-range-to/
---

## **Possibili Scenari di Utilizzo**

Questo è uno scenario comune in cui è necessario esportare solo l'area di stampa, ovvero la gamma selezionata di celle anziché l'intero foglio in HTML. Questa funzionalità è già disponibile per la resa in PDF, tuttavia, ora puoi eseguire questa attività anche per l'HTML. Imposta prima l'area di stampa nell'oggetto di impostazione pagina del foglio di lavoro. Successivamente, utilizza il flag [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) per esportare solo la gamma selezionata.

## Codice di esempio

Il codice di esempio seguente carica un libro di lavoro e quindi esporta l'area di stampa in HTML. Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
