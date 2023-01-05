---
title: Crea un'immagine trasparente del foglio di lavoro di Excel
type: docs
weight: 80
url: /it/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 A volte, devi generare l'immagine del tuo foglio di lavoro come immagine trasparente. Vuoi applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce il[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) proprietà per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è**falso** , quindi le celle senza colori di riempimento vengono disegnate con il colore bianco e quando lo è**VERO**, le celle senza colori di riempimento vengono disegnate in modo trasparente.

{{% /alert %}}

Nella seguente immagine del foglio di lavoro, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate in bianco.

**Immagine del foglio di lavoro senza applicare la trasparenza**

![cose da fare:immagine_alt_testo](create-transparent-image-of-excel-worksheet_1.png)

Mentre, nella seguente immagine del foglio di lavoro, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.

**Immagine del foglio di lavoro dopo l'applicazione della trasparenza**

![cose da fare:immagine_alt_testo](create-transparent-image-of-excel-worksheet_2.png)

È possibile utilizzare il seguente codice di esempio per generare un'immagine trasparente del foglio di lavoro di Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
