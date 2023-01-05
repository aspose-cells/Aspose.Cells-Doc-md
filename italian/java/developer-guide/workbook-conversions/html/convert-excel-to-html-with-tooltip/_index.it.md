---
title: Converti Excel in HTML con tooltip
type: docs
weight: 150
url: /it/java/convert-excel-to-html-with-tooltip/
---
## **Converti Excel in HTML con tooltip**

Potrebbero verificarsi casi in cui il testo viene tagliato nel HTML generato e si desidera visualizzare il testo completo come suggerimento sull'evento al passaggio del mouse. Aspose.Cells supporta questo fornendo**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**proprietà. Impostazione del**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**proprietà a**VERO**aggiungerà il testo completo come suggerimento nel HTML generato.

L'immagine seguente mostra la descrizione comando nel file HTML generato.

![cose da fare:immagine_alt_testo](convert-excel-to-html-with-tooltip_1.jpg)

L'esempio di codice seguente carica il file[file excel di origine](AddTooltipToHtmlSample.xlsx)e genera il[output HTML file](AddTooltipToHtmlSample_out.zip)con il tooltip.

## Codice d'esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
