---
title: Evitar Página en Blanco en el PDF de Salida cuando no hay Nada que Imprimir
type: docs
weight: 30
url: /es/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Cuando el archivo de Excel está vacío y el usuario lo guarda como PDF usando Aspose.Cells, se representa una página en blanco en el PDF de salida. A veces, este comportamiento predeterminado es indeseable. Aspose.Cells proporciona la propiedad [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) para tratar este problema. Si la estableces como **false**, entonces [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) ocurrirá cuando no haya nada que imprimir en el PDF de salida.

## **Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir**

El siguiente código de ejemplo crea un libro de trabajo vacío y luego lo guarda como PDF después de establecer la propiedad [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) como **false**. Ya que no hay nada que imprimir en el PDF de salida, [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) ocurre como se muestra a continuación.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Excepción**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
