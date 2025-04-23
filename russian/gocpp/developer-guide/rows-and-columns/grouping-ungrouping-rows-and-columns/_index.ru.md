---
title: Группирование, Разгруппирование строк и столбцов
type: docs
weight: 30
url: /ru/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Введение**

В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы контура**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, содержащие сводные сведения или заголовки разделов в листе Excel, или вы можете использовать символы для просмотра деталей под отдельным сводным сведением или заголовком.

## **Управление группировкой строк и столбцов**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) включает коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) содержит коллекцию [Cells](https://reference.aspose.com/cells/go-cpp/cells/), которая представляет все ячейки листа.

Коллекция [Cells](https://reference.aspose.com/cells/go-cpp/cells/) включает несколько методов для управления строками и столбцами листа, некоторые из которых рассмотрены ниже.

### **Группировка строк и столбцов**

Можно группировать строки или столбцы с помощью методов [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) и [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Настройки группировки**

Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.

## **Отмена группировки строк и столбцов**

Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите методы [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) и [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Оба метода принимают два параметра:

- Индекс первой строки или столбца, первая строка/столбец для отмены группировки.
- Индекс последней строки или столбца, последняя строка/столбец для отмены группировки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
