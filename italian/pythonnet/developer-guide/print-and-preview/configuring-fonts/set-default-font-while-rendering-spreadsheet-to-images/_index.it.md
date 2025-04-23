---
title: Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini
type: docs
weight: 360
url: /it/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Si prega di utilizzare la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) per impostare il carattere predefinito durante la rappresentazione dei fogli di calcolo in immagini. Questa proprietà avrà effetto solo quando il carattere predefinito del foglio di lavoro non potrà rappresentare i tuoi caratteri. Il carattere predefinito specificato con la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) viene utilizzato per tutte quelle celle che hanno caratteri non validi o inesistenti.

{{% /alert %}}

## Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini

Il seguente esempio di codice crea un foglio di lavoro, aggiunge del testo nella cella A4 del primo foglio di lavoro e imposta il carattere su un carattere inesistente o non valido. Quindi, si prendono due immagini del foglio di lavoro. La prima immagine è presa impostando la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su *Courier New* e la seconda immagine è presa impostando la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su *Times New Roman*.

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su *Courier New*.

![todo:image_alt_text](1.png)

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su *Times New Roman*.

![todo:image_alt_text](2.png)

## Codice di esempio

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

