---
title: Abrir archivos con diferentes formatos con Node.js a través de C++
linktitle: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/nodejs-cpp/opening-files-with-different-formats/
description: La API Aspose.Cells for Node.js via C++ le permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: abrir archivos xlsx, abrir archivos html, leer archivos fods, leer archivos ods, leer archivos sxc, abrir archivos csv, Delimitado por tabulaciones, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Con Aspose.Cells, puede abrir archivos con diferentes formatos. **Aspose.Cells** puede abrir una variedad de formatos de archivo como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos delimitados por tabulaciones (TSV), etc.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivos admitidos](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hoja de cálculo con diferentes formatos como SpreadsheetML, valores separados por comas (CSV), valores delimitados por tabuladores (TSV), archivos ODS. Para abrir tales archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información sobre ellas, como formato, fórmulas, etc. Desde Microsoft Excel XP, se añadió una opción de exportación XML a Microsoft Excel que exporta tus hojas de cálculo a archivos SpreadsheetML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **Abriendo Archivos HTML**

Aspose.Cells te permite abrir un archivo HTML en un objeto Workbook. El archivo HTML debe estar orientado a Microsoft Excel, es decir, MS-Excel debería poder abrirlo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en forma de tabla donde cada columna está separada por el carácter coma y entrecomillada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API Aspose.Cells, como se demuestra en el ejemplo de código a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```

### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```

### **Apertura de archivos con formato de pestañas**

Los archivos delimitados por tabulaciones (Texto) contienen datos de hojas de cálculo pero sin formato. Los datos se organizan en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulación es un tipo especial de archivo de texto simple con una tabulación entre cada columna.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

Un archivo de valores delimitados por tabulaciones (TSV) contiene datos de hojas de cálculo pero sin ningún formato. Es lo mismo que un archivo delimitado por tabulaciones, donde los datos se disponen en filas y columnas como en tablas y hojas de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y soporta fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se usa para archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC, como se demuestra en el siguiente ejemplo de código.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en XML OpenDocument sin compresión. Aspose.Cells puede leer archivos FODS, como se demuestra en el siguiente ejemplo de código.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

