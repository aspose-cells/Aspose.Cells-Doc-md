---
title: Как и где использовать перечисления с Golang через C++
linktitle: Итерация данных
type: docs
weight: 55
url: /ru/go-cpp/how-and-where-to-use-enumerators/
description: Узнайте, как использовать перечислители с помощью API Aspose.Cells for C++.
keywords: Как использовать перечислители, перечислитель ячеек, перечислитель строк, перечислитель столбцов
---

{{% alert color="primary" %}}

Перечислитель — это объект, предоставляющий возможность прохода по контейнеру или коллекции. Перечислители могут использоваться для чтения данных в коллекции, но не для изменения исходной коллекции, тогда как IEnumerable — это интерфейс, который определяет один метод GetEnumerator, возвращающий интерфейс IEnumerator, что, в свою очередь, обеспечивает только для чтения доступ к коллекции.

API Aspose.Cells предоставляет множество перечислителей, однако в данной статье обсуждаются в основном три типа, перечисленные ниже.

1. Перечислитель ячеек
1. Перечислитель строк
1. Перечислитель столбцов

{{% /alert %}}

## **Как использовать перечислители**

### **Перечислитель ячеек**

Существуют различные способы доступа к перечислителю ячеек, и можно использовать любые из этих методов в зависимости от требований приложения. Вот методы, возвращающие перечислитель ячеек.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Все вышеперечисленные методы возвращают перечислитель, который позволяет осуществлять обход коллекции ячеек, которые были инициализированы.

{{% alert color="primary" %}}

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию новой ячейки или удалению существующей). В противном случае перечислитель может не иметь возможности правильно обойти все ячейки (некоторые элементы могут быть обойдены повторно или пропущены).

{{% /alert %}}

Приведенный ниже пример кода демонстрирует реализацию интерфейса IEnumerator для коллекции Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Перечислитель строк**

Перебор строк можно осуществлять, используя метод [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/). Следующий пример демонстрирует реализацию интерфейса IEnumerator для [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Доступ к столбцам (Get)**

Доступ к столбцам осуществляется при использовании метода [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/). Следующий пример демонстрирует реализацию метода Get для [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Где использовать перечислители**

Чтобы обсудить преимущества использования перечислителей, давайте рассмотрим реальный пример.

**Сценарий**

Требование приложения — пройтись по всем ячейкам в заданном [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/), чтобы прочитать их значения. Для достижения этой цели существует несколько способов. Некоторые из них показаны ниже.

### **Использование диапазона отображения**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Использование MaxDataRow и MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Как видите, оба вышеупомянутых подхода используют более или менее похожую логику: цикл по всем ячейкам в коллекции для чтения значений ячеек. Это может вызвать проблемы по ряду причин, о которых рассказано ниже.

1. API такие как [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) и [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) требуют дополнительного времени для сбора соответствующей статистики. Если размер матрицы данных (строки x столбцы) велик, использование этих API может сказаться на производительности.
1. В большинстве случаев не все ячейки в заданном диапазоне созданы. В таких ситуациях проверка каждой ячейки в матрице не так эффективна, как проверка только инициализированных ячеек.
1. Доступ к ячейке в цикле в виде Cells row, column заставит создавать все объекты ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.

## **Заключение**

Исходя из вышеуказанных фактов, возможны следующие сценарии использования перечислителей.

1. Требуется только чтение коллекции ячеек, то есть только проверка ячеек.
1. Необходимо пройти большое количество ячеек.
1. Требуется пройти только инициализированные ячейки/строки/столбцы.
