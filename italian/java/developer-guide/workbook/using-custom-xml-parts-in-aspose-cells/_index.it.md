---
title: Utilizzo di parti XML personalizzate in Aspose.Cells
type: docs
weight: 570
url: /it/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Le parti XML personalizzate sono i dati XML memorizzati da diverse applicazioni come SharePoint, etc. all'interno del file Excel. Questi dati sono utilizzati da diverse applicazioni che ne hanno bisogno. Microsoft Excel non fa uso di questi dati, quindi non ha un'interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l'estensione da **.xlsx** a **.zip** e poi aprendolo con **WinRAR**. I dati sono presenti all'interno della cartella **customXml** come mostrato in questa immagine.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

È possibile aggiungere parti XML personalizzate usando Aspose.Cells tramite il metodo [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-)

{{% /alert %}} 
## **Utilizzo di parti XML personalizzate in Aspose.Cells**
Il seguente esempio di codice utilizza il metodo [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) e aggiunge il **Book Catalog Xml** con il nome **BookStore**. L’immagine seguente mostra il risultato di questo codice. Come si può vedere, il Book Catalog Xml viene aggiunto all’interno del nodo BookStore, che è il nome di questa proprietà.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Articolo correlato**
{{% alert color="primary" %}} 

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
