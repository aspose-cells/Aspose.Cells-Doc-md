---
title: Отслеживание процесса конвертации документа
type: docs
weight: 120
url: /ru/java/track-document-conversion-progress/
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занимать некоторое время. Во время этого, вы можете показать процесс преобразования документа вместо простого экрана загрузки для улучшения удобства использования вашего приложения. Aspose.Cells поддерживает отслеживание процесса преобразования документа, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) предоставляет методы [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs)) и [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs)), которые вы можете реализовать в своем собственном классе. Вы также можете контролировать, какие страницы рендерятся, как показано в пользовательском классе *TestPageSavingCallback*.

## **Отслеживание прогресса конвертации документов**

В следующем образце кода загружается [исходный файл Excel](PagesBook1.xlsx) и выводится его процесс преобразования в консоли при использовании пользовательского класса *TestPageSavingCallback*, реализующего интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback).

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Ниже приведен код для пользовательского класса *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Вывод в консоль**

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
