---
title: Esportare l area di stampa in HTML
type: docs
weight: 60
url: /it/net/export-print-area-range-to/
---

## **Possibili Scenari di Utilizzo**

Questo è uno scenario comune in cui è necessario esportare solo l'area di stampa, ovvero la gamma selezionata di celle anziché l'intero foglio in HTML. Questa funzionalità è già disponibile per la resa in PDF, tuttavia, ora puoi eseguire questa attività anche per l'HTML. Imposta prima l'area di stampa nell'oggetto di impostazione pagina del foglio di lavoro. Successivamente, utilizza il flag [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) per esportare solo la gamma selezionata.

## Codice di esempio

Il codice di esempio seguente carica un libro di lavoro e quindi esporta l'area di stampa in HTML. Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
