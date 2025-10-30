---
title: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells for Python via .NET può essere utilizzato per aggiungere proprietà personalizzate all'interno dell'oggetto workbook visibili nel Pannello delle Informazioni sul Documento. È possibile aprire il Pannello delle Informazioni sul Documento in Microsoft Excel tramite File > Info > Proprietà > Mostra pannello del documento.

Si prega di utilizzare il metodo [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) per aggiungere una proprietà personalizzata che sarà visibile nel pannello delle informazioni sul documento

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà è senza alcun tipo e la seconda proprietà ha un tipo come DataOra. Una volta aperto il file Excel di output generato da questo codice, vedrai queste due proprietà all'interno del pannello delle informazioni sul documento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
