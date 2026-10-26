---
title: Группировка полей сводной таблицы
linktitle: Группировка полей сводной таблицы
description: Узнайте, как группировать поля строк и столбцов сводной таблицы в периоды дат, такие как месяцы и кварталы, а также в числовые диапазоны, используя PivotField.Group и PivotFieldGroupOptions в Aspose.Cells for C++.
keywords: Aspose.Cells, сводная таблица, группировка полей сводной таблицы, PivotField.Group, PivotFieldGroupOptions, группировка по датам, группировка по числам, месяцы, кварталы, числовой диапазон, C++
type: docs
weight: 80
url: /ru/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит много различных значений, например поле дат с сотнями дат или числовое поле с большим количеством разрозненных значений. Группировка объединяет эти значения в осмысленные секции: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0–1, 2–3, 4–5. Это делает большую сводную таблицу компактной и более удобной для анализа. Aspose.Cells предоставляет эту возможность через метод `PivotField.Group()` (автоматическая группировка по типу данных) и `PivotField.Group(PivotFieldGroupOptions)` (пользовательские параметры группировки).
- Группировка по датам объединяет отдельные даты в более крупные периоды, такие как дни, месяцы, кварталы и годы, и формирует временную иерархию (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видны с первого взгляда, и каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов.
- Группировка доступна только для полей, размещённых в области СТРОК или СТОЛБЦОВ сводной таблицы. Поле данных (значений) нельзя сгруппировать напрямую. Чтобы сгруппировать такое поле, его необходимо сначала добавить в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка `PivotField.Group()` без параметров проверяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с использованием автоматического интервала.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет пользовательскую конфигурацию группировки. Для полей дат задайте `StartDate`, `EndDate` и `GroupTypes`. Для числовых полей задайте `StartNumber`, `EndNumber` и `Interval`. Свойство `NewPivotField` управляет тем, создаёт ли группировка новые поля сводной таблицы рядом с исходным (см. раздел «Примечание» в конце этой статьи).

### **Группировка поля даты по месяцам и кварталам**
Следующий пример группирует поле даты в строках образца сводной таблицы по месяцам и кварталам между начальной и конечной датами. Код загружает [образец файла Excel](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет сгруппированный результат. На снимке экрана показан эффект: поле даты в строках теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `options.GroupTypes` игнорируется. Независимо от того, в каком порядке перечислены типы групп, сгруппированные поля всегда отображаются от самого крупного периода к самому мелкому: годы, кварталы, месяцы, дни, часы, минуты, секунды. В этом примере месяцы перечислены в `options.GroupTypes` перед кварталами, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Загрузить образец рабочей книги
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Получить доступ ко второму листу и его сводной таблице
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Сгруппировать первое поле строки (поле даты) по месяцам и кварталам
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Установить типы групп: Месяцы и Кварталы
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Применить группировку к первому полю строки
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Вычислить данные сводной таблицы и сохранить выходной файл
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` в образце сводной таблицы изначально является полем данных (значений). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0–1, 2–3 и 4–5, используя `StartNumber = 0`, `EndNumber = 5` и `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.GroupBy()` устарели и удалены из API. Их заменой являются `PivotField.Group()` и `PivotField.Group(PivotFieldGroupOptions)`.
- В Microsoft Excel группировка числового поля ЗАМЕНЯЕТ исходное поле сводной таблицы сгруппированными диапазонами, тогда как группировка поля даты создаёт НОВЫЕ поля сводной таблицы (по одному на каждый уровень группировки, например Кварталы и Месяцы) рядом с исходным полем. Начиная с Aspose.Cells 26.10 методы `PivotField.Group()` следуют тому же поведению, что и Excel. Свойство `PivotFieldGroupOptions.NewPivotField` существует для совместимости со старыми версиями: по умолчанию оно равно false для числовой группировки и true для группировки по дате и времени; установите его в false, если хотите, чтобы группировка по датам заменяла исходное поле сводной таблицы вместо создания новых полей.
- Свойство `PivotFieldGroupOptions.Interval` действует только для числовой группировки и для группировки дат по дням (например, группировка дат в 7-дневные периоды); оно игнорируется при группировке дат по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/cpp/filter-by-label-or-value-of-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/cpp/add-page-field-in-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}