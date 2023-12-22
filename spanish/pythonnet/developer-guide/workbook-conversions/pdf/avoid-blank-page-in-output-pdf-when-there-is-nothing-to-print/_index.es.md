---
title: Evite páginas en blanco en la salida PDF cuando no hay nada que imprimir
type: docs
weight: 30
url: /es/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aprenda cómo evitar páginas en blanco en la salida PDF cuando no hay nada para imprimir con Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Posibles escenarios de uso**

Cuando el archivo de Excel está vacío y el usuario lo guarda en PDF usando Aspose.Cells for Python via .NET, muestra una página en blanco en la salida PDF. A veces, este comportamiento predeterminado no es deseable. Aspose.Cells for Python via .NET proporciona la[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)propiedad para abordar este problema. Si lo configura como *falso**, entonces[**Excepción de celdas**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)ocurrirá siempre que no haya nada que imprimir en la salida PDF.

##  **Evite páginas en blanco en la salida PDF cuando no hay nada que imprimir**

El siguiente código de muestra crea un libro vacío y luego lo guarda como PDF después de configurar el[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)propiedad como *falsa**. Como no hay nada que imprimir en la salida PDF, el[**Excepción de celdas**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)ocurre como se muestra a continuación.

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Excepción**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
