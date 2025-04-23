---
title: Управление диапазонами с помощью C++
linktitle: Диапазоны
type: docs
weight: 105
url: /ru/cpp/managing-ranges/
description: Узнайте, как управлять диапазонами в Excel файлах с помощью Aspose.Cells и C++. Создавайте, модифицируйте и стилизуйте диапазоны программно.
---

## **Введение**

 В Excel можно выбрать несколько ячеек с помощью выделения мышью, набор выбранных ячеек называется "Диапазон".

Например, вы можете щелкнуть левой кнопкой мыши в ячейке "A1" в Excel, а затем перетащить в ячейку "C4". Прямоугольная область, которую вы выбрали, также легко создается в виде объекта с помощью Aspose.Cells.

 Вот как создать диапазон, установить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## **Управление диапазонами с использованием Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Поместить значение в ячейки диапазона**

Предположим, что у вас есть диапазон ячеек, который расширяется от A1 до C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установить стиль ячеек диапазона**

В следующем примере показано, как установить стиль ячеек диапазона.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Получить текущий регион диапазона**

CurrentRegion - это свойство, которое возвращает объект Range, представляющий текущий регион. 

Текущий регион - это диапазон, ограниченный любой комбинацией пустых строк и столбцов. Только для чтения.

В Excel вы можете получить область CurrentRegion следующим образом:
1. Выделите область (range1) с помощью мыши.
2. Нажмите "Домой - Правка - Поиск и выбор - Перейти к специальному - Текущий регион", или используйте "Ctrl+Shift+*", теперь вы увидите, что Excel автоматически помогает вам выбрать область (range2), теперь вы сделали это, range2 - это CurrentRegion range1.

Используя Aspose.Cells, вы можете использовать свойство "Range.CurrentRegion" для выполнения той же функции.

Пожалуйста, загрузите следующий тестовый файл, откройте его в Excel, используйте мышь, чтобы выбрать область "A1:D7", затем нажмите "Ctrl+Shift+*", вы увидите, что область "A1:C3" выбрана.

[current_region.xlsx](current_region.xlsx)

Теперь запустите следующий пример, посмотрите, как это работает в Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/cpp/autofill-ranges/)
- [Копирование диапазонов в Excel](/cells/ru/cpp/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/cpp/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/cpp/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/cpp/copy-range-style-only/)
- [Создать объединенный диапазон](/cells/ru/cpp/create-union-range/)
- [Вырезать и вставить диапазон](/cells/ru/cpp/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/cpp/delete-ranges-from-Excel/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Вставить диапазоны](/cells/ru/cpp/insert-ranges-to-Excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/cpp/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/cpp/move-range-of-cells-in-a-worksheet/)
- [Создать именованные диапазоны с учетом книги и листа](/cells/ru/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/cpp/search-and-replace-data-in-a-range/)
