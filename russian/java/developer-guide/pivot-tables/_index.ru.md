---
title: Создание сводной таблицы
linktitle: Создание сводной таблицы
description: Создание и форматирование сводных таблиц с помощью Aspose.Cells for Java.
keywords: Создание сводной таблицы, Вставка сводной таблицы, Форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный отчет для обобщения данных: он преобразует большой массив необработанных данных, записанных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут агрегироваться как значения: сводная таблица выполняет группировку и вычисления:
- **Подведение итогов** — итоговый объем продаж в разрезе продуктов, регионов или кварталов вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в наглядную перекрестную таблицу, в которой сразу видны тенденции.
- **Детализация** — дважды щелкните по любому итоговому значению, чтобы посмотреть исходные строки, из которых оно сформировано.
- **Обновление** — при изменении исходных данных одно обновление пересчитывает весь отчет.
Типичные сценарии применения — информационные панели продаж, анализ структуры расходов и анализ запасов. Они позволяют ответить на вопросы вида «как эти числа распределяются по категориям и периодам?». Aspose.Cells for Java позволяет программно создавать такие же сводные таблицы, поэтому рабочие книги, создаваемые вашим приложением, могут содержать готовые отчеты, а не только необработанные данные.

### **Создание сводной таблицы с помощью Aspose.Cells**

{{% alert color="primary" %}}
С помощью Aspose.Cells в электронные таблицы можно добавлять сводные таблицы. В Aspose.Cells есть ряд специальных классов, предназначенных для создания и управления сводными таблицами. Эти классы используются для создания и настройки свойств объекта [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), который служит строительным блоком сводной таблицы.
Объекты, связанные со сводными таблицами:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): представляет поле сводной таблицы.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): представляет коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) в сводной таблице.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): представляет сводную таблицу.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): представляет коллекцию всех объектов сводных таблиц на рабочем листе.
{{% /alert %}}

### **Создание простой сводной таблицы**
Создание сводной таблицы состоит из трех шагов: записать исходные данные в ячейки рабочего листа, добавить сводную таблицу в позицию назначения и поместить поля сводной таблицы в области строк, столбцов и данных.
1. Добавьте данные в ячейки рабочего листа с помощью метода [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) объекта [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) (`putValue` в большинстве примеров). Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу на рабочий лист, вызвав метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) класса [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): `add(sourceData, row, column)`. `sourceData` — исходный диапазон (например, "A1:C8"); `row` и `column` — координаты ячейки назначения с индексацией с нуля. Например, ячейка E3 в левом верхнем углу сводной таблицы соответствует строке 2 и столбцу 4. Метод непосредственно возвращает новый объект [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
3. Разместите поля сводной таблицы с помощью метода `addFieldToArea` объекта [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): имя поля помещается в область строк (`PivotFieldType.ROW`), область столбцов (`PivotFieldType.COLUMN`) или область данных (`PivotFieldType.DATA`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохраненный файл.
Приведенный ниже пример кода создает простую сводную таблицу в соответствии с этими шагами. При его выполнении на рабочий лист добавляется сводная таблица на основе исходных данных:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Создать новую книгу и получить первый лист
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Записать исходные данные: продажи по видам спорта и кварталам
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Добавить сводную таблицу в ячейку E3 на основе A1:C8
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Назначить поля сводной таблицы: Sport — строки, Quarter — столбцы, Sales — данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Сохранить книгу
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
При указании диапазона ячеек в качестве источника данных он должен быть задан в направлении от верхней левой ячейки к нижней правой. Например, "A1:C3" — допустимый диапазон, а "C3:A1" — недопустимый.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}