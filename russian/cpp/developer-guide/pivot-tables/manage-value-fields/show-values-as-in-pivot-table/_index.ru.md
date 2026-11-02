---
title: Отображение значений как в сводной таблице в Aspose.Cells for C++
linktitle: Отображение значений как в сводной таблице в Aspose.Cells for C++
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и т.д. с помощью Aspose.Cells for C++.
keywords: Aspose.Cells, C++, сводная таблица, отображение значений как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ru/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегирующей функции, такой как `Sum` или `Count`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегированной величины — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рангом — так что можно выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога, включая проценты по строке, столбцу или общему итогу; накопительный отчёт с использованием накопительного итога в поле периода; анализ отклонений относительно эталонного элемента с помощью разницы или процентной разницы от базового элемента; а также ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for C++ параметр `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Метод доступа `PivotField.GetShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, у которого методы `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` и `SetBaseItemIndex` задают поведение; удобный метод `PivotField.ShowValuesAs(...)` применяет те же четыре настройки одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.GetDataFields()`.

## **Элементы перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою агрегирующую функцию, такую как Sum или Count, в то время как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой записи значений `PivotShowValuesSetting` (см. последний раздел), удобный метод одним вызовом применяет ту же конфигурацию:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичный расчёт `PivotFieldDataDisplayFormat`, который необходимо применить. | Всегда. |
| `baseField` | Индекс (ноль‑базовый) базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType::Previous`, `::Next` или `::Custom`. | Только три формата базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); игнорируется всеми остальными форматами. |
| `baseItem` | Индекс (ноль‑базовый) базового элемента. | Только когда `baseItemPositionType` установлен в `Custom` (индекс указывает точный базовый элемент); игнорируется для `Previous`/`Next` и всеми форматами, не использующими базовый элемент — передайте `0`. |

| Тип расчета | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Нет вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу с значением базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу с базовым элементом в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `RunningTotalIn` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле индекса Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итоговой суммы родительской строки (для вложенных полей строк). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итоговой суммы родительского столбца (для вложенных полей столбцов). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от итоговой суммы родительского уровня. | `baseField` (базовое родительское поле) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Присваивает ранги от наименьшего (1) к наибольшему. | — |
| `RankLargestToSmallest` | Присваивает ранги от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` записывает значения `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — метод и объект настроек представляют два способа конфигурировать одно и то же состояние, аналогично выборам базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений как процент от общего итога**
Вызовите метод `PivotField.ShowValuesAs` с параметром `PivotFieldDataDisplayFormat::PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой части от полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому ему не требуется базовое поле или базовый элемент — конечные аргументы (`0`, `PivotItemPositionType::Previous`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров выше.

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
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Получение и настройка PivotField.ShowValuesSetting**
Считайте текущую конфигурацию через `PivotField.GetShowValuesSetting()`: метод доступа возвращает объект `PivotShowValuesSetting` поля, у которого четыре метода‑получения описывают активное вычисление **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.ShowValuesAs` — он записывает все четыре настройки одним вызовом, поэтому нет необходимости задавать их по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре значения, которые записывает `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` выбирают вторичный расчёт `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` указывают ноль‑базовый индекс базового поля среди полей сводной таблицы. Он используется базовыми форматами.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` определяют, как базовый элемент позиционируется относительно текущего, и принимают значения `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` или `PivotItemPositionType::Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` задают ноль‑базовый индекс базового элемента и используются, когда тип позиции установлен в `Custom`.  
После вызова `ShowValuesAs` повторно вызовите `PivotTable.CalculateData()`, чтобы тело сводной таблицы пересчиталось и отобразилось с обновлённой конфигурацией.

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
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
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