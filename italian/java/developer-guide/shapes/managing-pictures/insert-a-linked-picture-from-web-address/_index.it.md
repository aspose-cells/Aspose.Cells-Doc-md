---
title: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 50
url: /it/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Inserimento di un'immagine collegata dall'indirizzo Web**

### **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

L'immagine è inserita.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Utilizzando Aspose.Cells for Java**

Aspose.Cells for Java supporta l'aggiunta di un'immagine collegata utilizzando il metodo [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-).

Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)

Nell'esempio seguente viene mostrato come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

Dopo l'esecuzione del codice, il file Excel generato contiene un'immagine collegata nel primo foglio di lavoro.

**Il file di output 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
