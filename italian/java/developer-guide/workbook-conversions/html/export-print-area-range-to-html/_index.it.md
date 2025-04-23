---
title: Esportare l area di stampa in HTML
type: docs
weight: 60
url: /it/java/export-print-area-range-to-html/
---

## Possibili scenari di utilizzo

Questo è uno scenario molto comune in cui è necessario esportare solo l'area di stampa, ovvero la selezione di celle anziché l'intero foglio in HTML. Questa funzionalità è già disponibile per la resa in PDF, tuttavia, ora è possibile eseguire questa operazione anche per l'HTML. Prima, impostare l'area di stampa nell'oggetto di impostazione pagina del foglio di lavoro. Successivamente, utilizzare la proprietà [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) per esportare solo la selezione.

## Codice Java per esportare l'area di stampa in HTML

Il codice di esempio seguente carica un foglio di lavoro e quindi esporta l'area di stampa in HTML. Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

{{< app/cells/assistant language="java" >}}
