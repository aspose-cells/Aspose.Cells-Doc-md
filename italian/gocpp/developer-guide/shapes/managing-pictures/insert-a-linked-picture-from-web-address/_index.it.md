---
title: Inserisci un immagine collegata da indirizzo Web con Golang tramite C++
linktitle: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 450
url: /it/go-cpp/insert-a-linked-picture-from-web-address/
description: Impara come inserire un immagine collegata da un indirizzo web in un foglio di lavoro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.

## **Utilizzando Aspose.Cells for C++**

Aspose.Cells for C++ supporta l'aggiunta di un'immagine collegata usando il metodo [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
