---
title: Seguir el progreso de conversión de Excel a TIFF
type: docs
weight: 140
url: /es/java/track-conversion-progress-of-excel-to-tiff/
---

## **Escenarios de uso posibles**

A veces, la conversión de archivos grandes de Excel puede llevar algo de tiempo. Durante este tiempo, es posible que desees mostrar el progreso de conversión del documento en lugar de solo una pantalla de carga para mejorar la usabilidad de tu aplicación. Aspose.Cells admite el seguimiento del proceso de conversión del documento proporcionando la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) proporciona los métodos [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs)) y [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs)) que puedes implementar en tu clase personalizada. También puedes controlar qué páginas se renderizan como se demuestra en la clase personalizada *TestTiffPageSavingCallback*.

## **Seguir el progreso de conversión de Excel a TIFF**

El siguiente ejemplo de código carga el [archivo de Excel fuente](sampleUseWorkbookRenderForImageConversion.xlsx) e imprime su progreso de conversión en la consola, utilizando la clase personalizada *TestTiffPageSavingCallback* que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). El archivo de salida generado está adjunto para tu referencia.

[Archivo de salida](DocumentConversionProgressForTiff_out.tiff)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

El siguiente es el código para la clase personalizada *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Salida de la consola**

{{< highlight java >}}
Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10

{{< /highlight >}}
