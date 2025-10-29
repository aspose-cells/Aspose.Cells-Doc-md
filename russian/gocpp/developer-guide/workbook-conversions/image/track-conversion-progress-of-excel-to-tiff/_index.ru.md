---
title: Отслеживание прогресса конвертации Excel в TIFF с помощью Golang через C++
linktitle: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 190
url: /ru/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Узнайте, как отслеживать прогресс преобразования файлов Excel в формат TIFF, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занять некоторое время. В этот момент вы можете захотеть показывать прогресс преобразования документа вместо просто экрана загрузки, чтобы улучшить удобство использования вашего приложения. Aspose.Cells поддерживает отслеживание прогресса преобразования документов, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) обеспечивает методы [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) и [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/), которые вы можете реализовать в вашем пользовательском классе. Также вы можете управлять тем, какие страницы рендерятся, как продемонстрировано в пользовательском классе *TestPageSavingCallback*.

## **Отслеживание процесса преобразования Excel в TIFF**

Следующий пример кода загружает [исходный файл Excel](95584311.xlsx) и выводит прогресс преобразования в консоль, используя пользовательский класс *TestPageSavingCallback*, реализующий интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Генерируемый файл прикреплён для вашего ознакомления.

[Output File](95584312.tiff)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Ниже приведен код для пользовательского класса *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
