---
title: Seguimiento del progreso de la conversión de documentos
type: docs
weight: 120
url: /es/java/track-document-conversion-progress/
---
## **Posibles escenarios de uso**

veces, la conversión de archivos de Excel de gran tamaño puede llevar algún tiempo. Durante este tiempo, es posible que desee mostrar el progreso de la conversión del documento en lugar de solo una pantalla de carga para mejorar la usabilidad de su aplicación. Aspose.Cells admite el proceso de conversión de documentos de seguimiento al proporcionar el**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz. los**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz proporciona**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**y**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** métodos que puede implementar en su clase personalizada. También puede controlar qué páginas se procesan como se muestra en el*TestPageSavingCallback*clase personalizada.

## **Seguimiento del progreso de la conversión de documentos**

El siguiente ejemplo de código carga el[archivo fuente excel](PagesBook1.xlsx)e imprime su progreso de conversión en la consola usando el*TestPageSavingCallback*clase personalizada que implementa el**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaz.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

El siguiente es el código para el*TestPageSavingCallback*clase personalizada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Salida de consola**

Empezar a guardar el índice de la página 0 de las páginas 11</br>
Terminar de guardar el índice de página 0 de las páginas 11</br>
Empezar a guardar el índice de la página 1 de las páginas 11</br>
Terminar de guardar el índice de página 1 de las páginas 11</br>
Empezar a guardar el índice de la página 2 de las páginas 11</br>
Terminar de guardar el índice de la página 2 de las páginas 11</br>
Empezar a guardar el índice de la página 3 de las páginas 11</br>
Terminar de guardar el índice de la página 3 de las páginas 11</br>
Comience a guardar el índice de la página 4 de las páginas 11</br>
Terminar de guardar el índice de página 4 de las páginas 11</br>
Empezar a guardar el índice de la página 5 de las páginas 11</br>
Terminar de guardar el índice de la página 5 de las páginas 11</br>
Comience a guardar el índice de la página 6 de las páginas 11</br>
Terminar de guardar el índice de página 6 de las páginas 11</br>
Empezar a guardar el índice de la página 7 de las páginas 11</br>
Terminar de guardar el índice de página 7 de las páginas 11</br>
Empezar a guardar el índice de la página 8 de las páginas 11</br>
Terminar de guardar el índice de la página 8 de las páginas 11
