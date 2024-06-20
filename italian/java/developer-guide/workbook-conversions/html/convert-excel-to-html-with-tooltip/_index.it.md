---
title: Convertire Excel in HTML con tooltip
type: docs
weight: 150
url: /it/java/convert-excel-to-html-with-tooltip/
---

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene tagliato nell'HTML generato e si desidera visualizzare il testo completo come tooltip nell'evento di hover. Aspose.Cells supporta ciò fornendo la proprietà [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText). Impostando la proprietà [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText) su **true** verrà aggiunto il testo completo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il seguente esempio di codice carica il [file Excel di origine](AddTooltipToHtmlSample.xlsx) e genera l'[output del file HTML](AddTooltipToHtmlSample_out.zip) con il tooltip.

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
