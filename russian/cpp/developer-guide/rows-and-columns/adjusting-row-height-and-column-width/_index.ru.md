---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменение высоты строк или ширины столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться для отображения данных. Обычно пользователи изменяют высоту строк и ширины столбцов в среде WYSIWYG с помощью Microsoft Excel. Однако разработчики Aspose.Cells могут выполнять эти операции во время выполнения.

{{% /alert %}} 
## **Работа со строками**
### **Изменение высоты строки**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), который позволяет получить доступ ко всем листам Excel файла. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), которая представляет все ячейки на листе. Коллекция [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них подробно обсуждаются ниже.
#### **Установка высоты строки**
Можно установить высоту отдельной строки, вызвав метод [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Установка высоты всех строк на листе**
Если разработчикам нужно установить одинаковую высоту строки для всех строк на листе, они могут сделать это, используя метод [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Работа с колонками**
### **Установка ширины колонки**
Установите ширину колонки, вызвав метод [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Установка ширины всех колонок на листе**
Чтобы установить одинаковую ширину колонки для всех колонок на листе, используйте метод [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
