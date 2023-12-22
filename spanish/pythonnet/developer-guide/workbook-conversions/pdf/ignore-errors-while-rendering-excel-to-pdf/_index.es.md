---
title: Ignorar errores al representar Excel en PDF
type: docs
weight: 80
url: /es/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Aprenda a ignorar errores al representar Excel en PDF con Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Posibles escenarios de uso**

 A veces, cuando convierte su archivo de Excel a PDF, se producen errores o excepciones y el proceso de conversión finaliza. Puede ignorar todos estos errores durante el proceso de conversión utilizando el[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)propiedad. De esta manera, el proceso de conversión se completará sin problemas sin generar ningún error o excepción, pero puede ocurrir pérdida de datos. Por lo tanto, utilice esta propiedad sólo si la pérdida de datos no es crítica para usted.

##  **Ignorar errores al representar Excel en PDF**

 El siguiente código carga el[archivo de Excel de muestra](55541778.xlsx) pero el archivo de Excel de muestra es erróneo y arroja un error durante[conversión a PDF](55541779.pdf) en 17.11 pero ya que estamos usando[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)propiedad, no arroja un error. Sin embargo, uno*forma de flecha roja redondeada*como se muestra en esta captura de pantalla se pierde.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
