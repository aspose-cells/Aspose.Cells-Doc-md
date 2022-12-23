---
title: Ignorar errores al renderizar Excel a PDF
type: docs
weight: 80
url: /es/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Posibles escenarios de uso**

 A veces, cuando convierte su archivo de Excel a PDF, se producen errores o excepciones y finaliza el proceso de conversión. Puede ignorar todos estos errores durante el proceso de conversión utilizando el[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)propiedad. De esta manera, el proceso de conversión se completará sin problemas sin arrojar ningún error o excepción, pero puede ocurrir la pérdida de datos. Por lo tanto, utilice esta propiedad solo si la pérdida de datos no es crítica para usted.

## **Ignorar errores al renderizar Excel a PDF**

 El siguiente código carga el[ejemplo de archivo de Excel](55541778.xlsx) pero el archivo de muestra de Excel es erróneo y arroja un error durante[conversión a PDF](55541779.pdf) en 17.11 pero como estamos usando[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)propiedad, no arroja un error. Sin embargo, uno*flecha roja redondeada como forma*como se muestra en esta captura de pantalla se pierde.

![todo:imagen_alternativa_texto](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
