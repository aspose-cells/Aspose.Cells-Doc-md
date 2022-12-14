---
title: Imposta il carattere predefinito durante il rendering del foglio di calcolo in HTML
type: docs
weight: 370
url: /it/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells consente di impostare il carattere predefinito durante il rendering del foglio di calcolo in HTML. Si prega di utilizzare il[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) per questo scopo. Questa proprietà è utile quando in un foglio di calcolo sono presenti alcune celle con caratteri non validi o inesistenti. Quindi quelle celle verranno visualizzate in un carattere specificato con il[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) proprietà.

{{% /alert %}}

## Imposta il carattere predefinito durante il rendering del foglio di calcolo in HTML

Il seguente codice di esempio crea una cartella di lavoro e aggiunge del testo nella cella B4 del primo foglio di lavoro e ne imposta il carattere su un carattere sconosciuto/inesistente. Quindi salva la cartella di lavoro in HTML impostando diversi nomi di caratteri predefiniti come Courier New, Arial, Times New Roman, ecc.

 Lo screenshot mostra l'effetto dell'impostazione di diversi nomi di font predefiniti tramite[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)proprietà.

![cose da fare:immagine_alt_testo](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Il codice genera il file[output file HTML con Courier New](5115516) , il[output HTML con Arial](5115518) , e il[output file HTML con Times New Roman](5115517).

## Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
