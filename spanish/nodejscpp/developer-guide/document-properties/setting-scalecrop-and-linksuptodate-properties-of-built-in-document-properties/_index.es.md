---
title: Configuración de propiedades ScaleCrop y LinksUpToDate de las propiedades incorporadas del Documento con Node.js a través de C++
linktitle: Establecimiento de las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas
type: docs
weight: 320
url: /es/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aprende cómo establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades incorporadas del documento usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) y [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) son dos propiedades extendidas de las propiedades incorporadas del documento definidas dentro del formato OpenXml. El propósito de estas propiedades es el siguiente.

## **1) ScaleCrop**
Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en **TRUE** para habilitar el escalado de la miniatura del documento para la visualización. Establezca este elemento en **FALSE** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajusten a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.

## **2) LinksUpToDate**
Este elemento indica si los hipervínculos en un documento están actualizados. Establezca este elemento en **TRUE** para indicar que los hipervínculos están actualizados. Establezca este elemento en **FALSE** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.

## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas**
El siguiente código de ejemplo establece las propiedades extendidas de las propiedades incorporadas del documento [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) y [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) del libro. Por favor, revisa el [archivo Excel de salida](5115500.xlsx) generado con este código, cambia su extensión a .zip y extrae su contenido para ver el app.xml como se muestra en la captura de pantalla anterior.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
