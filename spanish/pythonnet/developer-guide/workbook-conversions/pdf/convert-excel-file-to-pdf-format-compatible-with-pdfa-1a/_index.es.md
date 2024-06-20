---
title: Convertir archivo de Excel a formato PDF compatible con PDFA 1a
type: docs
weight: 130
url: /es/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aprende cómo convertir archivo de Excel a formato PDF compatible con PDFA 1a con Aspose.Cells para el API de Python via .NET.
keywords: Python Convertir archivo de Excel a formato PDF compatible con PDFA 1a, PDFA 1a, PDFA 1b, PDF14, PDF15, PDF16, PDF17
---

## **Escenarios de uso posibles**

PDF/A es una variante única de PDF diseñada para la preservación a largo plazo de documentos. PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) que es un formato de archivo de PDF que incrusta todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A difiere de PDF al prohibir características, como el enlace de fuentes (en lugar de la incrustación de fuentes) y el cifrado. Aspose.Cells para Python via .NET te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (tanto PdfA1a como PdfA1b son compatibles). Este tema describe cómo guardar el libro de Excel en un archivo PDF/A conforme (PdfA1a).

## **Convertir archivo de Excel a formato PDF compatible con PDFA-1a**

Los desarrolladores pueden utilizar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) para establecer diferentes atributos para la conversión. Establecer diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) te da control sobre la impresión, fuentes, configuraciones de seguridad y compresión para el PDF de salida. La propiedad más importante es [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) que te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

El siguiente código de ejemplo explica cómo convertir un archivo de Excel a un formato PDF compatible con PDFA-1a. Por favor consulta su [PDF de salida](outputCompliancePdfA1a.pdf) así como la captura de pantalla como referencia.

## **Captura de pantalla**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertExcelFileToPDFA_1a.py" >}}
