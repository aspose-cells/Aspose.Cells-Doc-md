---
title: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 450
url: /it/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.

## **Utilizzando Aspose.Cells for .NET**

Aspose.Cells for .NET supporta l'aggiunta di un'immagine collegata utilizzando il [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

Nell'esempio seguente viene mostrato come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
