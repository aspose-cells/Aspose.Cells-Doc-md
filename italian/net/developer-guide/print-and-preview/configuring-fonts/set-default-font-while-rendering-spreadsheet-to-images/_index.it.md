---
title: Imposta il carattere predefinito durante il rendering del foglio di calcolo sulle immagini
type: docs
weight: 360
url: /it/net/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}}

 Si prega di utilizzare il[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) proprietà per impostare il carattere predefinito durante il rendering dei fogli di calcolo nelle immagini. Questa proprietà sarà efficace solo quando il carattere predefinito della cartella di lavoro non è in grado di eseguire il rendering dei caratteri. Il carattere predefinito specificato con[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)property viene utilizzata per tutte quelle celle che hanno font non validi o inesistenti.

{{% /alert %}}

## Imposta il carattere predefinito durante il rendering del foglio di calcolo sulle immagini

Il seguente codice di esempio crea una cartella di lavoro, aggiunge del testo nella cella A4 del primo foglio di lavoro e ne imposta il carattere su un carattere non valido o inesistente. Quindi, prende due immagini del foglio di lavoro. La prima immagine viene scattata impostando il[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) proprietà a*Courier New* e la seconda immagine viene scattata impostando il[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) proprietà a*Times New Roman*.

 Questa è l'immagine di output dopo aver impostato il file[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) proprietà a*Courier New*.

![cose da fare:immagine_alt_testo](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Questa è l'immagine di output dopo aver impostato il file[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) proprietà a*Times New Roman*.

![cose da fare:immagine_alt_testo](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
