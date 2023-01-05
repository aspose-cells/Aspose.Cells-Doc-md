---
title: Salida de página en blanco cuando no hay nada que imprimir
type: docs
weight: 90
url: /es/net/output-blank-page-when-there-is-nothing-to-print/
---
## **Posibles escenarios de uso**

 Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada cuando exporte la hoja de trabajo a la imagen. Puedes cambiar este comportamiento usando[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propiedad. cuando lo vas a configurar**verdadero**, imprimirá la página en blanco.

## **Salida de página en blanco cuando no hay nada que imprimir**

El siguiente código de ejemplo crea el libro de trabajo vacío que tiene una hoja de trabajo vacía y representa la hoja de trabajo vacía en una imagen después de configurar el[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propiedad como**verdadero**. En consecuencia, genera la página en blanco ya que no hay nada que imprimir, como puede ver en la imagen a continuación.

![todo:imagen_alternativa_texto](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
