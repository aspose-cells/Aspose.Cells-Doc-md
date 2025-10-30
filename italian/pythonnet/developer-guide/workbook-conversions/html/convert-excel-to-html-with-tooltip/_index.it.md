---
title: Convertire Excel in HTML con tooltip
type: docs
weight: 200
url: /it/python-net/convert-excel-to-html-with-tooltip/
description: Questo argomento ti mostra come convertire Excel in HTML con tooltip usando Aspose.Cells per Python via NET.
keywords: Python Convertire Excel in HTML con tooltip, Convertire Excel in HTML con tooltip Python via NET, Python via NET Excel in HTML con tooltip, Python Workbook in HTML con tooltip.
---

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene troncato nell'HTML generato e si desidera visualizzare l'intero testo come tooltip nell'evento di hover. Aspose.Cells supporta questo fornendo la proprietà [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/). Impostando la proprietà [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) su **true** verrà aggiunto l'intero testo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il codice di esempio seguente carica il [file excel di origine](98107416.xlsx) e genera il [file HTML di output](98107417.zip) con il tooltip.

Codice di Esempio

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
