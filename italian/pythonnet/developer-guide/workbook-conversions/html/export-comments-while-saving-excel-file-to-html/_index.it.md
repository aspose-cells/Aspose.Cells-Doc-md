---
title: Esportazione dei commenti durante il salvataggio del file Excel in HTML
type: docs
weight: 40
url: /it/python-net/export-comments-while-saving-excel-file-to/
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, i commenti non vengono esportati. Tuttavia, Aspose.Cells per Python via .NET fornisce questa funzionalità usando la proprietà [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). Se la imposti su **true**, allora anche i commenti presenti nel tuo file Excel verranno visualizzati in HTML.

## **Esporta commenti durante il salvataggio del file di Excel in HTML**

Il codice di esempio seguente spiega l'uso della proprietà [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). La schermata mostra l'effetto del codice sull'HTML quando è impostato su **true**. Puoi scaricare il [file di esempio di Excel](50528260.xlsx) e l'HTML [generato](5052826.txt) come riferimento.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
