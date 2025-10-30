---  
title: Json con Node.js a través de C++  
linktitle: Json  
type: docs  
weight: 300  
url: /es/nodejs-cpp/convert-workbook-to-json/  
description: Aprende cómo convertir un libro de Excel a JSON usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells soporta la conversión de un libro a JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Convertir Libro de Excel a JSON**  

La API de Aspose.Cells ofrece soporte para convertir hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a JSON usando el miembro de enumeración [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json). Por favor, vea el código para convertir el [archivo fuente](book1.xlsx) al [archivo JSON de salida](book1.Json) generado por el código como referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Temas avanzados**  
- [Convertir CSV a JSON](/cells/es/nodejs-cpp/convert-csv-to-json/)  
- [Convertir-Excel-a-JSON](/cells/es/nodejs-cpp/convert-excel-to-json/)  
- [Convertir JSON a CSV](/cells/es/nodejs-cpp/convert-json-to-csv/)  
- [Convertir-JSON-a-Excel](/cells/es/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
