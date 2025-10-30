---
title: Cargando y gestionando archivos de Excel, OpenOffice, Json, Csv y Html
linktitle: Abrir archivos
type: docs
weight: 20
url: /es/nodejs-cpp/loading-saving-and-managing/
description: Con Aspose.Cells, es sencillo crear, abrir y gestionar archivos de Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Imagen, Mht y XPS usando Node.js a través de C++.
---

{{% alert color="primary" %}}

Con Aspose.Cells, es simple crear, abrir y gestionar archivos de Excel, por ejemplo, para obtener datos, o usar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Creando un libro de trabajo nuevo**
El siguiente ejemplo crea un nuevo libro de trabajo desde cero.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Abrir y guardar un archivo**
Con Aspose.Cells, es fácil abrir, guardar y gestionar archivos de Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Temas avanzados**
- [Diferentes formas de abrir archivos](/cells/es/nodejs-cpp/different-ways-to-open-files/)
- [Filtrar nombres definidos al cargar el libro de trabajo](/cells/es/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrar objetos al cargar el libro de trabajo o de la hoja de cálculo](/cells/es/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrar el tipo de datos al cargar el libro de trabajo desde un archivo de plantilla](/cells/es/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtener advertencias al cargar archivo de Excel](/cells/es/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Cargar archivo de Excel fuente sin gráficos](/cells/es/nodejs-cpp/load-source-excel-file-without-charts/)
- [Cargar hojas de cálculo específicas en un libro de trabajo](/cells/es/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Cargar libro de trabajo con tamaño de papel de impresora especificado](/cells/es/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Abrir archivos de diferentes versiones de Microsoft Excel](/cells/es/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Abriendo Archivos con Diferentes Formatos](/cells/es/nodejs-cpp/opening-files-with-different-formats/)
- [Optimización del uso de memoria al trabajar con archivos grandes que contengan conjuntos de datos extensos](/cells/es/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leer Hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells](/cells/es/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado](/cells/es/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Usar la API LightCells](/cells/es/nodejs-cpp/using-lightcells-api/)
- [Convertir CSV a JSON](/cells/es/nodejs-cpp/convert-csv-to-json/)
- [Convertir Excel a JSON](/cells/es/nodejs-cpp/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/nodejs-cpp/convert-json-to-csv/)
- [Convertir JSON a Excel](/cells/es/nodejs-cpp/convert-json-to-excel/)
- [Convertir Excel a Html](/cells/es/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
