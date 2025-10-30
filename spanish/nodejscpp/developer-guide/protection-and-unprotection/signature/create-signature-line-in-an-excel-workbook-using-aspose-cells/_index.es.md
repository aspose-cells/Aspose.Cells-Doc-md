---  
title: Crear línea de firma en un libro de Excel usando Aspose.Cells for Node.js via C++  
linktitle: Crear Línea de Firma en un Libro de Excel usando Aspose.Cells  
type: docs  
weight: 150  
url: /es/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Este artículo describe cómo crear una línea de firma en un libro de Excel usando código Node.js con Aspose.Cells for Node.js via C++.  
keywords: Crear línea de firma en un libro de Excel con Node.js a través de C++, Cómo crear una línea de firma en un libro de Excel, Cómo agregar línea de firma, Cómo agregar línea de firma a un archivo de Excel.  
---  

## **Introducción**  

Microsoft Excel proporciona una función para agregar **Línea de Firma** en libros de Excel. Puedes agregar una Línea de Firma haciendo clic en la pestaña **Insertar** y luego seleccionando **Línea de Firma** del grupo **Texto**.  

## **Cómo crear una línea de firma para Excel**  

Aspose.Cells for Node.js via C++ también ofrece esta función y ha expuesto la propiedad [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) para este propósito. Este artículo explicará cómo usar esta propiedad para agregar una línea de firma usando Aspose.Cells.  

El código de ejemplo siguiente agrega una línea de firma usando la propiedad [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) y guarda el libro de trabajo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
