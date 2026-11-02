---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы, входящие в верхний или нижний рейтинг поля сводной таблицы, в Aspose.Cells for C++. В этой статье рассматриваются метод Top10AutoShow для Excel 97–2003, чтение параметров с помощью GetTop10AutoShowSettings и фильтр «Топ-10» для Excel 2007–365 с помощью FilterTop10.
keywords: Aspose.Cells, C++, сводная таблица, топ-10, автопоказ, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ru/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строки, может быть трудна для чтения, если поле содержит десятки элементов. Отчет «Топ-10» оставляет только элементы, входящие в верхнюю или нижнюю часть рейтинга, что и требуется для отчетов с ранжированием: «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Excel 97–2003, автопоказ** — метод `PivotField.Top10AutoShow()`. Это классическая настройка «Показать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она поддерживается всеми версиями Excel, поскольку является частью исходного формата сводной таблицы.
- **Фильтр топ-10 для Excel 2007–365** — метод `PivotField.FilterTop10()`. Это современный фильтр значений «Топ-10», доступный в разделе «Фильтры по значениям» меню поля. Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование по количеству элементов и в процентах.

## **Отображение топ-10 в Excel 97–2003 (Top10AutoShow)**
Классический автопоказ настраивается одним вызовом `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)`:
- `isAutoShow` — включает или отключает автопоказ в поле.
- `isTop` — `true` оставляет элементы с наивысшим рейтингом (верхние), а `false` — с наименьшим (нижние).
- `count` — количество элементов, которые следует оставить, например 10 для классического отчета «Топ-10».
- `rankBy` — нулевой индекс поля **данных**, значения которого используются для ранжирования элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже показаны два варианта.

### **Ранжирование по полю значений**
Элементы поля строки можно ранжировать по обычному полю значений, например по полю «Сумма продаж». В следующем примере создается сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объемом продаж. Значение `rankBy` равно 0, поскольку «Сумма продаж» — поле данных с индексом 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Показать 2 верхних элемента, отсортированных по «Сумма продаж» (индекс поля данных 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ранжирование по самому полю**
Поле также можно ранжировать по самому себе — передайте -1 в качестве `rankBy`. Для этого варианта не требуется дополнительное поле данных; достаточно разместить поле в области строк или столбцов. В следующем примере показаны 3 вида спорта, находящихся в нижней части рейтинга по самому полю. При сохранении этой настройки атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `GetTop10AutoShowSettings().GetRankBy()` возвращает -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Чтение текущих параметров (GetTop10AutoShowSettings)**
Метод `PivotField.GetTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, который предоставляет текущие параметры автопоказа, сохраненные в поле. Используйте его, чтобы проверить, как будут представлены элементы в существующей рабочей книге или только что настроенной сводной таблице, в том числе в рабочих книгах, загруженных из файла.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Четыре члена класса соответствуют классическим атрибутам автопоказа, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому значения, считанные этим объектом, будут одинаково учитываться всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые свойства `PivotField` — `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` и `GetAutoShowField` — устарели. Вместо них используйте объект `PivotFieldTop10AutoShowSettings`: вместо `IsAutoShow` используйте `GetTop10AutoShowSettings().IsAutoShow()`, вместо `IsAscendShow` — `GetTop10AutoShowSettings().IsTop()`, вместо `GetAutoShowCount` — `GetTop10AutoShowSettings().GetAutoShowCount()`, а вместо `GetAutoShowField` — `GetTop10AutoShowSettings().GetRankBy()`. Для изменения параметров используйте сам метод `Top10AutoShow()`.
- `Top10AutoShow` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не выводятся в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007–365: фильтр топ-10 (FilterTop10)**
Современные версии Excel предоставляют фильтр «Топ-10» в меню поля (раздел «Фильтры по значениям», пункт «Топ-10…»). В Aspose.Cells этот фильтр реализован методом `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — нулевой индекс поля данных, агрегированные значения которого используются для ранжирования элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType::Count` оставляет фиксированное количество элементов (параметр «Элементы» в диалоговом окне). `PivotFilterType::Percent` сохраняет заданный процент элементов, поэтому `itemCount` задает сам процент: значение 30 сохраняет верхние 30 % элементов. `PivotFilterType::Sum` ранжирует элементы по накопленной сумме их значений.
- `isTop` — `true` для верхних элементов, `false` для нижних.
- `itemCount` — число N в выражении «Верхние N» или «Нижние N»; его единица измерения зависит от `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Фильтр «Топ-10» — сохранить 2 лучших элемента по «Сумме продаж» (индекс поля данных 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // Вместо этого для фильтра на основе процентов сохранить 30% лучших элементов:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` и `FilterTop10` представляют собой две отдельные функции. Автопоказ записывает классический набор атрибутов `autoShow` в поле сводной таблицы; этот набор учитывается всеми версиями Excel, начиная с Excel 97. `FilterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица, использующая современный фильтр, отображает все элементы. Для документов, которые должны сохраняться и повторно открываться в устаревших инструментах, предпочтительнее использовать `Top10AutoShow`; для современных рабочих книг предпочтительнее использовать `FilterTop10`, поскольку его можно применять совместно с другими фильтрами по значениям.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/cpp/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строки и столбца в сводную таблицу](/cells/ru/cpp/pivot-table-add-row-and-column-fields/)
- [Группировка полей в сводной таблице](/cells/ru/cpp/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}