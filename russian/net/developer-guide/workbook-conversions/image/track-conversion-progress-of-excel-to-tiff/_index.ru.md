---
title: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 190
url: /ru/net/track-conversion-progress-of-excel-to-tiff/
---
## **Возможные сценарии использования**

 Иногда преобразование больших файлов Excel может занять некоторое время. В это время вы можете захотеть показать ход преобразования документа, а не просто экран загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells поддерживает процесс преобразования документа отслеживания, предоставляя**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** интерфейс.**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**интерфейс обеспечивает**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**и**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**методы, которые вы можете реализовать в своем пользовательском классе. Вы также можете контролировать, какие страницы отображаются, как показано в T*estPageSavingCallback*пользовательский класс.

## **Отслеживание процесса преобразования Excel в TIFF**

 Следующий пример кода загружает[исходный файл excel](95584311.xlsx) и выводит ход преобразования в консоли с помощью команды*TestPageSavingCallback* пользовательский класс, который реализует**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**интерфейс. Сгенерированный выходной файл прилагается для справки.

[Выходной файл](95584312.tiff)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Ниже приведен код для*TestTiffPageSavingCallback*пользовательский класс.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
Завершить сохранение индекса страницы 8 из страниц 10</br>

