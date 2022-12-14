---
title: Converti Excel in HTML con tooltip
type: docs
weight: 200
url: /it/net/convert-excel-to-html-with-tooltip/
---
## **Converti Excel in HTML con tooltip**

Potrebbero verificarsi casi in cui il testo viene tagliato nell'HTML generato e si desidera visualizzare il testo completo come descrizione comando sull'evento al passaggio del mouse. Aspose.Cells supporta questo fornendo**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** proprietà. Impostazione del**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** proprietà a**VERO** aggiungerà il testo completo come suggerimento nell'HTML generato.

L'immagine seguente mostra la descrizione comando nel file HTML generato.

![cose da fare:immagine_alt_testo](convert-excel-to-html-with-tooltip_1.jpg)

 L'esempio di codice seguente carica il file[file excel di origine](98107416.xlsx) e genera il[file HTML di output](98107417.zip) con il tooltip.

Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
