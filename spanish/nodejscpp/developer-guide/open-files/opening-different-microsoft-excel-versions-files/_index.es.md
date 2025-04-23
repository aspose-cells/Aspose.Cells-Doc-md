---
title: Abrir diferentes archivos de Excel de versiones distintas con Node.js vía C++
linktitle: Abrir Archivos de Diferentes Versiones de Microsoft Excel
type: docs
weight: 20
url: /es/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Este artículo explica cómo abrir archivos de diferentes versiones de Excel usando Aspose.Cells for Node.js via C++.
keywords: Abrir diferentes archivos de Excel con Node.js vía C++, ¿Cómo abrir archivos de Excel cifrados con Node.js mediante C++?
---

{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de archivos de diferentes versiones de Microsoft Excel, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel encriptados.

{{% /alert %}}

## **Cómo Abrir Archivos de Diferentes Versiones de Microsoft Excel**

Una aplicación a menudo debe poder abrir archivos de Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que tenga que cargar un archivo en cualquiera de varios formatos, incluyendo XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, entre otros. Use el constructor, o especifique el atributo de tipo [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que indica el formato usando la enumeración [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype).

La enumeración [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|Csv|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|Xltx|Representa una plantilla de Excel 2007/2010/2013/2016/2019 y Office 365 XLTX|
|Xltm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 habilitado para macros XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|SpreadsheetML|Representa un archivo de SpreadsheetML|
|Tsv|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|Ods|Representa un archivo ODS|
|Html|Representa un archivo HTML|
|Mhtml|Representa un archivo MHTML|

### **Abrir archivos de Microsoft Excel 95/5.0**

Para abrir un archivo de Microsoft Excel 95/5.0, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y configure el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) para que se cargue el archivo de plantilla. Un archivo de ejemplo para probar esta función se puede descargar desde el siguiente enlace:

[Archivo de Excel95](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Abrir archivos de Microsoft Excel 97 - 2003**

Para abrir un archivo de Microsoft Excel 97 - 2003, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y configure el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) para que se cargue el archivo de plantilla.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Abrir archivos de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365  XLSX**

Para abrir un formato de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puede usar [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y configurar el atributo/opciones relacionados de la clase [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) para que se cargue el archivo de plantilla.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **Abrir archivos de Excel encriptados**

Es posible crear archivos de Excel encriptados utilizando Microsoft Excel. Para abrir un archivo encriptado, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y establezca sus atributos y opciones (por ejemplo, una contraseña) para que se cargue el archivo de plantilla.
Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells también admite la apertura de archivos protegidos con contraseña de Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365.


