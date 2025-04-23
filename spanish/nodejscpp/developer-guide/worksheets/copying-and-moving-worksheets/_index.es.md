---
title: Copiar y mover hojas de trabajo en Node.js a través de C++
linktitle: Copiar y mover hojas de cálculo
type: docs
weight: 10
url: /es/nodejs-cpp/copying-and-moving-worksheets/
description: Este artículo incluye código de ejemplo y describe cómo copiar y mover hojas de cálculo automáticamente tanto dentro de un libro de Excel como entre libros de Excel usando la API de Node.js con C++.
keywords: copiar hoja de cálculo Node.js, mover hoja de cálculo Node.js
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells for Node.js via C++ admite copiar y mover hojas de cálculo dentro o entre libros de trabajo. Hojas de cálculo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}}

## **Mover o Copiar Hojas usando Microsoft Excel**

A continuación se detallan los pasos necesarios para copiar y mover hojas de cálculo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro de diálogo **Hacia el libro**, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro de trabajo, haga clic en **Nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

### **Copiar hojas de cálculo dentro de un libro con Aspose.Cells for Node.js via C++**

Aspose.Cells proporciona un método sobrecargado, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), que se utiliza para agregar una hoja de cálculo a la colección y copiar datos de una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo fuente como parámetro. La otra versión toma el nombre de la hoja de cálculo fuente.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Copiar Hojas de Cálculo entre Libros de Trabajo**

Aspose.Cells proporciona un método, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), utilizado para copiar datos y formato de una hoja de cálculo fuente a otra hoja dentro o entre libros de trabajo. El método toma el objeto de hoja de cálculo fuente como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Mover Hojas de Cálculo dentro de un Libro de Trabajo**

Aspose.Cells ofrece un método [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) que se usa para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de destino como parámetro.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
