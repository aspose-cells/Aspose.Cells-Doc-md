---
title: Imposta il carattere predefinito durante la rendering del foglio di calcolo in HTML con Golang tramite C++
linktitle: Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML
type: docs
weight: 370
url: /it/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Impara come impostare il font predefinito durante la conversione di un foglio di calcolo in HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells permette di impostare il font predefinito durante la conversione di un foglio di calcolo in HTML. Usa [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) a tale scopo. Questa proprietà è utile quando alcune celle di un foglio di calcolo hanno font non validi o inesistenti. Quindi, quelle celle verranno renderizzate con il font specificato dalla proprietà [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML

Il seguente codice di esempio crea un workbook e aggiunge del testo nella cella B4 del primo foglio di lavoro e imposta il suo carattere su un font sconosciuto/inesistente. Quindi salva il workbook in HTML impostando diversi nomi di carattere predefinito come Courier New, Arial, Times New Roman, ecc.

Lo screenshot mostra l'effetto di impostare nomi di font predefiniti diversi tramite la proprietà [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Il codice genera [file HTML di output con Courier New](5115516), il [file HTML con Arial](5115518) e il [file HTML di output con Times New Roman](5115517).

## Codice di esempio

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
