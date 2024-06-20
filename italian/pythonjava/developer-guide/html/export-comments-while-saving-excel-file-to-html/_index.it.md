---
title: Esportazione dei commenti durante il salvataggio del file Excel in HTML
type: docs
weight: 60
url: /it/python-java/export-comments-while-saving-excel-file-to/
---

## **Esporta commenti durante il salvataggio del file di Excel in HTML**
Quando Excel viene convertito in HTML, i commenti non vengono esportati. Aspose.Cells for Python via Java fornisce la funzionalità di esportare i commenti durante la conversione da Excel a HTML. Per ottenere questo, l'API fornisce la proprietà [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments). Impostando il valore della proprietà [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) su **True** verranno esportati i commenti nell'HTML di output.

La seguente schermata mostra il file HTML generato dal frammento di codice di esempio.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

Il seguente codice di esempio dimostra l'esportazione dei commenti durante la conversione da Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
