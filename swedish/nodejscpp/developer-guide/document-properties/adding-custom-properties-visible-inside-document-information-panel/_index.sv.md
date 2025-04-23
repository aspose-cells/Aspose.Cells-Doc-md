---
title: Lägga till anpassade egenskaper som är synliga i dokumentinformationen med Node.js via C++
linktitle: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 300
url: /sv/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lär dig hur man lägger till anpassade egenskaper till ett arbetsboksobjekt med Aspose.Cells for Node.js via C++. Dessa egenskaper kan visas i Dokumentinformationspanelen.
---

## **Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen**

Aspose.Cells for Node.js via C++ kan användas för att lägga till anpassade egenskaper inuti arbetsboksobjektet som är synliga i Dokumentinformationspanelen. Du kan öppna Dokumentinformationspanelen i Microsoft Excel med File > Info > Properties > Show Document Panel menykommandon.

Använd [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-)-metoden för att lägga till en anpassad egenskap som syns i Dokumentinformation-panelen.

Följande exempel kod lägger till två anpassade egenskaper. Den första egenskapen saknar typ och den andra är av typen DateTime. När du öppnar den genererade Excel-filen kommer du att se dessa två egenskaper i Dokumentinformation-panelen.

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

### **Relaterad artikel**

{{% alert color="primary" %}}

- [Använd anpassade XML-delsar i Aspose.Cells](/cells/sv/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
