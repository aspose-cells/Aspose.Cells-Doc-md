---
title: Группировка и расгруппировка строк и столбцов
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns/
---

## **Введение**
В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы сводки**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые предоставляют сводки или заголовки для разделов в листе, или можно использовать символы, чтобы увидеть детали под отдельной сводкой или заголовком, как показано ниже на рисунке:

Группировка строк и столбцов 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Управление группировкой строк и столбцов**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждой рабочей книге в файле Excel. Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), которая представляет все ячейки в рабочем листе.

Коллекция [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) предоставляет несколько методов для управления строками или столбцами в рабочем листе, несколько из которых обсуждаются ниже более подробно.
### **Группировка строк и столбцов**
Можно группировать строки или столбцы, вызвав методы [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) и [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Настройки группировки**
Microsoft Excel также позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводки столбцов справа от деталей.

**Настройки группировки** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Возможно настроить эти параметры группировки, используя свойство Outline класса Worksheet.
### **Сводки строк ниже деталей**
Разработчики могут управлять отображением сводных строк под деталями, используя метод [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) класса [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Итоговые столбцы справа от деталей**
Возможно управлять отображением сводных столбцов справа от деталей с помощью метода [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) класса [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Отмена группировки строк и столбцов**
Разгруппировать сгруппированные строки или столбцы, вызвав методы [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) и [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) коллекции [Cells]. Оба метода принимают одинаковые параметры:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
