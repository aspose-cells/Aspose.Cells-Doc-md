---
title: Convertire Excel in HTML con tooltip
type: docs
weight: 200
url: /it/net/convert-excel-to-html-with-tooltip/
---

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene troncato nell'HTML generato e si desidera visualizzare l'intero testo come tooltip nell'evento di hover. Aspose.Cells supporta questo fornendo la proprietà [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext). Impostando la proprietà [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) su **true** verrà aggiunto l'intero testo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il codice di esempio seguente carica il [file excel di origine](98107416.xlsx) e genera il [file HTML di output](98107417.zip) con il tooltip.

Codice di Esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
