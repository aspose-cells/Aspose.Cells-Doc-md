---
title: Usare Parti XML Personalizzate in Aspose.Cells
type: docs
weight: 390
url: /it/python-net/use-custom-xml-parts-in-aspose-cells/
---

## Utilizzo di parti XML personalizzate in Aspose.Cells per Python via .NET

Le Parti XML Personalizzate sono i dati XML memorizzati da diverse applicazioni come SharePoint, ecc. all'interno del file excel. Questi dati vengono consumati da diverse applicazioni che ne hanno bisogno. Microsoft Excel non fa uso di questi dati quindi non c'è un'interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l'estensione da **.xlsx** a **.zip** e quindi aprendo il file utilizzando **WinZip**. Puoi anche aprire il file ZIP utilizzando qualsiasi utility zip di Windows di terze parti come WinRAR o WinZip, ecc. I dati sono presenti all'interno della cartella **customXml**.

Puoi aggiungere parti XML personalizzate utilizzando Aspose.Cells tramite il metodo [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str).

Il seguente codice di esempio utilizza il metodo [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) e aggiunge il **Catalogo dei Libri XML** e il suo nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, il Catalogo dei Libri XML viene aggiunto all'interno del nodo BookStore che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice C# per utilizzare parti XML personalizzate

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-UsingCustomXmlParts.py" >}}



{{< app/cells/assistant language="python-net" >}}
