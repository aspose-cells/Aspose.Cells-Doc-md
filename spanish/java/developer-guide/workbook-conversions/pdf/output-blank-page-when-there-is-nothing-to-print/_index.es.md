---
title: Salida de página en blanco cuando no hay nada que imprimir
type: docs
weight: 80
url: /es/java/output-blank-page-when-there-is-nothing-to-print/
---
## **Posibles escenarios de uso**

Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada cuando exporte la hoja de trabajo a la imagen. Puedes cambiar este comportamiento usando[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) propiedad. Cuándo lo configurarás**verdadero**, imprimirá la página en blanco.

## **Salida de página en blanco cuando no hay nada que imprimir**

El siguiente código de ejemplo crea el libro de trabajo vacío que tiene una hoja de trabajo vacía y representa la hoja de trabajo vacía en una imagen después de configurar el[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)propiedad como**verdadero**. En consecuencia, genera la página en blanco ya que no hay nada para imprimir que puede ver a continuación.

![todo:imagen_alternativa_texto](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
