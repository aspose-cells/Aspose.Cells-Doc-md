---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что для отображения данных необходимо изменить текущую высоту или ширину. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Но с Aspose.Cells разработчики могут выполнять эти операции во время выполнения.

{{% /alert %}} 
## **Работа со строками**
### **Регулировка высоты строки**
 Aspose.Cells предоставляет класс,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция, представляющая все ячейки рабочего листа.[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже более подробно.
#### **Установка высоты строки**
 Можно установить высоту одной строки, вызвав функцию[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) метод.[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)Метод принимает следующие параметры следующим образом:

- **Индекс строки**, индекс строки, высоту которой вы меняете.
- **Высота строки**, высота строки, применяемая к строке.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Установка высоты всех строк на листе**
 Если разработчикам нужно установить одинаковую высоту для всех строк на листе, они могут сделать это с помощью[SetStandardHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Работа со столбцами**
### **Установка ширины столбца**
 Задайте ширину столбца, вызвав метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) метод.[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)метод принимает следующие параметры:

- **Индекс столбца**, индекс столбца, ширину которого вы меняете.
- **Ширина колонки**, желаемая ширина столбца.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Установка ширины всех столбцов на листе**
 Чтобы установить одинаковую ширину столбца для всех столбцов на листе, используйте[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[SetStandardWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
