---
title: Фильтрация сводных таблиц по метке или значению
linktitle: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for C++ поддерживает комплексные возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по метке, фильтров по дате, фильтров по значению, топ-10 фильтров, а также путём скрытия или отображения элементов сводной таблицы.
keywords: Aspose.Cells, библиотека C++, электронная таблица, сводная таблица, фильтр, фильтр по метке, фильтр по значению, фильтр по дате, топ-10 фильтр, элемент сводной таблицы, скрыть элемент сводной таблицы
type: docs
weight: 10
url: /ru/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. Вы можете применять фильтры по метке к текстовым полям строк или столбцов, использовать фильтры по дате, когда поле содержит только ячейки с датой и временем или пустые значения, применять фильтры по значению к агрегированным числам, использовать топ-10 фильтры для ранжирования по полю значений или вручную скрывать и отображать отдельные элементы сводной таблицы с помощью свойства `IsHidden`. Каждая стратегия предоставляется через специализированные API классов `PivotField` и `PivotItem`.
{{% /alert %}}
## **Введение**
Сводные таблицы являются мощным инструментом анализа, однако необработанные сводки часто содержат значительно больше информации, чем вам необходимо представить. Фильтрация является основным механизмом сужения сводной таблицы до строк, столбцов или значений, важных для конкретного отчёта. Aspose.Cells for C++ воспроизводит возможности фильтрации, доступные в Microsoft Excel, предоставляя их программно, чтобы генерация отчётов могла быть полностью автоматизирована.
В данной статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по метке** — фильтрует элементы полей строк или столбцов на основе их текстовых меток.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени (или пустые значения).
3. **Фильтр по значению** — фильтрует элементы на основе агрегированных значений поля данных.
4. **Топ-10 фильтр** — отображает только верхние или нижние N элементов, ранжированных по полю значений.
5. **Скрытие / отображение элементов сводной таблицы** — управление видимостью каждого отдельного элемента в поле.
Каждый подход использует различный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `RefreshData()` и `CalculateData()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.
## **Фильтр по метке**
Фильтр по метке позволяет фильтровать элементы поля строки или столбца путём сравнения их текстовых заголовков с шаблоном. Это полезно, когда вы хотите отобразить только продукты, имена которых начинаются с определённой буквы, содержат конкретное слово или соответствуют другому критерию, основанному на заголовке.
Aspose.Cells предоставляет фильтрацию по метке через метод `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. Перечисление `PivotFilterType` включает такие значения, как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задаёт строку метки, используемую для сравнения.
В следующем примере загружается рабочая книга, содержащая существующую сводную таблицу, применяется фильтр по метке так, чтобы только элементы, заголовки которых начинаются с указанного префикса, оставались видимыми, обновляется сводная таблица, и сохраняется результат.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Загрузка существующей книги, содержащей сводную таблицу
    Workbook wb(fileName);

    // Доступ к листу по индексу (первый лист)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Доступ к сводной таблице по индексу
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Получение первого строкового PivotField
    PivotField rowField = pt.GetRowFields().Get(0);

    // Применение фильтра меток — отображать только строки, метки которых начинаются с указанного префикса
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Обновление и пересчёт данных сводной таблицы, чтобы фильтр вступил в силу
    pt.RefreshData();

    // Сохранение книги на диск
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Фильтр по дате**
Фильтры по дате позволяют сузить сводную таблицу по критериям на основе дат, таким как сегодня, прошлая неделя, этот месяц, следующий квартал или определённый диапазон дат. Это специализированные фильтры, которые работают только с полями, содержащими информацию о дате и времени.
{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем или пустые значения. Если базовое поле содержит другие типы данных, такие как числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
{{% /alert %}}
Aspose.Cells предоставляет фильтрацию по дате через метод `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. Перечисление `PivotFilterType` содержит специализированные значения для дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра вы передаёте одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).
В следующем примере загружается рабочая книга со сводной таблицей, область строк которой содержит поле даты, применяется фильтр по дате, ограничивающий видимые элементы определённым диапазоном дат, обновляется сводная таблица, и сохраняется рабочая книга.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";

    if (!std::filesystem::exists(inputPath))
    {
        // Исходная рабочая книга не найдена.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Загрузить существующую рабочую книгу, содержащую сводную таблицу
    Workbook workbook(U16String(inputPath.c_str()));

    // Получить доступ к рабочему листу, содержащему сводную таблицу (по индексу)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Получить доступ к сводной таблице по индексу
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Получить поле даты PivotField из области строк
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Определить критерий даты для фильтра Между
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Применить фильтр даты к полю сводной таблицы
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Обновить и пересчитать сводную таблицу, чтобы фильтр вступил в силу
    pivotTable.RefreshData();

    // Сохранить рабочую книгу
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Фильтр по значению**
Фильтры по значению работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых меток они сравнивают числовые итоги с пороговым значением. Типичные варианты использования включают отображение только тех продуктов, сумма продаж которых превышает целевую сумму, или только тех регионов, количество транзакций в которых находится в определённом диапазоне.
Aspose.Cells предоставляет фильтрацию по значению через метод `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Параметр `filterType` использует такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `valueField` указывает, какое поле данных должно оцениваться, а последний аргумент (или аргументы) задаёт пороговое значение (или значения).
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, который оставляет только те элементы, агрегированные продажи которых превышают числовой порог, обновляется сводная таблица, и сохраняется рабочая книга.
```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);

    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }

    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Топ-10 фильтр**
Топ-10 фильтр представляет собой специализированную форму фильтра по значению, которая сохраняет только верхние или нижние N элементов на основе выбранного поля значений. Он часто используется в отчётах с ранжированием, таких как «топ-10 продуктов по выручке» или «5 худших регионов по количеству продаж».
{{% alert color="primary" %}}
Топ-10 фильтр эффективен только тогда, когда сводная таблица имеет одно или несколько полей значений в области данных. Без хотя бы одного поля значений не существует агрегированной меры для ранжирования элементов, и фильтр не может быть применён.
{{% /alert %}}
Aspose.Cells предоставляет топ-10 фильтрацию через метод `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Параметр `itemCount` определяет, сколько элементов нужно сохранить, `isTop` указывает, следует ли сохранить верхние элементы (true) или нижние элементы (false), `valueField` ссылается на поле данных, используемое для ранжирования, а `filterType` управляет способом вычисления значения (обычно `Sum`, а также `Count` и `Percent`).
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, применяется топ-10 фильтр для сохранения только 10 верхних элементов по сумме продаж, обновляется сводная таблица, и сохраняется рабочая книга.
```cpp
#include "Aspose.Cells.h"
#include <stdexcept>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }

    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);

    int valueFieldIndex = 0;

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Фильтрация путём скрытия или отображения элементов сводной таблицы**
В дополнение к структурированным API фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` объекта `PivotField` и переключая свойство `IsHidden`, можно выборочно подавлять определённые элементы без применения формульного фильтра. Установка `IsHidden = true` скрывает элемент из сводной таблицы; установка `IsHidden = false` отображает его снова, делая видимым.
Этот подход полезен, когда правило фильтрации является нерегулярным или специфичным для элемента, например, при скрытии небольшого числа именованных категорий, которые не должны отображаться в конкретном отчёте. В приведённом ниже примере загружается сводная таблица, скрывается определённый элемент по имени, демонстрируется его отображение, обновляется сводная таблица, и сохраняется рабочая книга.
```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Загрузить существующую книгу, содержащую сводную таблицу
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Получить доступ к первому листу, содержащему сводную таблицу
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Получить доступ к сводной таблице по индексу (первая сводная таблица на листе)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Получить целевое PivotField (первое поле метки строки, в котором мы будем скрывать/отображать элементы)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Перебрать коллекцию PivotItems выбранного PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Скрыть элементы сводной таблицы, соответствующие определённому имени/критерию
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Продемонстрировать отображение: повторно показать ранее скрытый элемент сводной таблицы
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Обновить и пересчитать сводную таблицу, чтобы изменения вступили в силу
    pivotTable.CalculateData();

    // Сохранить книгу — скрытые элементы остаются в исходных данных,
    // но исключаются из отображаемого вывода сводной таблицы
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Резюме**
Aspose.Cells for C++ предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующий возможностям Microsoft Excel. Фильтры по метке, дате и значению охватывают наиболее распространённые аналитические сценарии, тогда как топ-10 фильтр обрабатывает отчёты с ранжированием. Когда правило фильтрации является нерегулярным, свойство `PivotItem.IsHidden` предлагает гибкий резервный вариант на уровне элементов. Комбинирование этих стратегий — например, применение фильтра по метке с последующим скрытием определённых элементов — позволяет создавать точно нацеленные отчёты сводных таблиц полностью из кода.
{{< app/cells/assistant language="cpp" >}}