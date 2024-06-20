---
title: Prevenire l esportazione del contenuto del foglio di lavoro nascosto durante il salvataggio in HTML
type: docs
weight: 90
url: /it/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

È possibile salvare i fogli di lavoro di Excel in HTML. Tuttavia, se il foglio di lavoro contiene fogli di lavoro nascosti, Aspose.Cells esporta per impostazione predefinita il contenuto del foglio di lavoro nascosto nella directory di output HTML (_files) che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, esportare il contenuto dei fogli di lavoro nascosti in questo modo non è appropriato. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non dovrebbero essere esportate nella directory _files.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet). Per impostazione predefinita, la proprietà [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) è impostata su **true**. Se la si imposta su **false**, allora Aspose.Cells non esporterà i contenuti nascosti del foglio di calcolo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Oltre al controllo se esportare o meno fogli di calcolo nascosti, è possibile anche configurare impostazioni aggiuntive per esportare il workbook in HTML. Gli articoli seguenti mostrano altre funzionalità supportate da Aspose.Cells per l'esportazione di workbook in HTML.

- [Converti Excel in HTML con intestazioni](/cells/it/java/convert-excel-to-html-with-headings/)
- [Escludere Stili Non Utilizzati durante la conversione da Excel a HTML](/cells/it/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Esporta commenti durante il salvataggio del file di Excel in HTML](/cells/it/java/export-comments-while-saving-excel-file-to-html/)
- [Nascondere il Contenuto Sovrapposto con CrossHideRight durante il salvataggio in HTML](/cells/it/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web](/cells/it/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
