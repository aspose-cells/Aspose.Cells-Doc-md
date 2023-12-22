---
title: Группировка, разгруппировка строк и столбцов
type: docs
weight: 30
url: /ru/cpp/grouping-ungrouping-rows-and-columns/
---
##  **Введение**
В файле Excel Microsoft вы можете создать структуру данных, чтобы можно было показывать и скрывать уровни детализации одним щелчком мыши.

Нажмите *Символы структуры**, 1,2,3, + и -, чтобы быстро отобразить только те строки или столбцы, которые содержат сводку или заголовки разделов на листе, или вы можете использовать символы, чтобы просмотреть детали в отдельной сводке или заголовок.
##  **Групповое управление строками и столбцами**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция, представляющая все ячейки на листе.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Коллекция предоставляет несколько методов управления строками и столбцами на листе, некоторые из них более подробно обсуждаются ниже.
###  **Группировка строк и столбцов**
 Можно сгруппировать строки или столбцы, вызвав[ГруппаРовс](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) и[ГруппаСтолбцы](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) методы[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрытый — логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Настройки группы**
Microsoft Excel позволяет настроить параметры группы для отображения:

- Строки сводки под подробностями.
- Столбцы сводки справа от подробностей.
##  **Разгруппировка строк и столбцов**
 Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[Разгруппировать строки](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) и[Разгруппировать столбцы](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)методы. Оба метода принимают два параметра:

- Индекс первой строки или столбца, первая строка/столбец, которую нужно разгруппировать.
- Индекс последней строки или столбца, последняя строка/столбец, которую нужно разгруппировать.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
