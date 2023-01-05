---
title: Группировка, разгруппировка строк и столбцов
type: docs
weight: 30
url: /ru/cpp/grouping-ungrouping-rows-and-columns/
---
## **Вступление**
В файле Excel Microsoft можно создать структуру данных, позволяющую отображать и скрывать уровни детализации одним щелчком мыши.

 Нажмите на**Контурные символы**, 1,2,3, + и -, чтобы быстро отобразить только те строки или столбцы, которые содержат сводки или заголовки для разделов на листе, или вы можете использовать символы, чтобы просмотреть подробности под отдельной сводкой или заголовком.
## **Групповое управление строками и столбцами**
 Aspose.Cells предоставляет класс,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция, представляющая все ячейки рабочего листа.

[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection предоставляет несколько методов для управления строками или столбцами на листе, некоторые из них более подробно обсуждаются ниже.
### **Группировка строк и столбцов**
 Можно сгруппировать строки или столбцы, вызвав метод[ГруппРовс](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) и[Групповые столбцы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) методы[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыт, логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Настройки группы**
Microsoft Excel позволяет настроить параметры группы для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от подробностей.
## **Разгруппировка строк и столбцов**
 Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[Разгруппировать ряды](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) и[Разгруппировать столбцы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)методы. Оба метода принимают два параметра:

- Индекс первой строки или столбца, первая строка/столбец для разгруппировки.
- Индекс последней строки или столбца, последняя строка/столбец для разгруппировки.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
