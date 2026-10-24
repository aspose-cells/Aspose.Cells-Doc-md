---
title: Добавление полей фильтрации в сводную таблицу с помощью Aspose.Cells for Java
linktitle: Добавление полей фильтрации в сводную таблицу с помощью Aspose.Cells for Java
description: Узнайте, как добавлять и настраивать поля фильтрации в сводных таблицах с помощью Aspose.Cells for Java, включая добавление полей фильтрации, фильтрацию с одиночным и множественным выбором.
keywords: Aspose.Cells, Java, сводная таблица, поле фильтрации, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает весь жизненный цикл работы с полями фильтрации в сводных таблицах. Поле фильтрации можно добавить с помощью удобного API высокого уровня или коллекции `PageFields` низкого уровня. Фильтр можно настроить на одиночный выбор, очистить, чтобы отобразить все элементы поля фильтрации, или переключить в режим множественного выбора, чтобы пользователи могли одновременно выбирать несколько элементов с помощью флажков в Excel.
{{% /alert %}}

## **Введение**
Поле фильтрации — это поле сводной таблицы, которое определяет, *какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его в виде раскрывающегося списка в верхней части сформированной сводной таблицы в Excel. При выборе одного из доступных элементов фильтра тело сводной таблицы перестраивается, и агрегируются только записи, относящиеся к выбранному элементу. Поле сводной таблицы становится полем фильтрации, если оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

## **Добавление поля фильтрации**

### Добавление поля фильтрации с помощью addFieldToArea
В следующем примере создается небольшой набор данных Fruit / Year / Amount. Сводная таблица размещается в ячейке E3, поле `Fruit` добавляется в область строк, `Amount` — в область данных, а `Year` — в область фильтрации. После этого сводная таблица обновляется, а рабочая книга сохраняется.

```java
import com.aspose.cells.*;
// Создать новую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Настроить строку заголовков
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Заполнить 9 строкsample data: Fruit, Year, Amount
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Добавить сводную таблицу с привязкой к ячейке E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Добавить поля в соответствующие области: Fruit как строка, Amount как данные, Year как поле страницы
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Обновить и вычислить данные сводной таблицы
pivotTable.calculateData();
// Сохранить книгу
workbook.save("pageFieldSample.xlsx");
```

### Добавление поля фильтрации с помощью PageFields.add
Если у вас уже есть экземпляр `PivotField`, его можно передать непосредственно в `PivotTable.PageFields.add`. Сводная таблица и поле фильтрации создаются точно так же, как в предыдущем сценарии; изменяется только регистрация поля в области фильтрации — вместо этого используется вызов API низкого уровня.

```java
import com.aspose.cells.*;
// - Сводная таблица и поле страницы создаются точно так же, как в
//   Сценарии 1a (данные Fruit/Year/Amount, сводная таблица в E3, Fruit->Row,
//   Amount->Data). Ниже мы получаем Year PivotField из коллекции
//   BaseFields и передаём его в PageFields.Add - низкоуровневую
//   альтернативу AddFieldToArea. Результат функционально
//   идентичен Сценарию 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Заголовки
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Пример данных (9 строк)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Добавление сводной таблицы в E3, охватывающей A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Row, Amount -> Data (Year будет помещено на Page ниже)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Низкоуровневый подход: получаем существующий Year PivotField из BaseFields
// и регистрируем его в области Page через PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Обновляем, чтобы новое поле страницы отразилось в сохранённой книге
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Фильтрация с одиночным выбором (отображение одного элемента фильтра)**
По умолчанию поле фильтрации отображается в виде одного раскрывающегося списка, а целочисленное значение `PivotField.CurrentPageItem` определяет, какой элемент фильтра применяется к телу сводной таблицы. При указании конкретного индекса выбирается соответствующий элемент. При указании специального служебного значения `0x7FFD` (32765 в десятичной системе) фильтр очищается, и агрегируются данные по всем элементам фильтра. Одиночный выбор включен по умолчанию, поэтому явно активировать его не требуется.

### Отображение всех элементов
Присваивание `CurrentPageItem` служебного значения `0x7FFD` эквивалентно очистке фильтра: тело сводной таблицы агрегирует данные по всем элементам поля фильтрации, как если бы фильтр не применялся.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Заполнить данные Fruit/Year/Amount
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Создать сводную таблицу в E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Настроить поля сводной таблицы: Fruit — строки, Amount — данные, Year — страница
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Очистить фильтр страницы, чтобы отображались все элементы поля страницы.
// 0x7FFD (десятичное 32765) — специальное значение-маркер, означающее «все элементы»,
// эквивалентное выбору «(Все)» в раскрывающемся списке поля страницы Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Отображение одного конкретного элемента
Присваивание `CurrentPageItem` конкретного индекса выбирает только соответствующий элемент фильтра. Индекс соответствует положению элемента в отсортированном списке элементов поля фильтрации, поэтому, например, `1` выбирает второй элемент после сортировки.

```java
import com.aspose.cells.*;
// Создать книгу
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Добавить пример данных (Фрукт/Год/Количество)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Добавить сводную таблицу в E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Добавить поля: Fruit→Строка, Amount→Данные, Year→Страница
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Операции с полями страницы
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = второй элемент в отсортированном порядке (например, "2021")
// Обновить и вычислить сводную таблицу
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Фильтрация с множественным выбором**
Фильтрация с множественным выбором превращает раскрывающийся список поля фильтрации в список с флажками и позволяет конечному пользователю одновременно выбирать несколько элементов фильтра. Aspose.Cells предоставляет два взаимосвязанных свойства. Свойство `PivotField.IsMultipleItemSelectionAllowed` должно иметь значение `true`, иначе интерфейс множественного выбора не активируется. После этого свойство `PivotItem.IsHidden` определяет, какие элементы отображаются в списке с флажками, поэтому можно отобразить все элементы или разрешить выбор только определенных элементов.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Пример данных: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Включить множественный выбор для поля страницы
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Часть A -- выбрать ВСЕ элементы (сделать видимыми все элементы)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Часть B -- выбрать только определенные элементы по исходному значению
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Примечание:** При настройке фильтрации с множественным выбором с помощью `PivotItem.IsHidden` **хотя бы один `PivotItem` должен оставаться видимым** (`IsHidden == false`). Если скрыты все элементы, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что список элементов, разрешенных для множественного выбора, содержит хотя бы один элемент исходных данных.

## **Какой API и какой режим следует использовать?**
В таблице ниже кратко показано, когда следует использовать каждый API и режим, чтобы выбрать подходящую комбинацию без необходимости подробно изучать каждый сценарий.
| Сценарий / вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавление поля фильтрации по имени столбца источника (самый распространенный случай) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | н/п | API высокого уровня, одна строка. Используйте его, если ссылка на `PivotField` не требуется. |
| Добавление поля фильтрации при наличии объекта `PivotField` | `PivotTable.PageFields.add(PivotField)` | н/п | Используйте его, если объект поля получен в другом месте или его необходимо повторно использовать. |
| Выбор одного элемента фильтра (режим по умолчанию) | `PivotField.CurrentPageItem` | устанавливается конкретный индекс | Например, `1` отображает второй элемент в отсортированном списке. |
| Отображение всех элементов / очистка фильтра | `PivotField.CurrentPageItem` | устанавливается `0x7FFD` | Специальное служебное значение `0x7FFD` (32765 в десятичной системе) обозначает «все элементы». |
| Включение интерфейса множественного выбора в Excel | `PivotField.IsMultipleItemSelectionAllowed` | устанавливается в `true` | Необходимо установить до вызовов `IsHidden`, чтобы они вступили в силу. |
| Скрытие и отображение отдельных элементов в списке множественного выбора | `PivotItem.IsHidden` | устанавливается для каждого элемента | Хотя бы один элемент должен оставаться видимым (`IsHidden == false`). |

{{% alert color="primary" %}}
Всегда учитывайте ограничение на видимость при настройке фильтрации с множественным выбором. Если скрыты все объекты `PivotItem` поля фильтрации с множественным выбором, Excel аварийно завершается при открытии файла или отображает пустую сводную таблицу. Формируйте список разрешенных элементов на основе исходных данных, оставляя хотя бы один элемент видимым. В таком случае сохраненные рабочие книги будут открываться без сбоев на любом компьютере.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}