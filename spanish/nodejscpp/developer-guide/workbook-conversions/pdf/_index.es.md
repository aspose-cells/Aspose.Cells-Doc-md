---
title: PDF con Node.js vía C++
linktitle: Pdf
type: docs
weight: 220
url: /es/nodejs-cpp/convert-excel-to-pdf/
description: Aprende cómo convertir un libro de Excel a PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells admite la conversión de Libro de Trabajo de Excel a PDF. En este ejemplo, veremos la conversión completa de un Libro de Trabajo de Excel a PDF.
{{% /alert %}}

## **Conversión de libro de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ escribe directamente la información sobre API y Número de Versión en los documentos de salida. Por ejemplo, al renderizar un Documento a PDF, Aspose.Cells for Node.js via C++ llena el campo **Productor de PDF** con el valor, por ejemplo 'Aspose.Cells v23.2'.

Tenga en cuenta que puede cambiar esta información en los Documentos de salida por medio de la propiedad [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--).
{{% /alert %}}

### **Conversión Directa**

Aspose.Cells for Node.js via C++ soporta la conversión de hojas de cálculo a PDF independientemente de otro software. Simplemente guarda un archivo de Excel como PDF usando el método [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). El método [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) proporciona el miembro de enumeración [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) que convierte los archivos nativos de Excel a formato PDF.

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instancia un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realiza cualquier trabajo (ingreso de datos, aplicación de formato, definición de fórmulas, inserción de imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo usando las APIs de Aspose.Cells.
1. Cuando el código de la hoja de cálculo está completo, llama al método [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) para guardar la hoja de cálculo.

El formato de archivo debe ser PDF, por lo que seleccione *Pdf* (un valor predefinido) de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) para generar el documento final en PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Conversión Avanzada**

También puede optar por usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) para configurar diferentes atributos para la conversión. El establecimiento de diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) le da control sobre la impresión, la fuente, la seguridad y la configuración de compresión para el PDF de salida. 

La propiedad más importante es [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) que le permite configurar el nivel de cumplimiento de los estándares PDF. Actualmente, puede guardar en los formatos PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab y PDF/A-3u. Tenga en cuenta que con el formato PDF/A, el tamaño de archivo de salida es más grande que el tamaño de archivo PDF regular.

#### **Guardando el Libro de Trabajo en Archivos PDF/A Compilados**

El fragmento de código proporcionado a continuación demuestra cómo utilizar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) para guardar archivos de Excel en formato PDF/A compatible.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Ten en cuenta que, la propiedad [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) fue agregada con el lanzamiento de Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **Establecer la Hora de Creación del PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), puede obtener o establecer la hora de creación del PDF. El siguiente código demuestra el uso de la propiedad [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) para establecer la hora de creación del archivo PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Establecer la opción ContentCopyForAccessibility**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), puede obtener o establecer la opción [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) del PDF para controlar el acceso al contenido en el PDF convertido.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Exportar Propiedades Personalizadas a PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), puede exportar las propiedades personalizadas en el libro de origen al PDF. Se proporciona el enumerador [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción Propiedades, como se muestra en la siguiente imagen. El archivo de plantilla "sourceWithCustProps.xlsx" se puede descargar [aquí](sourceWithCustProps.xlsx) para realizar pruebas y el archivo PDF de salida "outSourceWithCustProps" está disponible [aquí](outSourceWithCustProps.pdf) para su análisis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Atributos de Conversión**

Trabajamos para mejorar las características de conversión con cada nueva versión. La conversión de Excel a PDF de Aspose.Cells todavía tiene un par de limitaciones. MapChart no es compatible al convertir a formato PDF. Además, algunos objetos de dibujo no son bien compatibles.

La tabla que sigue lista todas las características que son completamente o parcialmente soportadas al exportar a PDF con Aspose.Cells. Esta tabla no es final y no cubre todos los atributos de la hoja de cálculo, pero identifica aquellas características que no son soportadas o parcialmente soportadas para la conversión a PDF.

|**Elemento del Documento**|**Atributo**|**Compatible**|**Notas**|
| :- | :- | :- | :- |
|Alineación| |Sí| |
|Configuraciones de fondo| |Sí| |
|Borde|Color|Sí| |
|Borde|Estilo de línea|Sí| |
|Borde|Ancho de línea|Sí| |
|Datos de celda| |Sí| |
|Comentarios| |Sí| |
|Formato condicional| |Sí| |
|Propiedades del documento| |Sí| |
|Objetos de dibujo| |Parcialmente|Las sombras y los efectos 3D para los objetos de dibujo no son bien compatibles; WordArt y SmartArt son parcialmente compatibles.|
|Fuente|Tamaño|Sí| |
|Fuente|Color|Sí| |
|Fuente|Estilo|Sí| |
|Fuente|Subrayado|Sí| |
|Fuente|Efectos|Sí||
|Imágenes| |Sí| |
|Hipervínculo| |Sí| |
|Gráficos| |Parcialmente| El MapChart no es compatible.|
|Celdas fusionadas| |Sí| |
|Salto de página| |Sí| |
|Configuración de página|Encabezado/Pie de página|Sí| |
|Configuración de página|Márgenes|Sí| |
|Configuración de página|Orientación de la página|Sí| |
|Configuración de página|Tamaño de la página|Sí| |
|Configuración de página|Área de impresión|Sí| |
|Configuración de página|Títulos de impresión|Sí| |
|Configuración de página|Escalado|Sí| |
|Altura de fila/Ancho de columna| |Sí| |
|Idioma RTL (de derecha a izquierda)| |Sí| |

{{% alert color="primary" %}}
Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.
{{% /alert %}}

## **Temas avanzados**
- [Agregar Marcadores de PDF con Destinos Nombrados](/cells/es/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir](/cells/es/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Cambie la fuente solo en los caracteres Unicode específicos al guardar en PDF](/cells/es/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convertir Archivo XLSX a Formato PDF](/cells/es/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Convertir archivo de Excel a formato PDF compatible con PDFA-1a](/cells/es/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir archivo XLS con imágenes o gráficos a PDF](/cells/es/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crear entrada de marcador de PDF para hoja de gráfico](/cells/es/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajustar todas las columnas de la hoja de cálculo en una sola página de PDF](/cells/es/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenga DrawObject y Bound al renderizar a PDF utilizando la clase DrawObjectEventHandler](/cells/es/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenga advertencias por sustitución de fuentes al renderizar el archivo de Excel](/cells/es/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorar errores al renderizar Excel a PDF](/cells/es/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limitar el número de páginas generadas - Conversión de Excel a PDF](/cells/es/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimir comentarios al guardar en PDF](/cells/es/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Renderizar complementos de Office al convertir Excel a PDF](/cells/es/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Renderizar una página de PDF por hoja de cálculo de Excel - Conversión de Excel a PDF](/cells/es/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells](/cells/es/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Muestrear imágenes agregadas - Conversión de Excel a PDF](/cells/es/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Guardar cada hoja de cálculo en un archivo PDF diferente](/cells/es/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Guardar Excel en PDF con tamaño estándar o mínimo](/cells/es/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Guardar hojas de cálculo especificadas en PDF](/cells/es/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Documentos PDF seguros](/cells/es/nodejs-cpp/secure-pdf-documents/)
- [Especificar cómo cruzar cadenas en el PDF de salida e imagen](/cells/es/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
