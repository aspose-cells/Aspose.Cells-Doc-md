---
title: Diferentes formas de abrir archivos con Node.js a través de C++
linktitle: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/nodejs-cpp/different-ways-to-open-files/
description: Este artículo explica cómo abrir un archivo de Excel usando la API de Aspose.Cells for Node.js via C++.
keywords: Abrir un archivo de Excel con Node.js sin Excel, ¿Cómo puedo abrir un archivo de Excel usando Node.js?
---

{{% alert color="primary" %}}

 Con Aspose.Cells, es sencillo abrir archivos, por ejemplo, para recuperar datos, o usar una plantilla de diseño para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Cómo abrir un archivo de Excel a través de una ruta**

 Los desarrolladores pueden abrir un archivo de Microsoft Excel usando su ruta de archivo en la computadora local especificándolo en el constructor de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Solo pasa la ruta en el constructor como un *string*. Aspose.Cells detectará automáticamente el tipo de formato del archivo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Cómo abrir un archivo de Excel via un Stream**

 También es sencillo abrir un archivo de Excel como un stream. Para ello, usa una versión sobrecargada del constructor que acepta el objeto *Stream* que contiene el archivo.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Cómo abrir un archivo con solo datos**

Para abrir un archivo solo con datos, usa las clases [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) para establecer los atributos y opciones relacionadas de las clases para cargar el archivo de plantilla.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Cómo cargar solo las hojas visibles**

Al cargar un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), a veces solo necesitas los datos en las hojas visibles de un libro. Aspose.Cells te permite saltar datos en hojas invisibles al cargar un libro. Para ello, crea una función personalizada que herede de la clase [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) y pasa su instancia a la propiedad [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Aquí está la implementación de la clase *CustomLoad* referenciada en el fragmento anterior.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Se lanzará una excepción si intentas abrir archivos de Excel no nativos u otros formatos de archivo (por ejemplo PPT/PPTX, DOC/DOCX, etc.) usando Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Es probable que el constructor [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) arroje *OutOfMemoryError* al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria; por lo tanto, la hoja de cálculo debe cargarse habilitando las Preferencias de Memoria.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
