---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /it/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A volte è necessario generare l'immagine del tuo foglio di lavoro come un'immagine trasparente. Desideri applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce la proprietà [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è **false**, le celle senza colori di riempimento vengono disegnate con il colore bianco e quando è **true**, le celle senza colori di riempimento vengono disegnate in modo trasparente.

{{% /alert %}} 

Nell'immagine del foglio di lavoro seguente, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate di bianco.

|**Output senza trasparenza: lo sfondo della cella è bianco**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Mentre, nell'immagine del foglio di lavoro seguente, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.

|**Output con trasparenza abilitata**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Il seguente codice di esempio genera un'immagine trasparente da un foglio di lavoro di Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
