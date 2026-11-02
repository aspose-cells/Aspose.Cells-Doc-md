---
title: Отображение значений как в сводной таблице
linktitle: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы с базовым элементом, накопительных итогов, рангов и др. с помощью Aspose.Cells for Java.
keywords: Aspose.Cells, сводная таблица, отображать значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /ru/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегирования, такой как `Sum` или `Count`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этого агрегата — например, процент от общего итога, накопительный итог, разницу с выбранным базовым элементом или ранг — позволяя выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов. Типичные применения включают анализ доли от общего итога, включая проценты строки, столбца или общего итога; накопительную отчетность с использованием накопительного итога в поле периода; анализ отклонений от эталонного элемента с помощью разницы или процентной разницы от базового элемента; а также ранжирование значений от наименьшего к наибольшему или от наибольшего к наименьшему. В Aspose.Cells for Java `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Только для чтения геттер `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, чьи методы `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` и `setBaseItemIndex(...)` настраивают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.getDataFields()`.

## **Члены перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою функцию агрегирования, такую как Sum или Count, тогда как Show Values As изменяет только способ отображения агрегированного значения.
Помимо прямого использования сеттеров `PivotShowValuesSetting` (см. последний раздел), удобный метод с одним вызовом применяет ту же конфигурацию:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Параметр | Значение | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичное вычисление `PivotFieldDataDisplayFormat`, которое необходимо применить. | Всегда. |
| `baseField` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс поля строки, к которому принадлежит базовый элемент). | Только шесть базовых форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.PREVIOUS`, `NEXT` или `CUSTOM`. | Только три формата базового элемента (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); игнорируется всеми остальными форматами. |
| `baseItem` | Нулевой индекс базового элемента. | Только когда `baseItemPositionType` равен `CUSTOM` (индекс элемента указывает точный базовый элемент); игнорируется для `PREVIOUS`/`NEXT` и всеми форматами без базового элемента — передайте `0`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Нет вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу с значением базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от итога строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от итога столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общего итога. | — |
| `INDEX` | Отображает значение с использованием формулы индекса Excel ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от итога родительской строки (для вложенных полей строк). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от итога родительского столбца (для вложенных полей столбцов). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от итога родительского элемента. | `baseField` (базовое родительское поле) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` задает значения `PivotShowValuesSetting` через `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` и `setBaseItemIndex(...)` — метод и объект свойства являются двумя способами настройки одного и того же состояния, отражая выбор базового поля и базового элемента в диалоговом окне Show Values As в Excel.
{{% /alert %}}

## **Отображать значения как процент от общего итога**
Вызовите метод `PivotField.showValuesAs(...)` с параметром `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой пропорцию полного набора результатов. Этот формат измеряет каждое значение только относительно общего итога, поэтому не требует базового поля или базового элемента — завершающие аргументы (`0`, `PivotItemPositionType.PREVIOUS`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров выше.

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
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получить и настроить PivotField.getShowValuesSetting**
Прочитайте текущую конфигурацию через `PivotField.getShowValuesSetting()`: геттер только для чтения возвращает объект `PivotShowValuesSetting` для поля, чьи четыре свойства описывают активное вычисление Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs(...)` — он записывает все четыре настройки одним вызовом, поэтому нет необходимости задавать свойства по отдельности.
Объект `PivotShowValuesSetting` раскрывает четыре свойства, которые записывает `showValuesAs(...)`:
- `getCalculationType()` / `setCalculationType(...)` выбирает вторичное вычисление `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` указывает нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` определяет, как базовый элемент позиционируется относительно текущего элемента, и принимает `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` или `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` задает нулевой индекс базового элемента и используется, когда `BaseItemPositionType` равно `CUSTOM`.
После вызова `showValuesAs(...)` снова вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы пересчиталось и было отрисовано с обновлённой конфигурацией.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}