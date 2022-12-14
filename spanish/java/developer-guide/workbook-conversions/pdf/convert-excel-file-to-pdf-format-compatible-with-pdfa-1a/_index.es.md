---
title: Convierta un archivo de Excel a formato PDF compatible con PDFA-1a
type: docs
weight: 80
url: /es/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Posibles escenarios de uso**

PDF/A es una variante única de PDF diseñada para la conservación de documentos a largo plazo. PDF/A es una versión estandarizada por ISO del formato de documento portátil (PDF), que es un formato de archivo de PDF que incorpora todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A se diferencia de PDF al prohibir funciones, como la vinculación de fuentes (a diferencia de la incrustación de fuentes) y el cifrado. Aspose.Cells le permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (se admiten tanto PdfA1a como PdfA1b). Este tema describe cómo guardar el libro de Excel en un archivo PDF compatible con PDF/A (PdfA1a).

## **Convierta un archivo de Excel a formato PDF compatible con PDFA-1a**

Los desarrolladores pueden usar el**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class para establecer diferentes atributos para la conversión. Configuración de diferentes propiedades del**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class le brinda control sobre la configuración de impresión, fuente, seguridad y compresión para el PDF de salida. La propiedad más importante es**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**que le permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

 El siguiente código de ejemplo explica cómo convertir un archivo de Excel a un formato PDF compatible con PDFA-1a. Por favor vea su[PDF de salida](outputCompliancePdfA1a.pdf) así como una captura de pantalla como referencia.

## **Captura de pantalla**

![todo:imagen_alternativa_texto](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
