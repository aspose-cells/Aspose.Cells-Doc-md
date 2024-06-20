---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /it/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A volte è necessario generare l'immagine del foglio di lavoro come un'immagine trasparente. Si desidera applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce la proprietà [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è **false**, le celle senza colori di riempimento vengono disegnate con il colore bianco e quando è **true**, le celle senza colori di riempimento vengono disegnate in modo trasparente.

{{% /alert %}}

Nell'immagine del foglio di lavoro seguente, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate di bianco.

**Immagine del foglio di lavoro senza applicare la trasparenza**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Mentre, nell'immagine del foglio di lavoro seguente, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.

**Immagine del foglio di lavoro dopo aver applicato la trasparenza**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Puoi utilizzare il seguente codice di esempio per generare un'immagine trasparente del tuo foglio di lavoro di Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
