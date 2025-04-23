---
title: Как и где использовать перечислители
linktitle: Итерация данных
type: docs
weight: 55
url: /ru/net/how-and-where-to-use-enumerators/
description: Узнайте, как и где использовать перечислители через API Aspose.Cells for .NET.
keywords: Как использовать перечислители, перечислитель ячеек, перечислитель строк, перечислитель столбцов
---

{{% alert color="primary" %}}

Перечислитель - это объект, который предоставляет возможность обхода контейнера или коллекции. Перечислители могут использоваться для чтения данных в коллекции, но они не могут использоваться для изменения основной коллекции, в то время как IEnumerable - это интерфейс, который определяет один метод GetEnumerator, который возвращает интерфейс IEnumerator, который, в свою очередь, позволяет только для чтения доступ к коллекции.

API Aspose.Cells предоставляет множество перечислителей, однако в данной статье обсуждаются в основном три типа, перечисленные ниже.

1. Перечислитель ячеек
1. Перечислитель строк
1. Перечислитель столбцов

{{% /alert %}}

## **Как использовать перечислители**

### **Перечислитель ячеек**

Существуют различные способы доступа к перечислителю ячеек, и можно использовать любые из этих методов в зависимости от требований приложения. Вот методы, возвращающие перечислитель ячеек.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Все вышеперечисленные методы возвращают перечислитель, который позволяет осуществлять обход коллекции ячеек, которые были инициализированы.

{{% alert color="primary" %}}

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию новой ячейки или удалению существующей). В противном случае перечислитель может не иметь возможности правильно обойти все ячейки (некоторые элементы могут быть обойдены повторно или пропущены).

{{% /alert %}}

Приведенный ниже пример кода демонстрирует реализацию интерфейса IEnumerator для коллекции Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Перечислитель строк**

Перечислитель строк можно получить при использовании метода [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator). Приведенный ниже пример кода демонстрирует реализацию интерфейса IEnumerator для [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Перечислитель столбцов**

Перечислитель столбцов можно получить при использовании метода [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection). Приведенный ниже пример кода демонстрирует реализацию интерфейса IEnumerator для [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Где использовать перечислители**

Чтобы обсудить преимущества использования перечислителей, давайте рассмотрим реальный пример.

**Сценарий**

Требование приложения состоит в том, чтобы обойти все ячейки в заданном [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) для чтения их значений. Существует несколько способов реализации этой цели. Некоторые из них показаны ниже.

### **Использование диапазона отображения**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Использование MaxDataRow и MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Как видите, оба вышеупомянутых подхода используют более или менее похожую логику: цикл по всем ячейкам в коллекции для чтения значений ячеек. Это может вызвать проблемы по ряду причин, о которых рассказано ниже.

1. API, такие как [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) и [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange), требуют дополнительного времени для сбора соответствующей статистики. В случае большой матрицы данных (строки x столбцы) использование этих API может отрицательно сказаться на производительности.
1. В большинстве случаев не все ячейки в заданном диапазоне созданы. В таких ситуациях проверка каждой ячейки в матрице не так эффективна, как проверка только инициализированных ячеек.
1. Доступ к ячейке в цикле в виде Cells row, column заставит создавать все объекты ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.

## **Заключение**

Исходя из вышеуказанных фактов, возможны следующие сценарии использования перечислителей.

1. Требуется только чтение коллекции ячеек, то есть только проверка ячеек.
1. Необходимо пройти большое количество ячеек.
1. Требуется пройти только инициализированные ячейки/строки/столбцы.
{{< app/cells/assistant language="csharp" >}}
