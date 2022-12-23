---
title: Utilizzo di parti XML personalizzate in Aspose.Cells
type: docs
weight: 570
url: /it/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Le parti XML personalizzate sono i dati XML memorizzati da diverse applicazioni come SharePoint ecc. All'interno del file Excel. Questi dati vengono consumati da diverse applicazioni che ne hanno bisogno. Microsoft Excel non fa uso di questi dati quindi non c'è nessuna GUI per aggiungerli. È possibile visualizzare questi dati modificando l'estensione di**.xlsx** in**.cerniera lampo** e poi aprendolo usando**WinRAR** . I dati sono presenti all'interno del**customXml** cartella come mostrato in questa immagine.

![cose da fare:immagine_alt_testo](using-custom-xml-parts-in-aspose-cells_1.png)

 È possibile aggiungere parti XML personalizzate utilizzando Aspose.Cells tramite il file[Cartella di lavoro.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) metodo.

{{% /alert %}} 
## **Utilizzo di parti Xml personalizzate in Aspose.Cells**
 Il seguente codice di esempio usa[Cartella di lavoro.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) metodo e aggiunge il**Catalogo libri Xml** e il suo nome è**Libreria**L'immagine seguente mostra il risultato di questo codice. Come puoi vedere Book Catalog Xml viene aggiunto all'interno del nodo BookStore che è il nome di questa proprietà.

![cose da fare:immagine_alt_testo](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Articolo correlato**
{{% alert color="primary" %}} 

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello Informazioni documento](/cells/it/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
