---
title: Как и где использовать перечислители с C++
linktitle: Итерация данных
type: docs
weight: 55
url: /ru/cpp/how-and-where-to-use-enumerators/
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

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Все вышеперечисленные методы возвращают перечислитель, который позволяет осуществлять обход коллекции ячеек, которые были инициализированы.

{{% alert color="primary" %}}

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию новой ячейки или удалению существующей). В противном случае перечислитель может не иметь возможности правильно обойти все ячейки (некоторые элементы могут быть обойдены повторно или пропущены).

{{% /alert %}}

Приведенный ниже пример кода демонстрирует реализацию интерфейса IEnumerator для коллекции Cells.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Перечислитель строк**

Перебор строк можно осуществлять, используя метод [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/). Следующий пример демонстрирует реализацию интерфейса IEnumerator для [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Доступ к столбцам (Get)**

Доступ к столбцам осуществляется при использовании метода [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/). Следующий пример демонстрирует реализацию метода Get для [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Где использовать перечислители**

Чтобы обсудить преимущества использования перечислителей, давайте рассмотрим реальный пример.

**Сценарий**

Требование приложения — пройтись по всем ячейкам в заданном [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), чтобы прочитать их значения. Для достижения этой цели существует несколько способов. Некоторые из них показаны ниже.

### **Использование диапазона отображения**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **Использование MaxDataRow и MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Как видите, оба вышеупомянутых подхода используют более или менее похожую логику: цикл по всем ячейкам в коллекции для чтения значений ячеек. Это может вызвать проблемы по ряду причин, о которых рассказано ниже.

1. API такие как [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) и [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) требуют дополнительного времени для сбора соответствующей статистики. Если размер матрицы данных (строки x столбцы) велик, использование этих API может сказаться на производительности.
1. В большинстве случаев не все ячейки в заданном диапазоне созданы. В таких ситуациях проверка каждой ячейки в матрице не так эффективна, как проверка только инициализированных ячеек.
1. Доступ к ячейке в цикле в виде Cells row, column заставит создавать все объекты ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.

## **Заключение**

Исходя из вышеуказанных фактов, возможны следующие сценарии использования перечислителей.

1. Требуется только чтение коллекции ячеек, то есть только проверка ячеек.
1. Необходимо пройти большое количество ячеек.
1. Требуется пройти только инициализированные ячейки/строки/столбцы.
