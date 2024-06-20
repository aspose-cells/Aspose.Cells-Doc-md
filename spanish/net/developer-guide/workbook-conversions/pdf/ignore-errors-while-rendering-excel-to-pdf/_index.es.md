---
title: Ignorar Errores al Renderizar Excel a PDF
type: docs
weight: 80
url: /es/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Escenarios de uso posibles**

A veces, al convertir tu archivo de Excel a PDF, se producen errores o excepciones y el proceso de conversión se interrumpe. Puedes ignorar todos esos errores durante el proceso de conversión utilizando la propiedad [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror). De esta manera, el proceso de conversión se completará sin problemas sin arrojar ningún error o excepción, pero puede ocurrir la pérdida de datos. Por lo tanto, utiliza esta propiedad solo si la pérdida de datos no es crítica para ti.

## **Ignorar errores al renderizar Excel a PDF**

El siguiente código carga el [archivo de Excel de muestra](55541778.xlsx) pero el archivo de Excel de muestra es erróneo y arroja un error durante [la conversión a PDF](55541779.pdf) en la versión 17.11 pero como estamos utilizando la propiedad [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror), no arroja un error. Sin embargo, se pierde una *forma similar a una flecha roja redondeada* como se muestra en esta captura de pantalla.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
