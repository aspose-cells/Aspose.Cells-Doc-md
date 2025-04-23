---
title: Evitar Página en Blanco en el PDF de Salida cuando no hay Nada que Imprimir
type: docs
weight: 30
url: /es/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Cuando el archivo de Excel está vacío y el usuario lo guarda como PDF usando Aspose.Cells, se representa una página en blanco en el PDF de salida. A veces, este comportamiento predeterminado es indeseable. Aspose.Cells proporciona la propiedad [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) para tratar este problema. Si la estableces como **false**, entonces [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) ocurrirá cuando no haya nada que imprimir en el PDF de salida.

## **Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir**

El siguiente código de ejemplo crea un libro de trabajo vacío y luego lo guarda como PDF de salida después de establecer la propiedad [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) como **false**. Dado que no hay nada que imprimir en el PDF de salida, el [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) ocurre como se muestra a continuación.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Excepción**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
