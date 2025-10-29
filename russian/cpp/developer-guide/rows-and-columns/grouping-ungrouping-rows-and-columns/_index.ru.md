---
title: Группирование, Разгруппирование строк и столбцов
type: docs
weight: 30
url: /ru/cpp/grouping-ungrouping-rows-and-columns/
---

## **Введение**
В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы контура**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, содержащие сводные сведения или заголовки разделов в листе Excel, или вы можете использовать символы для просмотра деталей под отдельным сводным сведением или заголовком.
## **Управление группировкой строк и столбцов**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), представляющую все ячейки на листе.

Коллекция [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками или столбцами на листе, несколько из них рассмотрены ниже более подробно.
### **Группировка строк и столбцов**
Возможно сгруппировать строки или столбцы, вызвав методы [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) и [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Настройки группировки**
Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.
## **Отмена группировки строк и столбцов**
Чтобы отменить группировку строк или столбцов, вызовите методы [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) и [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают два параметра:

- Индекс первой строки или столбца, первая строка/столбец для отмены группировки.
- Индекс последней строки или столбца, последняя строка/столбец для отмены группировки.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
