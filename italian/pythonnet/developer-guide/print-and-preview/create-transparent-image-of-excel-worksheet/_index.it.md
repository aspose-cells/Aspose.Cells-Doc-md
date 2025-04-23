---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /it/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A volte, è necessario generare l'immagine del foglio di lavoro come immagine trasparente. Si desidera applicare trasparenza a tutte le celle senza colori di riempimento. Aspose.Cells per Python via .NET fornisce la proprietà [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) per applicare trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è **false**, le celle senza colori di riempimento vengono disegnate con colore bianco e, quando è **true**, le celle senza colori di riempimento vengono disegnate come trasparenti.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

