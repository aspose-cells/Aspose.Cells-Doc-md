---
title: Convertir archivo de Excel a formato PDF compatible con PDFA 1a con Golang vía C++
linktitle: Convertir archivo de Excel a formato PDF compatible con PDFA 1a
type: docs
weight: 130
url: /es/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aprende cómo convertir archivos de Excel a formato PDF/A 1a usando Aspose.Cells con Golang vía C++.
---

## **Escenarios de uso posibles**

 PDF/A es una variante única de PDF diseñada para la conservación a largo plazo de documentos. PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) que es un formato de archivo archivístico que incrusta todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A difiere de PDF al prohibir funciones como la vinculación de fuentes (en lugar de incrustarlas) y el cifrado. Aspose.Cells te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, y PDF/A-3u son compatibles). Este tema describe cómo guardar el libro de Excel en un archivo PDF compatible con PDF/A (PDF/A-1a).

## **Convertir archivo de Excel al formato PDF compatible con PDF/A-1a**

 Los desarrolladores pueden usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) para establecer diferentes atributos para la conversión. Configurar diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) te da control sobre la impresión, fuente, seguridad y configuraciones de compresión para el PDF de salida. La propiedad más importante es [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), que te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

El siguiente código de muestra explica cómo convertir un archivo de Excel al formato PDF compatible con PDF/A-1a. Consulta su [PDF de salida](outputCompliancePdfA1a.pdf) así como la captura de pantalla para referencia.

## **Captura de pantalla**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
