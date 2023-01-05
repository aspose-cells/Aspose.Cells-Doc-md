---
title: Evite la página en blanco en la salida PDF cuando no hay nada que imprimir
type: docs
weight: 30
url: /es/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Posibles escenarios de uso**

Cuando el archivo de Excel está vacío y el usuario lo guarda en PDF usando Aspose.Cells, muestra una página en blanco en la salida PDF. A veces, este comportamiento predeterminado no es deseable. Aspose.Cells proporciona el[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) propiedad para hacer frente a este problema. Si lo vas a configurar como**falso**, después[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)ocurrirá siempre que no haya nada que imprimir en la salida PDF.

## **Evite la página en blanco en la salida PDF cuando no hay nada que imprimir**

El siguiente código de muestra crea un libro de trabajo vacío y luego lo guarda como salida PDF después de configurar el[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) propiedad como**falso**. Como no hay nada que imprimir en la salida PDF, el[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)ocurre como se muestra a continuación.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Excepción**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
