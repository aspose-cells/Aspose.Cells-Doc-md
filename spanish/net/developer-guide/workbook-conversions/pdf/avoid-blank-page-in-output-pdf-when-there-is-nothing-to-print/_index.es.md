---
title: Evite la página en blanco en la salida PDF cuando no hay nada que imprimir
type: docs
weight: 30
url: /es/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Posibles escenarios de uso**

Cuando el archivo de Excel está vacío y el usuario lo guarda en PDF usando Aspose.Cells, muestra una página en blanco en la salida PDF. A veces, este comportamiento predeterminado no es deseable. Aspose.Cells proporciona el[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) propiedad para hacer frente a este problema. Si lo vas a configurar como**falso**, después[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)ocurrirá siempre que no haya nada que imprimir en la salida PDF.

## **Evite la página en blanco en la salida PDF cuando no hay nada que imprimir**

El siguiente código de ejemplo crea un libro de trabajo vacío y luego lo guarda como PDF después de configurar el[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) propiedad como**falso**. Como no hay nada que imprimir en la salida PDF, el[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)ocurre como se muestra a continuación.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Excepción**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
