---  
title: Especificar autor al proteger con escritura un libro de trabajo con Node.js mediante C++  
linktitle: Especificar Autor al proteger un libro de trabajo  
type: docs  
weight: 40  
url: /es/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Especifique un nombre de autor al proteger con escritura un libro de trabajo usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**

Puede especificar un nombre de autor al proteger con escritura su libro de trabajo usando API Aspose.Cells. Por favor, use la propiedad [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) para este propósito.

## **Especificar Autor al Proteger la Escritura del Libro de Trabajo**

El código de ejemplo siguiente explica el uso de la propiedad [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). El código crea un libro de trabajo vacío, lo protege con una contraseña, especifica el nombre del autor y lo guarda como [archivo Excel de salida](67338582.xlsx). La siguiente captura de pantalla ilustra el efecto del código de ejemplo en el archivo Excel de salida para su referencia.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

