---
title: Seguimiento del progreso de conversión de documentos
type: docs
weight: 120
url: /es/java/track-document-conversion-progress/
---

## **Escenarios de uso posibles**

A veces, la conversión de archivos excel grandes puede llevar cierto tiempo. Durante este tiempo, es posible que desee mostrar el progreso de la conversión del documento en lugar de solo una pantalla de carga para mejorar la usabilidad de su aplicación. Aspose.Cells admite el seguimiento del proceso de conversión de documentos proporcionando la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) proporciona los métodos [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) y [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) que puede implementar en su clase personalizada. También puede controlar qué páginas se renderizan, como se muestra en la clase personalizada *TestPageSavingCallback*.

## **Seguimiento del progreso de conversión de documentos**

El siguiente ejemplo de código carga el [archivo de excel fuente](PagesBook1.xlsx) e imprime su progreso de conversión en la consola mediante la clase personalizada *TestPageSavingCallback* que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback).

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

El siguiente es el código para la clase personalizada *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
