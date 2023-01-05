---
title: Seguimiento del progreso de conversión de Excel a TIFF
type: docs
weight: 140
url: /es/java/track-conversion-progress-of-excel-to-tiff/
---
## **Posibles escenarios de uso**

A veces, la conversión de archivos de Excel de gran tamaño puede llevar algún tiempo. Durante este tiempo, es posible que desee mostrar el progreso de la conversión del documento en lugar de solo una pantalla de carga para mejorar la usabilidad de su aplicación. Aspose.Cells admite el proceso de conversión de documentos de seguimiento al proporcionar el**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz. Él**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz proporciona**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**y**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** métodos que puede implementar en su clase personalizada. También puede controlar qué páginas se procesan como se muestra en el*TestTiffPageSavingCallback*clase personalizada.

## **Seguimiento del progreso de conversión de Excel a TIFF**

El siguiente ejemplo de código carga el[archivo fuente excel](sampleUseWorkbookRenderForImageConversion.xlsx) e imprime su progreso de conversión en la consola usando el*TestTiffPageSavingCallback*clase personalizada que implementa el**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz. El archivo de salida generado se adjunta para su referencia.

[Archivo de salida](DocumentConversionProgressForTiff_out.tiff)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

El siguiente es el código para el*TestTiffPageSavingCallback*clase personalizada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Salida de consola**

Empezar a guardar el índice de página 0 de las páginas 10</br>
Terminar de guardar el índice de página 0 de las páginas 10</br>
Empezar a guardar el índice de la página 1 de las páginas 10</br>
Terminar de guardar el índice de página 1 de las páginas 10</br>
Empezar a guardar el índice de la página 2 de las páginas 10</br>
Terminar de guardar el índice de página 2 de las páginas 10</br>
Empezar a guardar el índice de la página 3 de las páginas 10</br>
Terminar de guardar el índice de la página 3 de las páginas 10</br>
Empezar a guardar el índice de la página 4 de las páginas 10</br>
Terminar de guardar el índice de la página 4 de las páginas 10</br>
Comience a guardar el índice de la página 5 de las páginas 10</br>
Terminar de guardar el índice de la página 5 de las páginas 10</br>
Empezar a guardar el índice de la página 6 de las páginas 10</br>
Terminar de guardar el índice de página 6 de las páginas 10</br>
Empezar a guardar el índice de la página 7 de las páginas 10</br>
Terminar de guardar el índice de página 7 de las páginas 10</br>
Empezar a guardar el índice de la página 8 de las páginas 10</br>
Terminar de guardar el índice de la página 8 de las páginas 10
