---
title: Convertir CSV a JSON con Node.js a través de C++
linktitle: Convertir CSV a JSON
type: docs
weight: 220
url: /es/nodejs-cpp/convert-csv-to-json/
description: Convertir archivo CSV a JSON usando la API fácil de usar Aspose.Cells for Node.js via C++.
keywords: Convertir, Convertir CSV a JSON, CSV a JSON, CSV, JSON, Convertir CSV a JSON en Node.js a través de C++, código en C++ para convertir CSV a JSON
---

## **Convertir CSV a JSON**

Aspose.Cells admite la conversión de CSV a JSON. Para esto, la API proporciona las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) y [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/). La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) ofrece las opciones para exportar rango a JSON. La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) tiene las siguientes propiedades.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Esto exporta el valor de cadena de las celdas a JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Esto indica si el rango contiene una fila de encabezado.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Indica la sangría.

La clase [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) exporta el JSON utilizando las opciones de exportación configuradas con la clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/).

El siguiente ejemplo de código demuestra el uso de las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) y [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) para cargar el [archivo CSV fuente](104398879.csv) e imprimir la salida JSON en la consola.

### **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Load CSV file
const filePath = path.join(sourceDir, "SampleCsv.csv");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
const lastCell = workbook.getWorksheets().get(0).getCells().getLastCell();

// Set JsonSaveOptions
const jsonSaveOptions = new AsposeCells.JsonSaveOptions();
const range = workbook.getWorksheets().get(0).getCells().createRange(0, 0, lastCell.getRow() + 1, lastCell.getColumn() + 1);
const data = AsposeCells.JsonUtility.exportRangeToJson(range, jsonSaveOptions);

// Print JSON
console.log(data);
```

### **Salida de la consola**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
