---
title: Группировка и разгруппировка строк и столбцов
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns/
---
## **Вступление**
В файле Excel Microsoft можно создать структуру данных, позволяющую отображать и скрывать уровни детализации одним щелчком мыши.

 Нажмите на**Контурные символы**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые содержат сводки или заголовки для разделов на листе, или вы можете использовать символы, чтобы увидеть подробности под отдельной сводкой или заголовком, как показано ниже на рисунке. :

 Группировка строк и столбцов

![дело:изображение_альтернативный_текст](grouping-and-ungrouping-rows-and-columns_1.png)
## **Групповое управление строками и столбцами**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция, представляющая все ячейки рабочего листа.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection предоставляет несколько методов для управления строками или столбцами на листе, некоторые из них более подробно обсуждаются ниже.
### **Группировка строк и столбцов**
 Можно сгруппировать строки или столбцы, вызвав метод[группа строк](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) и[группаКолонки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) методы[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыт, логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Настройки группы**
Microsoft Excel также позволяет настроить параметры группы для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от подробностей.

**Настройки группы** 

![дело:изображение_альтернативный_текст](grouping-and-ungrouping-rows-and-columns_2.png)

Эти групповые параметры можно настроить с помощью свойства Outline класса Worksheet.
### **Сводные строки под деталями**
 Разработчики могут управлять отображением итоговых строк под деталями с помощью[Контур](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) учебный класс'[РезюмеСтрокаНиже](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) метод.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Сводные столбцы справа от подробностей**
Можно управлять отображением сводных столбцов справа от сведений с помощью кнопки[Контур](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) учебный класс'[РезюмеСтолбецПравый](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)метод.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Разгруппировка строк и столбцов**
 Разгруппируйте сгруппированные строки или столбцы, вызвав метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[Разгруппировать ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) и[Разгруппировать столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) методы. Оба метода принимают одни и те же параметры:

- Индекс первой строки или столбца, первая строка/столбец, подлежащий разгруппировке.
- Индекс последней строки или столбца, последняя строка/столбец для разгруппировки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
