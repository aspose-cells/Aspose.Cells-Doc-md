---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
linktitle: Добавить поля фильтров
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for C++, включая добавление полей фильтра, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
keywords: Aspose.Cells, C++, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через удобный API высокого уровня или через коллекцию нижнего уровня `PageFields`, управлять фильтром страницы в режиме одиночного выбора, сбрасывать его для отображения каждого элемента страницы, либо переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс с флажками в Excel.
{{% /alert %}}

## **Введение**

поле фильтра — это поле сводной таблицы, которое управляет тем, *какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображаемой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы так, чтобы были подытожены только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

поле фильтра может работать в двух режимах. В режиме по умолчанию — **одиночный выбор** — одновременно виден только один элемент страницы, поэтому тело сводной таблицы подытоживает ровно одно подмножество. В режиме **множественного выбора** поле отображает список флажков, и тело сводной таблицы подытоживает объединение каждого отмеченного элемента страницы. Одно и то же исходное поле можно переключать между этими режимами, изменяя значение одного свойства.

Aspose.Cells for C++ предоставляет два эквивалентных способа регистрации поля фильтраы. API высокого уровня — это `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. API низкого уровня — это `PivotTable.PageFields.Add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `PageFields`, а остальная часть этой статьи демонстрирует, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Вызов высокого уровня принимает имя исходного столбца в виде строки и является наиболее распространённым путём. Вызов низкого уровня принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля необходимо использовать повторно в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.PageFields`, после чего оно отображается как раскрывающийся список страницы в верхней части отображаемой сводной таблицы.

### Добавление поля фильтраы с помощью AddFieldToArea

В следующем примере создаётся небольшой набор данных Fruit / Year / Amount, сводная таблица размещается в ячейке E3 с `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, сводная таблица обновляется, и рабочая книга сохраняется.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // Создание новой книги
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // Настройка строки заголовка
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Заполнение 9 строк примерами данных: Фрукт, Год, Количество
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // Добавление сводной таблицы с привязкой к ячейке E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Добавление полей в области: Фрукт как Строка, Количество как Данные, Год как Поле страницы
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // Обновление и вычисление данных сводной таблицы
    pivotTable.CalculateData();

    // Сохранение книги
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Добавление поля фильтраы с помощью PageFields.Add

Когда вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `PivotTable.PageFields.Add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только последняя регистрация в области страницы заменяется вызовом API низкого уровня.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Заголовки
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Пример данных (9 строк)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // Добавить сводную таблицу в E3, охватывающую A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Fruit -> Строка, Amount -> Данные
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Подход низкого уровня: найти существующий PivotField Year в BaseFields
    // и зарегистрировать его в области страницы через PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Обновить, чтобы новое поле страницы отразилось в сохранённой книге
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле фильтра отображается как одиночный раскрывающийся список, а целочисленное значение `PivotField.CurrentPageItem` определяет, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает этот один элемент; присвоение специального значения-маркера `0x7FFD` (десятичное 32765) сбрасывает фильтр, чтобы все элементы страницы были подытожены одновременно. Одиночный выбор используется по умолчанию; вам не нужно включать его явным образом.

### Отображение всех элементов

Установка `CurrentPageItem` на магическое значение `0x7FFD` эквивалентна сбросу фильтра страницы: тело сводной таблицы подытоживает каждый элемент страницы так, как если бы фильтр не применялся.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Отображение одного конкретного элемента

Установка `CurrentPageItem` на реальный индекс выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает раскрывающийся список страницы в список флажков и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. `PivotField.IsMultipleItemSelectionAllowed` должно быть установлено в `true`, чтобы интерфейс множественного выбора вообще начал действовать. После его включения `PivotItem.IsHidden` управляет тем, какие элементы отображаются в списке флажков, поэтому вы можете либо показать все элементы, либо разрешить только определённые элементы.

Приведённый ниже код включает множественный выбор для того же поля фильтраы Year, созданного в Сценарии 1a, а затем демонстрирует два шаблона: Часть A показывает каждый элемент страницы, оставляя `IsHidden` равным `false` для каждой записи, тогда как Часть B разрешает только выбранные вами исходные значения и скрывает все остальные через блок `switch (pivotItems[i].GetStringValue())`.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Пример данных: Фрукт | Год | Количество
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — Включить множественный выбор для поля страницы
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // Часть A — выбрать ВСЕ элементы (сделать все элементы видимыми)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // Часть B — выбрать только определённые элементы по исходному значению
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.IsHidden` **хотя бы один `PivotItem` должен оставаться видимым** (`IsHidden == false`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш список разрешённых элементов множественного выбора включает хотя бы один элемент из исходных данных.

## **Какой API и какой режим следует использовать?**

Таблица ниже обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая подробно каждый сценарий.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавить поле фильтра по имени исходного столбца (наиболее распространённый вариант) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | н/п | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавить поле фильтра, когда у вас уже есть объект `PivotField` | `PivotTable.PageFields.Add(PivotField)` | н/п | Используйте, когда объект поля был получен в другом месте или должен быть использован повторно. |
| Фильтрация по одному элементу страницы (режим по умолчанию) | `PivotField.CurrentPageItem` | установить на конкретный индекс | Например, `1` отображает второй элемент в отсортированном списке. |
| Показать все элементы / сбросить фильтр страницы | `PivotField.CurrentPageItem` | установить на `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) является маркером для «все элементы». |
| Включить интерфейс множественного выбора в Excel | `PivotField.IsMultipleItemSelectionAllowed` | установить в `true` | Требуется до того, как какие-либо вызовы `IsHidden` вступят в силу. |
| Скрыть / показать отдельные элементы в списке множественного выбора | `PivotItem.IsHidden` | установить для каждого элемента | Хотя бы один элемент должен оставаться видимым (`IsHidden == false`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если каждый `PivotItem` в поле фильтра с множественным выбором скрыт, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Составляйте список разрешённых элементов на основе исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые рабочие книги будут надёжно открываться на любом компьютере.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
