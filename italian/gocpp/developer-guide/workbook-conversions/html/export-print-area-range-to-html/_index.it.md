---
title: Esporta l intervallo di stampa in HTML con Golang via C++
linktitle: Esporta l area di stampa in HTML
type: docs
weight: 60
url: /it/go-cpp/export-print-area-range-to/
description: Impara come esportare l area di stampa in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Questo è uno scenario comune in cui è necessario esportare solo l'area di stampa, ovvero un intervallo di celle selezionato, invece di tutto il foglio in HTML. Questa funzione è già disponibile per la generazione PDF; tuttavia, ora puoi eseguire questa operazione anche per HTML. Per prima cosa, imposta l'area di stampa nell'oggetto layout della pagina del foglio di lavoro. Poi, usa il flag [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) per esportare solo l'intervallo selezionato.

## **Codice di Esempio**

Il seguente esempio di codice carica un workbook e successivamente esporta l'area di stampa in HTML. Il file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
