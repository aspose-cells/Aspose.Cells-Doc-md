---
title: Inserisci un'immagine collegata dall'indirizzo web
type: docs
weight: 450
url: /it/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

volte è necessario inserire un'immagine dal Web (http://) in un foglio di lavoro. Per fare ciò, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è fisicamente incorporata nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1.  Clicca il**Inserire** menu e selezionare**Immagine**.
1. Specificare l'indirizzo Web per l'immagine nella finestra di dialogo Inserisci immagine.

## **Utilizzando Aspose.Cells for .NET**

 Aspose.Cells for .NET supporta l'aggiunta di un'immagine collegata utilizzando il[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . Il metodo restituisce a[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)oggetto.

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo Web a un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
