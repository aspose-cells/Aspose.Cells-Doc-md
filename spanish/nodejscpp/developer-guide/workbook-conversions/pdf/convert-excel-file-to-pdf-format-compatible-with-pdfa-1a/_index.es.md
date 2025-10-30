---  
title: Convertir archivo de Excel a formato PDF compatible con PDF/A 1a con Node.js a través de C++  
linktitle: Convertir archivo de Excel a formato PDF compatible con PDF/A 1a  
type: docs  
weight: 130  
url: /es/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Aprende cómo convertir archivos de Excel a archivos PDF compatibles con PDF/A usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

PDF/A es una versión única de PDF diseñada para la conservación a largo plazo de documentos. PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) que es un formato de archivo archivístico de PDF que incrusta todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A difiere de PDF al prohibir funciones como la vinculación de fuentes (en lugar de incrustación de fuentes) y la encriptación. Aspose.Cells for Node.js via C++ te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab y PDF/A-3u son compatibles). Este tema describe cómo guardar el libro de Excel en un archivo PDF compatible con PDF/A (PDF/A-1a).  

## **Convertir archivo de Excel al formato PDF compatible con PDF/A-1a**  

 Los desarrolladores pueden usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) para establecer diferentes atributos para la conversión. Configurar diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) te da control sobre la impresión, fuente, seguridad y configuraciones de compresión para el PDF de salida. La propiedad más importante es [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), que te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.  

El siguiente código de ejemplo explica cómo convertir un archivo de Excel a formato PDF compatible con PDF/A-1a. Por favor, veas su [PDF de salida](outputCompliancePdfA1a.pdf) así como la captura de pantalla para referencia.  

## **Captura de pantalla**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
