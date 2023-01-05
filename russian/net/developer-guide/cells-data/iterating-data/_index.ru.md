---
title: Как и где использовать перечислители
linktitle: Повторить данные
type: docs
weight: 55
url: /ru/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

Перечислитель — это объект, предоставляющий возможность обхода контейнера или коллекции. Перечислители можно использовать для чтения данных в коллекции, но их нельзя использовать для изменения базовой коллекции, в то время как IEnumerable — это интерфейс, определяющий один метод GetEnumerator, который возвращает интерфейс IEnumerator, что, в свою очередь, разрешает доступ только для чтения к Коллекция.

Aspose.Cells API предоставляют множество счетчиков, однако в этой статье в основном обсуждаются три типа, перечисленные ниже.

1. Cells Счетчик
1. Перечислитель строк
1. Перечислитель столбцов

{{% /alert %}}

## **Как использовать перечислители**

### **Cells Счетчик**

Существуют различные способы доступа к перечислителю Cells, и любой из этих способов можно использовать в зависимости от требований приложения. Вот методы, которые возвращают перечислитель ячеек.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Все вышеперечисленные методы возвращают перечислитель, который позволяет обойти коллекцию ячеек, которые были инициализированы.

{{% alert color="primary" %}}

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию нового экземпляра Cell или удалению существующего Cell). В противном случае счетчик не сможет правильно пройти все ячейки (некоторые элементы могут быть пройдены повторно или пропущены).

{{% /alert %}}

В следующем примере кода демонстрируется реализация интерфейса IEnumerator для коллекции Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Перечислитель строк**

 Доступ к перечислителю строк можно получить при использовании[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) метод. В следующем примере кода демонстрируется реализация интерфейса IEnumerator для[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Перечислитель столбцов**

 Доступ к перечислителю столбцов можно получить при использовании[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) метод. В следующем примере кода демонстрируется реализация интерфейса IEnumerator для[**КолонкаКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Где использовать перечислители**

Чтобы обсудить преимущества использования счетчиков, давайте рассмотрим пример в реальном времени.

**Сценарий**

 Требование к приложению состоит в том, чтобы обойти все ячейки в заданном[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)читать их значения. Способов реализации этой цели может быть несколько. Некоторые из них показаны ниже.

### **Использование диапазона отображения**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Использование MaxDataRow и MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Как вы можете заметить, оба вышеупомянутых подхода используют более или менее схожую логику, то есть; цикл по всем ячейкам в коллекции, чтобы прочитать значения ячеек. Это может быть проблематично по ряду причин, как описано ниже.

1.  API, такие как[**МаксРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**Максдатаров**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**Максколумн**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**Максдатаколумн**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)требуется дополнительное время для сбора соответствующей статистики. Если матрица данных (строки x столбцы) велика, использование этих API может привести к снижению производительности.
1. В большинстве случаев создаются не все ячейки в заданном диапазоне. В таких ситуациях проверять каждую ячейку матрицы не так эффективно, как проверять только инициализированные ячейки.
1. Доступ к ячейке в цикле как строка Cells, столбец приведет к созданию экземпляров всех объектов ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.

## **Заключение**

Основываясь на вышеупомянутых фактах, ниже приведены возможные сценарии использования счетчиков.

1. Требуется доступ только для чтения к коллекции ячеек, т.е. требование состоит только в проверке ячеек.
1. Необходимо пройти большое количество клеток.
1. Только инициализированные ячейки/строки/столбцы должны быть пройдены.
