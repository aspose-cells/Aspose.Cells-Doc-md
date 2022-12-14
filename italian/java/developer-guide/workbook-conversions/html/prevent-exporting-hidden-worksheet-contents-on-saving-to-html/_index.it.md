---
title: Impedisci l'esportazione di contenuti nascosti del foglio di lavoro durante il salvataggio in HTML
type: docs
weight: 90
url: /it/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Puoi salvare le cartelle di lavoro di Excel in HTML. Tuttavia, se la cartella di lavoro contiene fogli di lavoro nascosti, Aspose.Cells per impostazione predefinita esporta il contenuto del foglio di lavoro nascosto nell'output HTML (_ files) directory che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, l'esportazione del contenuto dei fogli di lavoro nascosti in questo modo non è appropriata. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non devono essere esportate nel file_cartella dei file.

{{% /alert %}}

Aspose.Cells fornisce il[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) proprietà. Per impostazione predefinita, il[**Esporta foglio di lavoro nascosto**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) proprietà è impostata su**VERO**. Se lo imposti su**falso**, quindi Aspose.Cells non esporterà i contenuti nascosti del foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Oltre a controllare se esportare o meno i fogli di lavoro nascosti, puoi anche configurare impostazioni aggiuntive per l'esportazione della cartella di lavoro in HTML. Gli articoli seguenti illustrano altre funzionalità supportate da Aspose.Cells per l'esportazione di cartelle di lavoro in HTML.

- [Converti Excel in HTML con intestazioni](/cells/it/java/convert-excel-to-html-with-headings/)
- [Escludi stili inutilizzati durante la conversione da Excel a HTML](/cells/it/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Esporta commenti durante il salvataggio del file Excel in HTML](/cells/it/java/export-comments-while-saving-excel-file-to-html/)
- [Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML](/cells/it/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Esporta uno stile del bordo simile quando lo stile del bordo non è supportato dai browser web](/cells/it/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
