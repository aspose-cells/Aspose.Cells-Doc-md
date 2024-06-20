---
title: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 500
url: /it/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells può essere utilizzato per aggiungere proprietà personalizzate all'interno dell'oggetto del foglio di lavoro visibili all'interno del pannello delle informazioni del documento. È possibile aprire il pannello delle informazioni del documento in Microsoft Excel utilizzando i comandi del menu File > Informazioni > Proprietà > Mostra pannello del documento.

Si prega di utilizzare il metodo [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) per aggiungere una proprietà personalizzata che sarà visibile nel riquadro delle informazioni sul documento

{{% /alert %}}

## **Esempio**

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà è senza alcun tipo e la seconda proprietà ha un tipo come DataOra. Una volta aperto il file Excel di output generato da questo codice, vedrai queste due proprietà all'interno del pannello delle informazioni sul documento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizzo di parti XML personalizzate in Aspose.Cells](/cells/it/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
