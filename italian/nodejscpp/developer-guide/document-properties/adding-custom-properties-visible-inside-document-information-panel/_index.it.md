---
title: Aggiungi proprietà personalizzate visibili nella finestra di documentazione tramite Node.js via C++
linktitle: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Impara come aggiungere proprietà personalizzate a un oggetto cartella di lavoro utilizzando Aspose.Cells for Node.js via C++. Queste proprietà possono essere visualizzate nel Pannello Informazioni Documento.
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells for Node.js via C++ può essere usato per aggiungere proprietà personalizzate all'interno dell'oggetto cartella di lavoro, visibili nel Pannello Informazioni Documento. Puoi aprire il Pannello Informazioni Documento in Microsoft Excel usando File > Info > Proprietà > Mostra pannello documento.

Usa il metodo [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) per aggiungere una proprietà personalizzata che sarà visibile nel Pannello Informazioni Documento.

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà non ha alcun tipo e la seconda ha un tipo come DateTime. Una volta aperto il file Excel generato da questo codice, vedrai queste due proprietà all'interno del Pannello Informazioni Documento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
