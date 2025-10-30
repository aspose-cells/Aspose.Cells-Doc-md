---
title: Seguimiento del progreso de conversión de documentos con Golang via C++
linktitle: Seguimiento del progreso de conversión de documentos
type: docs
weight: 970
url: /es/go-cpp/track-document-conversion-progress/
description: Aprende cómo rastrear el progreso de la conversión de documentos en C++ usando Aspose.Cells para mejorar la usabilidad de la aplicación.
---

## **Escenarios de uso posibles**

A veces, convertir archivos Excel grandes puede tomar algún tiempo. Durante este proceso, es posible que quieras mostrar el progreso de la conversión en lugar de solo una pantalla de carga para mejorar la usabilidad de tu aplicación. Aspose.Cells soporta el seguimiento del progreso mediante la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) proporciona los métodos [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) y [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) que puedes implementar en tu clase personalizada. También puedes controlar qué páginas se renderizan, como se demuestra en la clase personalizada `TestPageSavingCallback`.

## **Seguimiento del progreso de conversión de documentos**

El siguiente ejemplo carga el archivo de Excel de origen y muestra su progreso de conversión en la consola usando la clase personalizada `TestPageSavingCallback` que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
El siguiente es el código para la clase personalizada `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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
