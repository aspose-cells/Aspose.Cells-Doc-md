---
title: Отслеживание прогресса преобразования документа с помощью Golang через C++
linktitle: Отслеживание процесса конвертации документа
type: docs
weight: 970
url: /ru/go-cpp/track-document-conversion-progress/
description: Узнайте, как отслеживать прогресс преобразования документа в C++ с помощью Aspose.Cells для повышения удобства использования приложения.
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel занимает некоторое время. В этот период вы можете отображать прогресс преобразования документа вместо просто экрана загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells поддерживает отслеживание прогресса преобразования документа через интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) предоставляет методы [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) и [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/), которые можно реализовать в вашем собственном классе. Также вы можете управлять тем, какие страницы рендерятся, как показано в пользовательском классе `TestPageSavingCallback`.

## **Отслеживание прогресса конвертации документов**

Следующий пример кода загружает исходный файл Excel и выводит прогресс его преобразования в консоль, используя пользовательский класс `TestPageSavingCallback`, реализующий интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Следующий код — это пользовательский класс `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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
