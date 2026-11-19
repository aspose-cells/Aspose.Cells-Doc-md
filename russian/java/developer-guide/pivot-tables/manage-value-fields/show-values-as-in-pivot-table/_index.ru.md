---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображение значений полей данных сводной таблицы в процентах от общего итога, в виде разницы с базовым элементом, нарастающего итога, ранга и других производных значений с помощью Aspose.Cells for Java.
keywords: Aspose.Cells, сводная таблица, показать значения как, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /ru/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегатной функции, например `Sum` или `Count`. Функция Excel **«Показать значения как»** заменяет каждый отображаемый результат вторичным вычислением на основе агрегата — например, процентом от общего итога, нарастающим итогом, разницей с выбранным базовым элементом или рангом, что позволяет выполнять сравнительный анализ без вспомогательных формул и вычисляемых столбцов.
Типичные варианты применения включают анализ долей от общего итога, в том числе расчёт процентов от итога строки, столбца или общего итога; накопительную отчётность с использованием нарастающего итога в поле периода; анализ отклонений относительно элемента сравнения с помощью разницы от базового элемента или процентной разницы относительно него; а также ранжирование значений от наименьшего к наибольшему или от наибольшего к наименьшему.
В Aspose.Cells for Java перечисление `PivotShowValuesAsType` определяет вторичное вычисление. Доступный только для чтения геттер `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, методы `setShowValuesAs(...)`, `setBaseFieldIndex(...)` и `setBaseItemIndex(...)` которого задают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же настройки одним вызовом. Примените эти настройки к полю данных или полю значений, полученному из `PivotTable.getDataFields()`.

## **Члены перечисления PivotShowValuesAsType**
Поле данных сохраняет агрегатную функцию, например `Sum` или `Count`, тогда как режим «Показать значения как» изменяет только способ отображения агрегированного значения.
Помимо непосредственного использования методов установки значений `PivotShowValuesSetting` (см. последний раздел), ту же конфигурацию применяет удобный метод, выполняющий все действия одним вызовом. Предусмотрены две перегрузки: одна принимает базовое поле и базовый элемент по индексам, другая — по именам.

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Параметр | Назначение | Когда требуется |
| --- | --- | --- |
| `showValuesAsType` | Тип вторичного вычисления `PivotShowValuesAsType`, которое необходимо применить. | Всегда. |
| `baseField` | Индекс (с нуля) базового поля в списке базовых полей сводной таблицы (например, индекс поля строки, к которому относится базовый элемент) или — в перегрузке `String` — имя базового поля. | Для восьми форматов, относительных к базовому полю или элементу, перечисленных ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); для любого другого формата передайте `0` (или `null` в перегрузке `String`). |
| `baseItem` | Индекс (с нуля) базового элемента; предусмотрены два служебных значения: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) выбирает предыдущий элемент, а `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) — следующий. Перегрузка `String` принимает вместо этого подпись базового элемента; если выбранному формату базовый элемент не требуется, передавайте `null`. | Только три формата, связанных с базовым элементом (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`), используют базовый элемент; пять форматов, связанных с полем (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, оба ранга), игнорируют его — передайте `0` или `null`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Дополнительное вычисление не выполняется; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу со значением базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу со значением базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `RUNNING_TOTAL_IN` | Отображает значение как нарастающий итог по последовательным элементам базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от итога строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от итога столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общего итога. | — |
| `INDEX` | Отображает значение по формуле индекса Excel ((значение * общий итог) / (итог строки * итог столбца)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от итога родительской строки (для вложенных полей строк). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от итога родительского столбца (для вложенных полей столбцов). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от итога родительского поля. | `baseField` (родительское поле, итог которого служит базой) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от нарастающего итога в базовом поле. | `baseField` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) до наибольшего. | `baseField` (поле, элементы которого определяют область ранжирования) |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) до наименьшего. | `baseField` (поле, элементы которого определяют область ранжирования) |

{{% alert color="primary" %}}
`showValuesAs(...)` задаёт именно состояние `PivotShowValuesSetting` с помощью `setShowValuesAs(...)`, `setBaseFieldIndex(...)` и `setBaseItemIndex(...)` — метод и объект свойств являются двумя способами настроить одно и то же состояние, воспроизводящими выбор базового поля и базового элемента в диалоговом окне Excel «Показать значения как».
{{% /alert %}}

## **Отображение значений в процентах от общего итога**
Вызовите метод `PivotField.showValuesAs(...)` с `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая ячейку общего итога, в долю от общего итога. Таким образом, отображаемые числа показывают доли элементов полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому базовое поле и базовый элемент ему не нужны — завершающие аргументы (`0`, `0`) являются заполнителями, которые этот формат игнорирует, как указано в таблице параметров выше.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получение и настройка PivotField.getShowValuesSetting**
Получите текущую конфигурацию с помощью `PivotField.getShowValuesSetting()`: доступный только для чтения геттер возвращает объект `PivotShowValuesSetting` поля, свойства которого описывают активное вычисление «Показать значения как». Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs(...)` — он записывает все настройки одним вызовом, поэтому свойства не требуется задавать по одному.
Объект `PivotShowValuesSetting` предоставляет состояние, которое задаёт `showValuesAs(...)`:
- `getShowValuesAs()` / `setShowValuesAs(...)` выбирает тип вторичного вычисления — `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` задаёт индекс (с нуля) базового поля среди полей сводной таблицы. Это значение используется в форматах, связанных с базовым полем.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` задаёт базовый элемент: индекс (с нуля) конкретного элемента или одно из двух служебных значений — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) для предыдущего элемента и `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) для следующего. Это значение используется в форматах, связанных с базовым элементом.
- `getBaseFieldName()` и `getBaseItemCaption()` — доступные только для чтения методы, которые возвращают вычисленное имя базового поля и подпись базового элемента; например, после выбора служебного значения, соответствующего предыдущему элементу, `getBaseItemCaption()` возвращает `(previous)`.
После вызова `showValuesAs(...)` повторно вызовите `PivotTable.calculateData()`, чтобы пересчитать и перерисовать тело сводной таблицы с обновлённой конфигурацией.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}