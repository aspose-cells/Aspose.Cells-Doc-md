---
title: Usare Parti XML Personalizzate in Aspose.Cells
type: docs
weight: 390
url: /it/net/use-custom-xml-parts-in-aspose-cells/
---

## Utilizzo di Parti XML Personalizzate in Aspose.Cells

Le Parti XML Personalizzate sono i dati XML memorizzati da diverse applicazioni come SharePoint, ecc. all'interno del file excel. Questi dati vengono consumati da diverse applicazioni che ne hanno bisogno. Microsoft Excel non fa uso di questi dati quindi non c'è un'interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l'estensione da **.xlsx** a **.zip** e quindi aprendo il file utilizzando **WinZip**. Puoi anche aprire il file ZIP utilizzando qualsiasi utility zip di Windows di terze parti come WinRAR o WinZip, ecc. I dati sono presenti all'interno della cartella **customXml**.

Puoi aggiungere parti XML personalizzate utilizzando Aspose.Cells tramite il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index).

Il seguente codice di esempio utilizza il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) e aggiunge il **Catalogo dei Libri XML** e il suo nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, il Catalogo dei Libri XML viene aggiunto all'interno del nodo BookStore che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice C# per utilizzare parti XML personalizzate

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Articolo Correlato

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/net/adding-custom-properties-visible-inside-document-information-panel/)
