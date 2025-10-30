---
title: Converti Excel in HTML con tooltip usando C++
linktitle: Convertire Excel in HTML con tooltip
type: docs
weight: 200
url: /it/go-cpp/convert-excel-to-html-with-tooltip/
description: Converti Excel in HTML aggiungendo tooltip con Aspose.Cells usando C++.
---

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene tagliato nell'HTML generato e vuoi visualizzare il testo completo come tooltip al passaggio del mouse. Aspose.Cells supporta questo fornendo la proprietà [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/). Impostare la proprietà [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) su **true** aggiungerà il testo completo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il seguente esempio di codice carica il [file Excel sorgente](98107416.xlsx) e genera il [file HTML di output](98107417.zip) con il tooltip.

Codice di Esempio

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
