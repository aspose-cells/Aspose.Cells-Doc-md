---
title: Seguir el progreso de conversión de Excel a TIFF con Golang mediante C++
linktitle: Seguir el progreso de conversión de Excel a TIFF
type: docs
weight: 190
url: /es/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aprenda cómo seguir el progreso de conversión de archivos de Excel a formato TIFF usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

 A veces, convertir archivos grandes de Excel puede tomar algo de tiempo. Durante este tiempo, quizás desee mostrar el progreso de conversión del documento en lugar de una pantalla de carga para mejorar la usabilidad de su aplicación. Aspose.Cells soporta el seguimiento del progreso de conversión del documento proporcionando la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) proporciona los métodos [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) y [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) que puede implementar en su clase personalizada. También puede controlar qué páginas se renderizan, como se demuestra en la clase personalizada *TestPageSavingCallback*.

## **Seguir el progreso de conversión de Excel a TIFF**

El siguiente ejemplo carga el [archivo de Excel de origen](95584311.xlsx) y muestra su progreso de conversión en la consola usando la clase personalizada *TestPageSavingCallback* que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). El archivo de salida generado se adjunta para su referencia.

[Output File](95584312.tiff)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
El siguiente es el código para la clase personalizada *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
End saving page index 8 of pages 10</br>

{{< /highlight >}}
