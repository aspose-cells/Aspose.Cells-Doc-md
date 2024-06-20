---
title: Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini
type: docs
weight: 840
url: /it/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Si prega di utilizzare la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) per impostare il font predefinito durante il rendering del foglio di calcolo nelle immagini. Questa proprietà sarà efficace solo quando il font predefinito del workbook non potrebbe renderizzare i tuoi caratteri. Il font predefinito specificato con la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) è utilizzato per tutte quelle celle che hanno un font non valido o inesistente.

{{% /alert %}} 
## **Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini**
Il seguente codice di esempio crea un workbook, aggiunge del testo nella cella A4 del primo foglio di lavoro e imposta il suo font su un font non valido o inesistente. Quindi, ottiene due immagini del foglio di lavoro. La prima immagine è ottenuta impostando la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su *Courier New* e la seconda immagine è ottenuta impostando la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su *Times New Roman*.

Questa è l'immagine di output dopo aver impostato la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Questa è l'immagine di output dopo aver impostato la proprietà [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
