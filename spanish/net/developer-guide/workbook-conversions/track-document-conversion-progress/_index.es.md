---
title: Seguimiento del progreso de conversión de documentos
type: docs
weight: 970
url: /es/net/track-document-conversion-progress/
---

## **Escenarios de uso posibles**

A veces, convertir archivos grandes de Excel puede llevar algo de tiempo. Durante este tiempo, es posible que desees mostrar el progreso de la conversión del documento en lugar de simplemente una pantalla de carga para mejorar la usabilidad de tu aplicación. Aspose.Cells admite el seguimiento del proceso de conversión del documento proporcionando la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) proporciona los métodos [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) y [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) que puedes implementar en tu clase personalizada. También puedes controlar qué páginas se renderizan, como se demuestra en la clase personalizada *TestPageSavingCallback*.

## **Seguimiento del progreso de conversión de documentos**

El siguiente ejemplo de código carga el [archivo de Excel fuente](94896151.xlsx) e imprime su progreso de conversión en la consola mediante la clase personalizada *TestPageSavingCallback* que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback).

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

El siguiente es el código para la clase personalizada *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
