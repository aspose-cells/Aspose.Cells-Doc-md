---
title: Группировка и расгруппировка строк и столбцов
type: docs
weight: 50
url: /ru/python-net/grouping-and-ungrouping-rows-and-columns/
description: Этот статья показывает, как группировать и разгруппировывать строки и столбцы с помощью Aspose.Cells for Python via .NET API.
keywords: Библиотека Excel для Python, Как группировать строки и столбцы в Python, Как разгруппировывать строки и столбцы в Python, Управление группами строк и столбцов в Python, Как установить строки резюме ниже деталей в Python, Как установить столбцы резюме справа от деталей в Python.
---

## **Введение**

В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы сводки**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые предоставляют сводки или заголовки для разделов в листе, или можно использовать символы, чтобы увидеть детали под отдельной сводкой или заголовком, как показано ниже на рисунке:

|**Группировка строк и столбцов.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Управление группировкой строк и столбцов**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу Excel в файле. Лист Excel представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), представляющую все ячейки на листе Excel.

Коллекция [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе, ниже подробно рассмотрены некоторые из них.

### **Как группировать строки и столбцы**

Возможно сгруппировать строки или столбцы, вызвав методы [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) и [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Настройки группировки**

Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.

Разработчики могут настроить параметры группы, используя свойство [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

### **Как установить строки резюме ниже деталей**

Возможно управлять отображением итоговых строк под деталями, установив свойство [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) класса [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) в **true** или **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Как установить столбцы резюме справа от деталей**

Разработчики могут также управлять отображением итоговых столбцов справа от деталей, установив свойство [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) класса [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) в **true** или **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Как разгруппировывать строки и столбцы**

Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите методы [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) и [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Оба метода принимают два параметра:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) имеет перегрузку, принимающую третий параметр логического типа. Установка его в **true** удаляет всю группированную информацию. В противном случае удаляется только внешняя информация о группе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
