---
title: Usa parti XML personalizzate in Aspose.Cells
type: docs
weight: 390
url: /it/net/use-custom-xml-parts-in-aspose-cells/
---
## Utilizzo di parti XML personalizzate in Aspose.Cells

Le parti XML personalizzate sono i dati XML archiviati da diverse applicazioni come SharePoint ecc. All'interno del file excel. Questi dati vengono consumati da diverse applicazioni che ne hanno bisogno. Microsoft Excel non fa uso di questi dati quindi non c'è nessuna GUI per aggiungerli. È possibile visualizzare questi dati modificando l'estensione di**.xlsx** in**.cerniera lampo** e poi aprendolo usando**WinZip** . Puoi anche aprire il file ZIP utilizzando qualsiasi utilità zip di terze parti Windows come WinRAR o WinZip ecc. I dati sono presenti all'interno del**customXml** cartella.

 È possibile aggiungere parti XML personalizzate utilizzando Aspose.Cells tramite il file[**Cartella di lavoro.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)metodo.

 Il seguente codice di esempio usa[**Cartella di lavoro.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) metodo e aggiunge il**Catalogo libri XML** e il suo nome è**Libreria**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere Book Catalog XML viene aggiunto all'interno del nodo BookStore che è il nome di questa proprietà.

![cose da fare:immagine_alt_testo](use-custom-xml-parts-in-aspose-cells_1.png)

![cose da fare:immagine_alt_testo](use-custom-xml-parts-in-aspose-cells_2.png)

## C# codice per utilizzare parti XML personalizzate

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Articolo correlato

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello Informazioni documento](/cells/it/net/adding-custom-properties-visible-inside-document-information-panel/)
