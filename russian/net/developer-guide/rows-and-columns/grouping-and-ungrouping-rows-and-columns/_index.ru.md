---
title: Группировка и расгруппировка строк и столбцов
type: docs
weight: 50
url: /ru/net/grouping-and-ungrouping-rows-and-columns/
---

## **Введение**

В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы сводки**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые предоставляют сводки или заголовки для разделов в листе, или можно использовать символы, чтобы увидеть детали под отдельной сводкой или заголовком, как показано ниже на рисунке:

|**Группировка строк и столбцов.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Управление группировкой строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), что позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) обеспечивает коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), которая представляет все ячейки в листе.

Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе, ниже подробно рассмотрены некоторые из них.

### **Группировка строк и столбцов**

Возможно сгруппировать строки или столбцы, вызвав методы [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) и [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Настройки группировки**

Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.

Разработчики могут настроить параметры группы, используя свойство [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

### **Итоговые строки под деталями**

Возможно управлять отображением итоговых строк под деталями, установив свойство [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) класса [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) в **true** или **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Итоговые столбцы справа от деталей**

Разработчики могут также управлять отображением итоговых столбцов справа от деталей, установив свойство [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) класса [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) в **true** или **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Разгруппировка строк и столбцов**

Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите методы [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) и [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода принимают два параметра:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) имеет перегрузку, принимающую третий параметр логического типа. Установка его в **true** удаляет всю группированную информацию. В противном случае удаляется только внешняя информация о группе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
