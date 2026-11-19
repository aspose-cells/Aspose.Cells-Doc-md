---
title: Показать значения как в сводной таблице с помощью Aspose.Cells for C++
linktitle: Показать значения как в сводной таблице с помощью Aspose.Cells for C++
description: Отображение значений полей данных сводной таблицы в виде процентов от итога, разности относительно базового элемента, нарастающих итогов, рангов и других значений с помощью Aspose.Cells for C++.
keywords: Aspose.Cells, C++, сводная таблица, показать значения как, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ru/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегатной функции, например `Sum` или `Count`. Функция Excel **«Показать значения как»** заменяет каждое отображаемое значение результатом вторичного вычисления, основанного на этом агрегате, например процентом от общего итога, нарастающим итогом, разностью относительно выбранного базового элемента или рангом. Это позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.
Типичные варианты применения включают анализ долей, в том числе процентов от итога строки, столбца или общего итога; подготовку отчетности с нарастающим итогом по полю периода; анализ отклонений относительно эталонного элемента с помощью разности или процентного отличия от базового элемента; а также ранжирование значений от меньшего к большему или от большего к меньшему.
В Aspose.Cells for C++ перечисление `PivotShowValuesAsType` выбирает тип вторичного вычисления. Метод `PivotField.GetShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, методы `SetShowValuesAs`, `SetBaseFieldIndex` и `SetBaseItemIndex` которого настраивают поведение; удобный метод `PivotField.ShowValuesAs(...)` применяет те же параметры одним вызовом. Примените эти параметры к полю данных или значений, полученному из `PivotTable.GetDataFields()`.

## **Члены перечисления PivotShowValuesAsType**
Поле данных сохраняет агрегатную функцию, например `Sum` или `Count`, а функция «Показать значения как» изменяет только способ отображения агрегированного значения.
Помимо непосредственного задания значений `PivotShowValuesSetting` (см. последний раздел), ту же конфигурацию можно применить с помощью удобного метода, выполняющего настройку одним вызовом. Метод существует в двух вариантах: в одном базовое поле и базовый элемент задаются по индексам, в другом — по именам:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Параметр | Назначение | Когда требуется |
| --- | --- | --- |
| `showValuesAsType` | Тип применяемого вторичного вычисления `PivotShowValuesAsType`. | Всегда. |
| `baseField` | Индекс базового поля (с нуля) среди базовых полей сводной таблицы (например, индекс поля строки, к которому относится базовый элемент) или имя базового поля в варианте с именами. | Требуется для восьми форматов, зависящих от базового поля (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); для всех остальных форматов передайте `0` (или пустую `U16String` в варианте с именами). |
| `baseItem` | Индекс базового элемента (с нуля). Предусмотрены два специальных значения-маркера: -1 выбирает предыдущий элемент, а -2 — следующий (C++ API не определяет именованных констант для этих значений — передайте литералы). В варианте с именами вместо индекса передается подпись базового элемента, а для форматов, не требующих базового элемента, — пустая `U16String`. | Используется только тремя форматами, зависящими от базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); пять форматов, зависящих от поля (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, оба ранга), его игнорируют — передайте `0` или пустую `U16String`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Дополнительное вычисление не выполняется; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает разность между значением и значением базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо значение-маркер предыдущего или следующего элемента) |
| `PercentageOf` | Отображает значение в процентах от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо значение-маркер предыдущего или следующего элемента) |
| `PercentageDifferenceFrom` | Отображает процентное отличие от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо значение-маркер предыдущего или следующего элемента) |
| `RunningTotalIn` | Отображает нарастающий итог для последовательных элементов базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PercentageOfRow` | Отображает значение в процентах от итога строки. | — |
| `PercentageOfColumn` | Отображает значение в процентах от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение в процентах от общего итога. | — |
| `Index` | Отображает значение по формуле индекса Excel ((значение * общий итог) / (итог строки * итог столбца)). | — |
| `PercentageOfParentRowTotal` | Отображает значение в процентах от итога родительской строки (для вложенных полей строк). | — |
| `PercentageOfParentColumnTotal` | Отображает значение в процентах от итога родительского столбца (для вложенных полей столбцов). | — |
| `PercentageOfParentTotal` | Отображает значение в процентах от итога родительского элемента. | `baseField` (родительское поле, итог которого служит базой) |
| `PercentageOfRunningTotalIn` | Отображает значение в процентах от нарастающего итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Присваивает значение ранг от наименьшего (1) к наибольшему. | `baseField` (поле, элементы которого определяют область ранжирования) |
| `RankLargestToSmallest` | Присваивает значение ранг от наибольшего (1) к наименьшему. | `baseField` (поле, элементы которого определяют область ранжирования) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` устанавливает значения `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex` и `BaseItemIndex`). Метод и объект параметров представляют два способа настройки одного и того же состояния, аналогичных полям выбора базового поля и базового элемента в диалоговом окне Excel «Показать значения как».
{{% /alert %}}

## **Отображение значений в процентах от общего итога**
Вызовите метод `PivotField.ShowValuesAs` с `PivotShowValuesAsType::PercentageOfTotal`, чтобы представить каждую ячейку поля данных, включая ячейку общего итога, в виде доли от общего итога. Таким образом, отображаемые числа показывают долю каждого значения в общем результате. Этот формат сравнивает каждое значение только с общим итогом, поэтому базовое поле и базовый элемент не требуются. Последние аргументы (`0`, `0`) являются значениями-заполнителями, которые игнорируются этим форматом, как указано в таблице параметров выше.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Получение и настройка PivotField.ShowValuesSetting**
Получите текущую конфигурацию с помощью `PivotField.GetShowValuesSetting()`: этот метод возвращает объект `PivotShowValuesSetting` поля, а его методы получения позволяют определить активное вычисление функции «Показать значения как». Чтобы изменить конфигурацию, вызовите метод `PivotField.ShowValuesAs`: он задает все параметры одним вызовом, поэтому их не требуется устанавливать по одному.
Объект `PivotShowValuesSetting` хранит параметры, задаваемые методом `ShowValuesAs`:
- `GetShowValuesAs()` / `SetShowValuesAs()` выбирают тип вторичного вычисления `PivotShowValuesAsType`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` задают индекс базового поля (с нуля) среди полей сводной таблицы. Этот индекс используется в форматах, зависящих от базового поля.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` задают базовый элемент: индекс конкретного элемента сводной таблицы (с нуля) или одно из двух специальных значений-маркеров — -1 для предыдущего элемента и -2 для следующего (C++ API не определяет именованных констант для этих значений). Этот параметр используется в форматах, зависящих от базового элемента.
- `GetBaseFieldName()` и `GetBaseItemCaption()` — методы только для чтения, которые возвращают вычисленное имя базового поля и подпись базового элемента соответственно. Например, после выбора значения-маркера для предыдущего элемента `GetBaseItemCaption()` возвращает `(previous)`.
После вызова `ShowValuesAs` снова вызовите `PivotTable.CalculateData()`, чтобы пересчитать и заново отобразить тело сводной таблицы с обновленной конфигурацией.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}