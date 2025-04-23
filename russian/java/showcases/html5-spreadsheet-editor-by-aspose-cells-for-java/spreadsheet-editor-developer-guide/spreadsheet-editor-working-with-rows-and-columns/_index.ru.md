---
title: Редактор электронных таблиц  Работа с строками и столбцами
type: docs
weight: 30
url: /ru/java/spreadsheet-editor-working-with-rows-and-columns/
---

**Содержание**

- [Добавить строку](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Добавить столбец](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Удалить строку](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Удалить столбец](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Ширина столбца и высота строки](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Вставить ячейку](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Добавить строку**
Чтобы добавить новую строку:

1. Щелкните по ячейке, где вы хотите добавить строку.
1. Переключитесь на вкладку **Формат**.
1. Нажмите **Добавить строку выше**, чтобы добавить строку над выбранной ячейкой.
1. Нажмите **Добавить строку ниже**, чтобы добавить строку под выбранной ячейкой.

Редактор добавит новую строку в выбранное место.

![todo:image_alt_text](jjsornm.png)

**Как это работает?**

**Добавить строку выше** и **Добавить строку ниже** обрабатываются бэкэнд-бином JSF **WorksheetView**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addRowAbove**
{{< highlight java >}}

     public void addRowAbove() {

        try {

            getAsposeWorksheet().getCells().insertRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(currentRowId);

    }

{{< /highlight >}}

#### **WorksheetView.addRowBelow**
{{< highlight java >}}

     public void addRowBelow() {

        if (getCurrentRowId() < 0) {

            msg.sendMessage("No cell selected", null);

            return;

        }

        int newRowId = currentRowId + 1;

        try {

            getAsposeWorksheet().getCells().insertRows(newRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(newRowId);

    }

{{< /highlight >}}
### **Добавить столбец**
Чтобы добавить новый столбец:

1. Щелкните по ячейке, где вы хотите добавить столбец.
1. Переключитесь на вкладку **Формат**.
1. Нажмите **Добавить столбец до** для добавления столбца перед выбранной ячейкой.
1. Нажмите **Добавить столбец после** для добавления столбца после выбранной ячейки.

Редактор добавит новый столбец в выбранное место.

![todo:image_alt_text](jjsornm.png)

**Как это работает?**

Операции **Добавить столбец до** и **Добавить столбец после** выполняются бэкэнд-бином JSF **WorksheetView**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addColumnBefore**
{{< highlight java >}}

     public void addColumnBefore() {

        try {

            getAsposeWorksheet().getCells().insertColumns(getCurrentColumnId(), 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(currentColumnId);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.addColumnAfter**
{{< highlight java >}}

     public void addColumnAfter() {

        int newColumnId = currentColumnId + 1;

        try {

            getAsposeWorksheet().getCells().insertColumns(newColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(newColumnId);

        purge();

    }

{{< /highlight >}}
### **Удалить строку**
Для удаления строки:

1. Нажмите на ячейку в строке, которую вы хотите удалить.
1. Переключитесь на вкладку **Формат**.
1. Нажмите кнопку **Удалить строку**.

Редактор удалит строку, включающую выбранную ячейку.

![todo:image_alt_text](jjsornm.png)

**Как это работает?**

Операция кнопки **Удалить строку** обрабатывается бэкэнд-бином JSF **WorksheetView** с помощью метода **WorksheetView.deleteRow**:
#### **WorksheetView.deleteRow**
{{< highlight java >}}

     public void deleteRow() {

        try {

            getAsposeWorksheet().getCells().deleteRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete row", cx.getMessage());

            return;

        }

        cells.getRows(workbook.getCurrent()).remove(currentRowId);

        getRowHeight().remove(currentRowId);

        purge();

    }

{{< /highlight >}}
### **Удалить столбец**
Для удаления столбца:

1. Нажмите на ячейку в столбце, который вы хотите удалить.
1. Переключитесь на вкладку **Формат**.
1. Нажмите кнопку **Удалить столбец**.

Редактор удалит столбец, включающий выбранную ячейку.

![todo:image_alt_text](jjsornm.png)

**Как это работает?**

Кнопка **Удалить столбец** управляется бэкэнд-бином JSF **WorksheetView** с использованием метода **WorksheetView.deleteColumn**:
#### **WorksheetView.deleteColumn**
{{< highlight java >}}

     public void deleteColumn() {

        try {

            getAsposeWorksheet().getCells().deleteColumns(currentColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete column", cx.getMessage());

            return;

        }

        cells.getColumns(workbook.getCurrent()).remove(currentColumnId);

        getRowHeight().remove(currentColumnId);

        purge();

    }

{{< /highlight >}}
### **Ширина столбца и высота строки**
Для изменения ширины столбца:

1. Щелкните любую ячейку внутри столбца.
1. Переключитесь на вкладку **Формат**.
1. Щелкните по кнопке **Ширина столбца**, чтобы открыть диалоговое окно **Ширина столбца**.
1. Введите новое значение в диалоговом окне.
1. Нажмите **Закрыть**.

Редактор изменит ширину столбца.

**Как изменить высоту строки?**

Для изменения высоты строки:

1. Щелкните любую ячейку внутри строки.
1. Переключитесь на вкладку **Формат**.
1. Щелкните по кнопке **Высота строки**, чтобы открыть диалоговое окно **Высота строки**.
1. Введите новое значение в диалоговом окне.
1. Нажмите **Закрыть**.

Редактор изменит высоту строки.

**Как это работает?**

Когда пользователь отправляет значение ширины и высоты, эти значения обрабатываются на серверной стороне с помощью методов **setCurrentRowHeight** и **setCurrentColumnWidth** бэкэнд-бина JSF **WorksheetView**.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight java >}}

     public void setCurrentRowHeight(int height) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setRowHeightPixel(currentRowId, height);

        reloadRowHeight(currentRowId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}

#### **WorksheetView.setCurrentColumnWidth**
{{< highlight java >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **Вставить ячейку**
Чтобы добавить новую ячейку:

1. Нажмите на ячейку, где хотите добавить новую.
1. Переключитесь на вкладку **Вставка**.
1. Нажмите на кнопку **Ячейка**.
1. Выберите кнопку **Сдвинуть ячейки вправо** или **Сдвинуть ячейки вниз**.

Редактор добавит новую ячейку ​​в выбранное место. Соседние ячейки автоматически сдвинутся горизонтально или вертикально, чтобы освободить место для новой.

**Как это работает?**

**Сдвиг ячеек вправо** и **Сдвиг ячеек вниз** обрабатываются бэкэнд-бином JSF **WorksheetView**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addCellShiftRight**
{{< highlight java >}}

     public void addCellShiftRight() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.RIGHT);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.addCellShiftDown**
{{< highlight java >}}

     public void addCellShiftDown() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.DOWN);

        purge();

    }

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
