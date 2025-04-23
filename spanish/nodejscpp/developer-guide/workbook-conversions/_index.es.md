---  
title: Convertir Excel a Pdf, imagen y otros formatos  
linktitle: Conversiones de libros de trabajo  
type: docs  
weight: 65  
url: /es/nodejs-cpp/convert-workbook-to-different-formats/  
description: Convertir archivos Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más usando Node.js a través de C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.  
{{% /alert %}}  

## **Convertir libro de trabajo de Excel a PDF**  
Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.  

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Convertir Libro de Excel a JPG**  
Aspose.Cells soporta la conversión de archivos Excel a JPG. El ejemplo de código a continuación muestra cómo guardar un libro de trabajo como JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Convertir Libro de Excel a Imagen**  
Aspose.Cells soporta convertir archivos Excel a imágenes. El ejemplo de código a continuación muestra cómo guardar un libro de trabajo como imágenes.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Convirtiendo Libro de Excel a XPS**  
El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de renderizado para distribuir, archivar, renderizar, procesar e imprimir documentos.  

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos de gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas de la Fundación de Presentación de Windows (WPF). Los elementos utilizados se describen en términos de rutas y otras primitivas geométricas.  

Un archivo XPS es, de hecho, un archivo ZIP unicode que utiliza las Convenciones de Empaquetado Abierto, que contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como la información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admite archivos ZIP.  

A partir de Aspose.Cells 6.0.0, se admite la conversión de Microsoft Excel a XPS.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Convertir Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells soporta la conversión de archivos Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [ plantillas](book1.xlsx) en archivos Ods, Sxc y Fods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Convirtiendo Libro de Excel a Archivos MHTML**  
MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.  

Aspose.Cells admite la lectura y escritura de archivos MHTML.  

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Convirtiendo Libro de Excel a HTML**  
La API de Aspose.Cells ofrece soporte para exportar hojas de cálculo a formato HTML. Para esto, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) para ofrecer flexibilidad en el control de varios aspectos del HTML de salida.  

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Configuración de las Preferencias de Imagen para HTML**  
A partir de la versión 8.0.2, Aspose.Cells ha expuesto [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), permitiendo a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.  

A continuación se detallan algunas de las configuraciones de imagen que se pueden aplicar:  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Especifica el tipo de imagen. Por favor, tenga en cuenta que todas las formas, incluidos los gráficos, se renderizan como imágenes en el HTML de salida.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Especifica la calidad de la imagen de 0 a 100, cuando [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) se especifica como Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): Obtiene o establece el tipo de compresión para las imágenes cuando [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) se especifica como Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.  

## **Convertir Libro de Excel a Markdown**  
La API de Aspose.Cells soporta exportar hojas de cálculo a formato Markdown. Para exportar la hoja activa a Markdown, pase [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). También puede usar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) para especificar configuraciones adicionales para exportar la hoja a Markdown.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a Markdown usando el miembro de enumeración [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Consulte el [archivo Markdown generado](md_sample.txt) para referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Convertir Libro de Excel a JSON**  
Aspose.Cells soporta la conversión de un libro a JSON (JavaScript Object Notation).  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a Json usando el miembro de enumeración [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Consulte el código para convertir el [archivo fuente](Book1.xlsx) al [archivo Json resultado](Book1.Json) generado por el código para referencia.  

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

## **Convertir Excel a XML**  
Aspose.Cells admite la conversión de un libro de trabajo a XML de Hoja de Cálculo Excel 2003 y datos XML sin formato.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Convertir libro de Excel a TIFF**  
Aspose.Cells admite la conversión de un libro de trabajo a un archivo TIFF.  

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Convertir libro de Excel a DOCX**  
La API de Aspose.Cells soporta convertir hojas de cálculo a formato DOCX. Para exportar el libro a DOCX, pase [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). También puede usar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) para especificar configuraciones adicionales para exportar la hoja a DOCX.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a DOCX usando el miembro de enumeración [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Consulte el [archivo DOCX generado](Book1.docx) para referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Convertir libro de Excel a PPTX**  
La API de Aspose.Cells soporta convertir hojas de cálculo a formato PPTX. Para exportar el libro a PPTX, pase [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). También puede usar la clase [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) para especificar configuraciones adicionales para exportar la hoja a PPTX.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a PPTX usando el miembro de enumeración [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Consulte el [archivo PPTX generado](Book1.pptx) para referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Convertir Libro de Excel a EPUB**  
La API de Aspose.Cells soporta convertir hojas de cálculo a formato EPUB. Para exportar el libro a EPUB, pase [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) para especificar configuraciones adicionales para exportar la hoja a Epub.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a EPUB usando el miembro de enumeración [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Convertir Libro de Excel a AZW3**  
La API de Aspose.Cells soporta convertir hojas de cálculo a formato AZW3. Para exportar el libro a AZW3, pase [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) para especificar configuraciones adicionales para exportar la hoja a AZW3.  

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a AZW3 usando el miembro de enumeración [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Temas avanzados**  
- [Convertir Revisión de XLSB a XLSM](/cells/es/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/es/nodejs-cpp/convert-excel-to-html/)  
- [Imagen](/cells/es/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/es/nodejs-cpp/convert-workbook-to-json/)  
- [Convertir Libro de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc).](/cells/es/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/es/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Convertir Excel a CSV, TSV y Txt](/cells/es/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Seguimiento del progreso de conversión de documentos](/cells/es/nodejs-cpp/track-document-conversion-progress/)  
- [Convertir CSV, TSV y TXT a Excel](/cells/es/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

