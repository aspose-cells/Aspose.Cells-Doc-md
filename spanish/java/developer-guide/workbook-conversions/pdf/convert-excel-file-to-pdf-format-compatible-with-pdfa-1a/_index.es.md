---
title: Convertir archivo de Excel a formato PDF compatible con PDFA 1a
type: docs
weight: 80
url: /es/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Escenarios de uso posibles**

PDF/A es una variante única de PDF diseñada para la preservación a largo plazo de documentos. PDF/A es una versión estandarizada por ISO del Formato de Documento Portable (PDF) que es un formato de archivo PDF que incrusta todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A difiere de PDF al prohibir características como enlace de fuentes (en lugar de incrustación de fuentes) y encriptación. Aspose.Cells te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (se admiten PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab y PDF/A-3u). Este tema describe cómo guardar el libro de Excel en un archivo PDF/A compatible (PDF/A-1a)

## **Convertir archivo de Excel al formato PDF compatible con PDF/A-1a**

Los desarrolladores pueden usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) para establecer diferentes atributos para la conversión. Establecer diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) te da control sobre las configuraciones de impresión, fuente, seguridad y compresión para el PDF de salida. La propiedad más importante es [PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) que te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

El siguiente código de muestra explica cómo convertir un archivo de Excel al formato PDF compatible con PDF/A-1a. Consulta su [PDF de salida](outputCompliancePdfA1a.pdf) así como una captura de pantalla para referencia.

## **Captura de pantalla**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
{{< app/cells/assistant language="java" >}}
