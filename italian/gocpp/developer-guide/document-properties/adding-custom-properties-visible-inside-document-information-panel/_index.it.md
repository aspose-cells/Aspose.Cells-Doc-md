---
title: Aggiunta di Proprietà Personalizzate visibili nel Pannello Informazioni Documento con Golang via C++
linktitle: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Impara come aggiungere proprietà personalizzate visibili nel Pannello Informazioni Documento usando Aspose.Cells con Golang via C++.
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells può essere utilizzato per aggiungere proprietà personalizzate all'interno dell'oggetto del foglio di lavoro visibili all'interno del pannello delle informazioni del documento. È possibile aprire il pannello delle informazioni del documento in Microsoft Excel utilizzando i comandi del menu File > Informazioni > Proprietà > Mostra pannello del documento.

Usa il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) per aggiungere una proprietà personalizzata che sarà visibile nel Pannello Informazioni Documento.

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà non ha alcun tipo e la seconda ha un tipo come DateTime. Una volta aperto il file Excel generato da questo codice, vedrai queste due proprietà all'interno del Pannello Informazioni Documento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
