---
title: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 450
url: /it/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.

## **Usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET supporta l'aggiunta di un'immagine collegata utilizzando [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). Il metodo ritorna un oggetto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

Nell'esempio seguente viene mostrato come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
