---
title: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento con Node.js a través de C++
linktitle: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 300
url: /es/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aprende cómo agregar propiedades personalizadas a un objeto libro utilizando Aspose.Cells for Node.js via C++. Estas propiedades se pueden ver en el Panel de Información del Documento.
---

## **Agregar propiedades personalizadas visibles dentro del Panel de información del documento**

Aspose.Cells for Node.js via C++ puede usarse para agregar propiedades personalizadas dentro del objeto libro que son visibles en el Panel de Información del Documento. Puedes abrir el Panel de Información del Documento en Microsoft Excel usando los comandos de menú Archivo > Información > Propiedades > Mostrar panel de documento.

Utilice el método [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento.

El siguiente ejemplo de código añade dos propiedades personalizadas. La primera propiedad no tiene ningún tipo y la segunda tiene un tipo como DateTime. Cuando abras el archivo de Excel generado por este código, verás estas dos propiedades dentro del Panel de Información del Documento.

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

### **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes de XML Personalizadas en Aspose.Cells](/cells/es/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
