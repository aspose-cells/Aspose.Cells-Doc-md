---
title: Usa parti XML personalizzate in Aspose.Cells con Golang tramite C++
linktitle: Utilizza parti XML personalizzate
type: docs
weight: 390
url: /it/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Impara come usare le parti XML personalizzate nei file Excel tramite programmazione usando Aspose.Cells con Golang tramite C++.
---

## Utilizzo di Parti XML Personalizzate in Aspose.Cells

Le parti XML personalizzate sono dati XML memorizzati da diverse applicazioni come SharePoint all'interno di un file Excel. Questi dati sono utilizzati da varie applicazioni che ne necessitano. Microsoft Excel non utilizza questi dati, quindi non esiste un'interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l'estensione di **.xlsx** in **.zip** e aprendolo con **WinZip**. Puoi anche aprire il file ZIP con qualsiasi utility di compressione Windows di terze parti come WinRAR o WinZip. I dati sono presenti all'interno della cartella **customXml**.

Puoi aggiungere parti XML personalizzate usando Aspose.Cells tramite il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/).

Il seguente esempio di codice utilizza il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) per aggiungere l'**XML del catalogo libri**, il cui nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, l'XML del catalogo libri è stato aggiunto all'interno del nodo BookStore, che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice C++ per usare parti XML personalizzate

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Articolo Correlato

- [Aggiunta di proprietà personalizzate visibili nel pannello delle informazioni del documento](/cells/it/cpp/adding-custom-properties-visible-inside-document-information-panel/)
