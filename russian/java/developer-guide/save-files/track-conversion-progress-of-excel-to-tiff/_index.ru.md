---
title: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 140
url: /ru/java/track-conversion-progress-of-excel-to-tiff/
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занимать некоторое время. Во время этого, вы можете показать процесс преобразования документа вместо простого экрана загрузки для улучшения удобства использования вашего приложения. Aspose.Cells поддерживает отслеживание процесса преобразования документа, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) предоставляет методы [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) и [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-), которые вы можете реализовать в своем собственном классе. Вы также можете контролировать, какие страницы рендерятся, как показано в пользовательском классе *TestTiffPageSavingCallback*.

## **Отслеживание процесса преобразования Excel в TIFF**

В следующем образце кода загружается [исходный файл Excel](sampleUseWorkbookRenderForImageConversion.xlsx) и выводится его процесс преобразования в консоли при использовании пользовательского класса *TestTiffPageSavingCallback*, реализующего интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). Сгенерированный выходной файл прикреплен для вашего ознакомления.

[Файл вывода](DocumentConversionProgressForTiff_out.tiff)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Ниже приведен код для пользовательского класса *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

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
End saving page index 8 of pages 10

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
