---
title: Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML
type: docs
weight: 370
url: /it/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di impostare il carattere predefinito durante la conversione del foglio di calcolo in HTML. Si prega di utilizzare [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) a questo scopo. Questa proprietà è utile quando alcune celle in un foglio di calcolo hanno caratteri non validi o inesistenti. Quindi quelle celle verranno renderizzate con un carattere specificato con la proprietà [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML

Il seguente codice di esempio crea un workbook e aggiunge del testo nella cella B4 del primo foglio di lavoro e imposta il suo carattere su un font sconosciuto/inesistente. Quindi salva il workbook in HTML impostando diversi nomi di carattere predefinito come Courier New, Arial, Times New Roman, ecc.

La schermata mostra l'effetto del setting di diversi nomi di caratteri predefiniti tramite la proprietà [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Il codice genera [file HTML di output con Courier New](5115516), il [file HTML con Arial](5115518) e il [file HTML di output con Times New Roman](5115517).

## Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
