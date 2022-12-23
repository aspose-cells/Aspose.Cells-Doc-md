---
title: Crea un'immagine trasparente del foglio di lavoro di Excel
type: docs
weight: 170
url: /it/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 A volte, devi generare l'immagine del tuo foglio di lavoro come immagine trasparente. Vuoi applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce il[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)proprietà per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è**falso** , quindi le celle senza colori di riempimento vengono disegnate con il colore bianco e quando lo è**VERO**, le celle senza colori di riempimento vengono disegnate in modo trasparente.

{{% /alert %}} 

Nella seguente immagine del foglio di lavoro, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate in bianco.

|**Output senza trasparenza: lo sfondo della cella è bianco**|
|:- |
|![cose da fare:immagine_alt_testo](create-transparent-image-of-excel-worksheet_1.png)|

Mentre, nella seguente immagine del foglio di lavoro, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.

|**Output con trasparenza abilitata**|
|:- |
|![cose da fare:immagine_alt_testo](create-transparent-image-of-excel-worksheet_2.png)|

Il codice di esempio seguente genera un'immagine trasparente da un foglio di lavoro di Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
