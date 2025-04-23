---  
title: Convertir CSV, TSV y TXT a Excel con Node.js vía C++  
linktitle: Convertir CSV, TSV y TXT a Excel  
type: docs  
weight: 30  
url: /es/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Usando Aspose.Cells, puedes convertir archivos CSV a Excel, OpenOffice, PDF, JSON y muchos otros formatos.  
{{% /alert %}}  

## **Abriendo Archivos CSV**  

Los archivos de Valores Separados por Comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en una tabla donde cada columna está separada por el carácter de coma y entre comillas por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hoja de cálculo a CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Abriendo Archivos CSV y reemplazando caracteres inválidos**  

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API Aspose.Cells, como se demuestra en el ejemplo de código a continuación.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

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
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**  

Los archivos de valores separados por tabulaciones (TSV) contienen datos de hojas de cálculo pero sin formato. Es lo mismo que un archivo delimitado por tabulación donde los datos se organizan en filas y columnas como en tablas y hojas de cálculo.  

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

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Temas avanzados**  
- [Cargar o importar archivo CSV con fórmulas](/cells/es/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Lectura de archivo CSV con múltiples codificaciones](/cells/es/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


