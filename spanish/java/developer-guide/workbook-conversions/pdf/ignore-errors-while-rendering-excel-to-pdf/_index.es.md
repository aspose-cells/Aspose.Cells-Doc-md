---
title: Ignorar Errores al Renderizar Excel a PDF
type: docs
weight: 70
url: /es/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Escenarios de uso posibles**

A veces, al convertir su archivo de Excel a PDF, se producen errores o excepciones y el proceso de conversión se termina. Puede ignorar todos esos errores durante el proceso de conversión utilizando la propiedad [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError). De esta manera, el proceso de conversión se completará sin problemas sin generar ningún error o excepción, pero puede producirse pérdida de datos. Por lo tanto, utilice esta propiedad solo si la pérdida de datos no es crítica para usted.

## **Ignorar errores al renderizar Excel a PDF**

El siguiente código carga el [archivo de Excel de muestra](55541813.xlsx) pero el archivo de Excel de muestra es erróneo y arroja un error durante la [conversión a PDF](55541814.pdf) en 17.11, pero como estamos utilizando la propiedad [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError), no arroja un error. Sin embargo, se pierde una forma similar a una flecha roja redondeada como se muestra en esta captura de pantalla.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}
