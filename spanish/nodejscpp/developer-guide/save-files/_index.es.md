---
title: Diferentes formas de guardar archivos con Node.js a través de C++
linktitle: Guardar archivos
type: docs
weight: 40
url: /es/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ puede guardar archivos en diferentes formatos, incluidos PDF, HTML, DOCX, PPTX, JSON y MHTML.
keywords: Aspose.Cells Guarda Excel como PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML y más usando Node.js a través de C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible crear y guardar archivos. Este artículo explica las varias maneras en las que los archivos pueden ser guardados.

{{% /alert %}}

## **Diferentes formas de guardar archivos**

Aspose.Cells proporciona el [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel y ofrece las propiedades y métodos necesarios para trabajar con archivos de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) proporciona el método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) utilizado para guardar archivos de Excel. El método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes maneras.

El formato de archivo en el que se guarda el archivo se decide por la enumeración [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007 XLSX|
|Xlsm|Representa un archivo de Excel 2007 XLSM|
|Xltx|Representa una plantilla de Excel 2007 XLTX|
|Xltm|Representa un archivo habilitado para macros de Excel 2007 XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007|
|SpreadsheetML|Representa un archivo XML de hoja de cálculo|
|TSV|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|Html|Representa archivo(s) HTML|
|MHtml|Representa archivo(s) MHTML|
|Pdf|Representa un archivo PDF|
|XPS|Representa un documento XPS|
|TIFF|Representa el Formato de Archivo de Imágenes Etiquetado (TIFF)|

## **Cómo Guardar un Archivo en Diferentes Formatos**

Para guardar archivos en una ubicación de almacenamiento, especifica el nombre del archivo (incluido la ruta de almacenamiento) y el formato de archivo deseado (de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)) al llamar al método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) del objeto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Cómo guardar un libro en formato PDF**
El Formato de Documento Portable (PDF) es un tipo de documento creado por Adobe en los años 90. El propósito de este formato de archivo era introducir un estándar para la representación de documentos y otros materiales de referencia en un formato independiente de la aplicación de software, hardware y sistema operativo. El formato PDF tiene la capacidad completa de contener información como texto, imágenes, hipervínculos, campos de formulario, medios enriquecidos, firmas digitales, archivos adjuntos, metadatos, características geoespaciales y objetos 3D que pueden formar parte del documento fuente.

El siguiente código muestra cómo guardar un libro de trabajo como archivo PDF con Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Cómo guardar un libro en formato de texto o CSV**

A veces, deseas convertir o guardar un libro con múltiples hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar una hoja de cálculo completa en formato de texto. Cargue el libro fuente, que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (como XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de cálculo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en formato CSV. Por defecto, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) es coma, así que no especifique un separador si guarda en formato CSV. Tenga en cuenta: si usa la versión de evaluación e incluso si la propiedad [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) está configurada en true, el programa aún exportará solo una hoja de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Cómo guardar archivo en archivos de texto con un separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **Cómo guardar archivo en un flujo de datos**

Para guardar archivos en un flujo de datos, cree un objeto *MemoryStream* o *FileStream* y guarde el archivo en ese objeto de flujo llamando al método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) del objeto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Especifique el formato de archivo deseado usando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) al llamar al método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Cómo guardar archivo de Excel en archivos HTML y MHT**
Aspose.Cells puede simplemente guardar un archivo de Excel, JSON, CSV u otros archivos que puedan ser cargados por Aspose.Cells como archivos .html y .mht.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Cómo guardar archivo de Excel en OpenOffice (ODS, SXC, FODS, OTS)**
Podemos guardar los archivos en formato OpenOffice: ODS, SXC, FODS, OTS, etc.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Cómo guardar archivo de Excel en JSON o XML**

JSON (Notación de Objetos de JavaScript) es un formato de archivo estándar abierto para compartir datos que utiliza texto legible para almacenar y transmitir datos. Los archivos JSON se almacenan con la extensión .json. JSON requiere menos formato y es una buena alternativa para XML. JSON se deriva de JavaScript, pero es un formato de datos independiente del lenguaje. La generación y análisis de JSON son compatibles con muchos lenguajes de programación modernos. application/json es el tipo de medio utilizado para JSON.

Aspose.Cells es compatible con la posibilidad de guardar archivos en JSON o XML.

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
- [Ajustar el nivel de compresión del libro de trabajo](/cells/es/nodejs-cpp/adjust-workbook-compression-level/)
- [Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto](/cells/es/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Guardando archivo en objeto de respuesta](/cells/es/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
