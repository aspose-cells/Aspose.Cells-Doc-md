---  
title: Convertir Excel a JSON con Node.js a través de C++  
linktitle: Convertir Excel a JSON  
type: docs  
weight: 300  
url: /es/nodejs-cpp/convert-excel-to-json/  
description: Aprende cómo convertir un archivo de Excel a JSON usando Aspose.Cells for Node.js via C++.  
keywords: Exportación de libro a JSON en Node.js a través de C++, Convertir Excel a JSON en Node.js a través de C++  
---  

{{% alert color="primary" %}}  
Aspose.Cells soporta convertir un libro a un archivo JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Convertir Libro de Excel a JSON**  

 No necesitas preguntarte cómo convertir un libro de Excel a JSON, porque la biblioteca Aspose.Cells for Node.js via C++ ofrece la mejor solución. La API Aspose.Cells admite convertir hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) como el segundo parámetro del método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.  

 El siguiente ejemplo de código demuestra cómo exportar un libro de Excel a JSON. Consulta el código para convertir el [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

 El siguiente ejemplo de código usa la clase JsonSaveOptions para especificar configuraciones adicionales y demuestra cómo exportar un libro de Excel a JSON. Consulta el código para convertir el [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
