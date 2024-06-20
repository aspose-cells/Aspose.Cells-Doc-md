---
title: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells può essere utilizzato per aggiungere proprietà personalizzate all'interno dell'oggetto del foglio di lavoro visibili all'interno del pannello delle informazioni del documento. È possibile aprire il pannello delle informazioni del documento in Microsoft Excel utilizzando i comandi del menu File > Informazioni > Proprietà > Mostra pannello del documento.

Si prega di utilizzare il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) per aggiungere una proprietà personalizzata che sarà visibile nel pannello delle informazioni sul documento

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà è senza alcun tipo e la seconda proprietà ha un tipo come DataOra. Una volta aperto il file Excel di output generato da questo codice, vedrai queste due proprietà all'interno del pannello delle informazioni sul documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddingCustomPropertiesVisible-1.cs" >}}

### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
