---
title: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 190
url: /ru/net/track-conversion-progress-of-excel-to-tiff/
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занять некоторое время. В этот момент вы можете хотеть отображать процесс преобразования документов вместо простого экрана загрузки для повышения удобства использования вашего приложения. Aspose.Cells поддерживает отслеживание процесса преобразования документов, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) предоставляет методы [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) и [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving), которые вы можете реализовать в своем собственном классе. Вы также можете управлять тем, какие страницы рендерятся, как показано на примере класса пользовательского  T*estPageSavingCallback*.

## **Отслеживание процесса преобразования Excel в TIFF**

Приведенный ниже образец кода загружает [исходный файл Excel](95584311.xlsx) и печатает его ход преобразования в консоль, используя пользовательский класс *TestPageSavingCallback*, который реализует интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). Сгенерированный выходной файл прикреплен для вашего справления.

[Output File](95584312.tiff)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Ниже приведен код для пользовательского класса *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **Вывод в консоль**

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
{{< app/cells/assistant language="csharp" >}}
