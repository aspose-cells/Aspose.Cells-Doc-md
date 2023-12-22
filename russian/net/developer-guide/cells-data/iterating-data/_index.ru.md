---
title: Как и где использовать перечислители
linktitle: Итерация данных
type: docs
weight: 55
url: /ru/net/how-and-where-to-use-enumerators/
description: Узнайте, как и где использовать перечислители, по номеру Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

Перечислитель — это объект, который предоставляет возможность перемещаться по контейнеру или коллекции. Перечислители можно использовать для чтения данных в коллекции, но их нельзя использовать для изменения базовой коллекции, тогда как IEnumerable — это интерфейс, который определяет один метод GetEnumerator, который возвращает интерфейс IEnumerator, что, в свою очередь, обеспечивает доступ только для чтения к Коллекция.

Aspose.Cells API предоставляют множество перечислителей, однако в этой статье в основном обсуждаются три типа, перечисленные ниже.

1. Cells Счетчик
1. Перечислитель строк
1. Перечислитель столбцов

{{% /alert %}}

##  **Как использовать перечислители**

###  **Cells Счетчик**

Существуют различные способы доступа к перечислителю Cells, и можно использовать любой из этих методов в зависимости от требований приложения. Ниже приведены методы, которые возвращают перечислитель ячеек.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Диапазон.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Все вышеупомянутые методы возвращают перечислитель, который позволяет перемещаться по коллекции инициализированных ячеек.

{{% alert color="primary" %}}

При перемещении по ячейкам коллекцию не следует изменять (операции, которые приведут к созданию нового экземпляра Cell или удалению существующего Cell). В противном случае перечислитель не сможет правильно пройти все ячейки (некоторые элементы могут проходиться повторно или пропускаться).

{{% /alert %}}

В следующем примере кода демонстрируется реализация интерфейса IEnumerator для коллекции Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Перечислитель строк**

 Доступ к перечислителю строк можно получить при использовании[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) метод. В следующем примере кода демонстрируется реализация интерфейса IEnumerator для[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Перечислитель столбцов**

 Доступ к счетчику столбцов можно получить при использовании[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) метод. В следующем примере кода демонстрируется реализация интерфейса IEnumerator для[**СтолбецКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Где использовать перечислители**

Чтобы обсудить преимущества использования перечислителей, давайте рассмотрим пример в реальном времени.

**Сценарий**

 Требование приложения — пройти все ячейки в заданном[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)прочитать их значения. Способов реализации этой цели может быть несколько. Некоторые из них продемонстрированы ниже.

###  **Использование диапазона отображения**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **Использование MaxDataRow и MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Как вы можете заметить, оба вышеупомянутых подхода используют более или менее схожую логику, то есть; пройдите по всем ячейкам коллекции, чтобы прочитать значения ячеек. Это может быть проблематично по ряду причин, которые обсуждаются ниже.

1.  API, такие как[**МаксРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**Максдатаров**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**МаксКолонн**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**Максдатаколонн**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**Макс.диапазон отображения**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)требуется дополнительное время для сбора соответствующей статистики. Если матрица данных (строки x столбцы) велика, использование этих API может привести к снижению производительности.
1. В большинстве случаев не все ячейки в заданном диапазоне создаются. В таких ситуациях проверять каждую ячейку матрицы не так эффективно, как проверять только инициализированные ячейки.
1. Доступ к ячейке в цикле как строке Cells, столбцу приведет к созданию экземпляров всех объектов ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.

##  **Заключение**

Основываясь на вышеупомянутых фактах, ниже приведены возможные сценарии использования счетчиков.

1. Требуется доступ только для чтения к коллекции ячеек, т.е. требование состоит в том, чтобы проверять только клетки.
1. Необходимо пройти большое количество ячеек.
1. Для перемещения подлежат только инициализированные ячейки/строки/столбцы.
