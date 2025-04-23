---
title: Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini
type: docs
weight: 360
url: /it/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Si prega di utilizzare la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) per impostare il carattere predefinito durante la rappresentazione dei fogli di calcolo in immagini. Questa proprietà avrà effetto solo quando il carattere predefinito del foglio di lavoro non potrà rappresentare i tuoi caratteri. Il carattere predefinito specificato con la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) viene utilizzato per tutte quelle celle che hanno caratteri non validi o inesistenti.

{{% /alert %}}

## Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini

Il seguente esempio di codice crea un foglio di lavoro, aggiunge del testo nella cella A4 del primo foglio di lavoro e imposta il carattere su un carattere inesistente o non valido. Quindi, si prendono due immagini del foglio di lavoro. La prima immagine è presa impostando la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) su *Courier New* e la seconda immagine è presa impostando la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) su *Times New Roman*.

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) su *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) su *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
