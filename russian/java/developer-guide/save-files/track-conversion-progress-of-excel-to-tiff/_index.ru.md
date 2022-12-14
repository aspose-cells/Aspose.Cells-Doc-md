---
title: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 140
url: /ru/java/track-conversion-progress-of-excel-to-tiff/
---
## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занять некоторое время. В это время вы можете захотеть показать ход преобразования документа, а не просто экран загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells поддерживает процесс преобразования документа отслеживания, предоставляя**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**интерфейс.**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**интерфейс обеспечивает**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**а также**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** методы, которые вы можете реализовать в своем пользовательском классе. Вы также можете управлять отображением страниц, как показано в*TestTiffPageSavingCallback*пользовательский класс.

## **Отслеживание процесса преобразования Excel в TIFF**

Следующий пример кода загружает[исходный файл excel](sampleUseWorkbookRenderForImageConversion.xlsx)и выводит ход преобразования в консоли с помощью команды*TestTiffPageSavingCallback*пользовательский класс, который реализует**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**интерфейс. Сгенерированный выходной файл прилагается для справки.

[Выходной файл](DocumentConversionProgressForTiff_out.tiff)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Ниже приведен код для*TestTiffPageSavingCallback*пользовательский класс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Консольный вывод**

Начать сохранение индекса страницы 0 из страниц 10</br>
Завершить сохранение индекса страницы 0 из страниц 10</br>
Начать сохранение индекса страницы 1 из страниц 10</br>
Завершить сохранение индекса страницы 1 из страниц 10</br>
Начать сохранение указателя страниц 2 из страниц 10</br>
Завершить сохранение указателя страниц 2 из страниц 10</br>
Начать сохранение указателя страницы 3 из страниц 10</br>
Завершить сохранение указателя страниц 3 из страниц 10</br>
Начать сохранение индекса страниц 4 из страниц 10</br>
Завершить сохранение указателя страниц 4 из страниц 10</br>
Начать сохранение индекса страницы 5 из страниц 10</br>
Завершить сохранение индекса страницы 5 из страниц 10</br>
Начать сохранение индекса страницы 6 из страниц 10</br>
Завершить сохранение индекса 6 страницы из 10</br>
Начать сохранение индекса страницы 7 из страниц 10</br>
Завершить сохранение индекса страницы 7 из страниц 10</br>
Начать сохранение индекса страницы 8 из страниц 10</br>
Завершить сохранение индекса страницы 8 из страниц 10
