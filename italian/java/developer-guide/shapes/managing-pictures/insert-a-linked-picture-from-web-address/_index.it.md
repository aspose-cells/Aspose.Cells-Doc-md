---
title: Inserisci un'immagine collegata dall'indirizzo web
type: docs
weight: 50
url: /it/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal Web (http://) in un foglio di lavoro. Per fare ciò, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è fisicamente incorporata nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Inserimento di un'immagine collegata da un indirizzo Web**

### **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1.  Clicca il**Inserire** menu e selezionare**Immagine**.

![cose da fare:immagine_alt_testo](insert-a-linked-picture-from-web-address_1.png)

1.  Specificare l'indirizzo Web per l'immagine nella finestra di dialogo Inserisci immagine.

![cose da fare:immagine_alt_testo](insert-a-linked-picture-from-web-address_2.png)

L'immagine viene inserita.

![cose da fare:immagine_alt_testo](insert-a-linked-picture-from-web-address_3.png)

### **Utilizzando Aspose.Cells for Java**

 Aspose.Cells for Java supporta l'aggiunta di un'immagine collegata utilizzando il metodo[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int altezza, int larghezza, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 Il metodo restituisce a[**Immagine**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)oggetto.

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo Web a un foglio di lavoro.

Dopo aver eseguito il codice, il file Excel generato contiene un'immagine collegata nel primo foglio di lavoro.

**Il file di output** 

![cose da fare:immagine_alt_testo](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
