---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
linktitle: Добавить поля фильтров
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for Java, включая добавление полей фильтра, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
keywords: Aspose.Cells, Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /ru/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через высокоуровневый удобный API или через низкоуровневую коллекцию `PageFields`, и вы можете управлять фильтром страницы в режиме одиночного выбора, очищать его, чтобы показать все элементы страницы, или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс с флажками в Excel.
{{% /alert %}}

## **Введение**

поле фильтра — это поле сводной таблицы, которое управляет *тем, какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображаемой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы так, чтобы суммировались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

поле фильтра может работать в двух режимах. В режиме **одиночного выбора** по умолчанию одновременно виден только один элемент страницы, поэтому тело сводной таблицы суммирует ровно одно подмножество. В режиме **множественного выбора** поле отображает список с флажками, и тело сводной таблицы суммирует объединение каждого отмеченного элемента страницы. То же самое исходное поле можно переключать между этими режимами, изменяя одно свойство.

Aspose.Cells for Java предоставляет два эквивалентных способа регистрации поля фильтраы. Высокоуровневый API — это `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — это `PivotTable.PageFields.add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `PageFields`, и остальная часть этой статьи демонстрирует, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым способом. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля должен повторно использоваться в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.PageFields`, после чего оно появляется как раскрывающийся список страницы в верхней части отображаемой сводной таблицы.

### Добавление поля фильтраы с помощью addFieldToArea

Следующий пример создаёт небольшой набор данных Fruit / Year / Amount, размещает сводную таблицу в ячейке E3 с полем `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, обновляет сводную таблицу и сохраняет книгу.

```java
import com.aspose.cells.*;

// Создать новую рабочую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Настроить строку заголовка
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Заполнить 9 строк примерных данных: Фрукт, Год, Количество
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

// Добавить сводную таблицу, привязанную к ячейке E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Добавить поля в их области: Фрукт как строка, Количество как данные, Год как поле страницы
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// Обновить и вычислить данные сводной таблицы
pivotTable.calculateData();

// Сохранить рабочую книгу
workbook.save("pageFieldSample.xlsx");
```

### Добавление поля фильтраы с помощью PageFields.add

Когда вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `PivotTable.PageFields.add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только последняя регистрация в области страницы заменяется вызовом низкоуровневого API.

```java
import com.aspose.cells.*;

// - Сводная таблица и поле страницы создаются точно так же, как в
//   Сценарии 1a (данные Фрукт/Год/Сумма, сводная в E3, Фрукт->Строка,
//   Сумма->Данные). Ниже мы получаем PivotField "Год" из
//   коллекции BaseFields и передаём его в PageFields.Add -
//   низкоуровневую альтернативу AddFieldToArea. Результат
//   функционально идентичен Сценарию 1a.

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

// Добавить сводную таблицу в E3, охватывающую A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Фрукт -> Строка, Сумма -> Данные (Год будет добавлен на страницу ниже)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Низкоуровневый подход: берём существующий PivotField "Год" из BaseFields
// и регистрируем его в области страницы через PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Обновляем, чтобы новое поле страницы отразилось в сохранённой книге
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле фильтра отображается как один раскрывающийся список, и целочисленное значение `PivotField.CurrentPageItem` определяет, какой элемент страницы управляет телом сводной таблицы. Присвоение определённого индекса выбирает именно этот элемент; присвоение специального значения `0x7FFD` (десятичное 32765) сбрасывает фильтр, чтобы все элементы страницы были просуммированы одновременно. Одиночный выбор — это режим по умолчанию; его не нужно включать явно.

### Отображение всех элементов

Установка `CurrentPageItem` на магическое значение `0x7FFD` эквивалентна сбросу фильтра страницы: тело сводной таблицы суммирует все элементы страницы, как если бы фильтр не был применён.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// Заполнить данные Фрукт/Год/Количество
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

// Настроить поля сводной таблицы: Фрукт в строки, Количество в данные, Год в страницы
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.calculateData();

// Очистить фильтр страницы, чтобы каждый элемент поля страницы был виден.
// 0x7FFD (десятичное 32765) — это специальное значение-маркер, означающее "все элементы",
// эквивалентно выбору "(Все)" в раскрывающемся списке поля страницы в Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### Отображение одного конкретного элемента

Установка `CurrentPageItem` на реальный индекс выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```java
import com.aspose.cells.*;

// Создать книгу
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Добавить демонстрационные данные (Фрукт/Год/Количество)
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

// Операции, специфичные для поля страницы
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = второй элемент в отсортированном порядке (например, "2021")

// Обновить и вычислить сводную таблицу
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает раскрывающийся список страницы в список с флажками и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. `PivotField.IsMultipleItemSelectionAllowed` должно быть установлено в `true` до того, как интерфейс множественного выбора вступит в силу. После его включения `PivotItem.IsHidden` управляет тем, какие элементы отображаются в списке с флажками, поэтому вы можете либо показать все элементы, либо включить в белый список только определённые элементы.

Приведённый ниже код включает множественный выбор для того же поля фильтраы Year, созданного в сценарии 1a, а затем демонстрирует два шаблона: Часть A раскрывает все элементы страницы, оставляя `IsHidden` установленным в `false` для каждой записи, тогда как Часть B включает в белый список только выбранные вами исходные значения и скрывает всё остальное через блок `switch (pivotItems[i].getStringValue())`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Пример данных: Фрукт | Год | Количество
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

// Часть A -- выбрать ВСЕ элементы (сделать все элементы видимыми)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}

// Часть B -- выбрать только определённые элементы по исходному значению
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

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.IsHidden` **как минимум один `PivotItem` должен оставаться видимым** (`IsHidden == false`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список для множественного выбора включает хотя бы один элемент из ваших исходных данных.

## **Какой API и какой режим следует использовать?**

Таблица ниже обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая каждый сценарий подробно.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавление поля фильтраы по имени исходного столбца (наиболее распространённый случай) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавление поля фильтраы, когда у вас уже есть объект `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/a | Используйте, когда объект поля был получен в другом месте или должен быть повторно использован. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.CurrentPageItem` | устанавливается на конкретный индекс | Например, `1` показывает второй элемент в отсортированном списке. |
| Показать все элементы / сбросить фильтр страницы | `PivotField.CurrentPageItem` | устанавливается на `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) — это метка-заполнитель для «все элементы». |
| Включение интерфейса множественного выбора в Excel | `PivotField.IsMultipleItemSelectionAllowed` | устанавливается в `true` | Требуется перед тем, как любые вызовы `IsHidden` вступят в силу. |
| Скрытие / отображение отдельных элементов в списке множественного выбора | `PivotItem.IsHidden` | устанавливается для каждого элемента | Как минимум один элемент должен оставаться видимым (`IsHidden == false`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если каждый `PivotItem` в поле фильтра с множественным выбором скрыт, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Создавайте свой белый список на основе ваших исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые книги будут надёжно открываться на любом компьютере.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
