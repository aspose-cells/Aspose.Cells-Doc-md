---
title: Evitar Página en Blanco en el PDF de Salida cuando no hay Nada que Imprimir
type: docs
weight: 30
url: /es/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aprenda cómo evitar que aparezca una página en blanco en el PDF de salida cuando no hay nada que imprimir con Aspose.Cells para Python via .NET API.
keywords: Python Evitar Página en Blanco en PDF de Salida cuando no hay Nada que Imprimir
---

## **Escenarios de uso posibles**

Cuando el archivo de Excel está vacío y el usuario lo guarda en PDF usando Aspose.Cells para Python via .NET, renderiza una página en blanco en el PDF de salida. A veces, este comportamiento predeterminado es indeseable. Aspose.Cells para Python via .NET proporciona la propiedad [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) para abordar este problema. Si lo establece como **falso**, entonces [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) ocurrirá cada vez que no haya nada que imprimir en el PDF de salida.

## **Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir**

El siguiente código de ejemplo crea un libro de trabajo vacío y luego lo guarda como PDF después de establecer la propiedad [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) como **false**. Ya que no hay nada que imprimir en el PDF de salida, [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) ocurre como se muestra a continuación.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Excepción**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
