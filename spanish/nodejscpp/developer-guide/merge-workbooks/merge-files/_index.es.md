---
title: Fusionar archivos con Node.js a través de C++
linktitle: Combinar archivos
type: docs
weight: 20
url: /es/nodejs-cpp/merge-files/
---

## **Introducción**

Aspose.Cells ofrece diferentes maneras de fusionar archivos. Para archivos simples con datos, formato y fórmulas, se puede usar el método [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) para combinar varios libros de trabajo, y el método [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) para copiar hojas de trabajo en un nuevo libro. Estos métodos son fáciles de usar y efectivos, pero si tienes muchos archivos para fusionar, puede que tomen muchos recursos del sistema. Para evitar esto, usa el método estático [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-), una forma más eficiente de fusionar varios archivos.

## **Fusionar archivos usando Aspose.Cells for Node.js via C++**

El siguiente código de ejemplo ilustra cómo fusionar archivos grandes usando el método [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-). Toma dos archivos simples pero grandes, Book1.xls y Book2.xls. Los archivos contienen datos formateados y fórmulas solamente.

{{% alert color="primary" %}}

El método [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) solo admite la combinación de datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos pueden no ser combinados usando este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
