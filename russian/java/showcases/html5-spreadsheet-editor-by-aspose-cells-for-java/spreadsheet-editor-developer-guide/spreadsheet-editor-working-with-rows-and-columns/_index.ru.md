---
title: Редактор электронных таблиц — Работа со строками и столбцами
type: docs
weight: 30
url: /ru/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Оглавление**

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
- [Вставьте Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Добавить строку**
Чтобы добавить новую строку:

1. Нажмите на ячейку, в которую вы хотите добавить строку.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Добавить строку выше** чтобы добавить строку над выбранной ячейкой.
1.  Нажмите**Добавить строку ниже** чтобы добавить строку под выбранной ячейкой.

Редактор добавит новую строку в выбранное место.

![дело:изображение_альтернативный_текст](jjsornm.png)

**Как это работает?**

**Добавить строку выше** и**Добавить строку ниже** обрабатываются внутренним компонентом JSF**Вид рабочего листа**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addRowAbove**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1. Щелкните ячейку, в которую вы хотите добавить столбец.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Добавить столбец перед**чтобы добавить столбец перед выбранной ячейкой.
1.  Нажмите**Добавить столбец после** чтобы добавить столбец после выбранной ячейки.

Редактор добавит новый столбец в выбранное место.

![дело:изображение_альтернативный_текст](jjsornm.png)

**Как это работает?**

**Добавить столбец перед** и**Добавить столбец после** обрабатываются внутренним компонентом JSF**Вид рабочего листа**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addColumnBefore**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
Чтобы удалить строку:

1. Нажмите на ячейку в строке, которую вы хотите удалить.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Удалить строку** кнопка.

Редактор удалит строку, содержащую выбранную ячейку.

![дело:изображение_альтернативный_текст](jjsornm.png)

**Как это работает?**

**Удалить строку** кнопка обрабатывается внутренним компонентом JSF**Вид рабочего листа** используя метод**WorksheetView.deleteRow**:
#### **WorksheetView.deleteRow**
{{< highlight "java" >}}

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
Чтобы удалить столбец:

1. Нажмите на ячейку в столбце, который вы хотите удалить.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Удалить столбец** кнопка.

Редактор удалит столбец, содержащий выбранную ячейку.

![дело:изображение_альтернативный_текст](jjsornm.png)

**Как это работает?**

**Удалить столбец** кнопка обрабатывается внутренним компонентом JSF**Вид рабочего листа** используя метод**WorksheetView.deleteColumn**:
#### **WorksheetView.deleteColumn**
{{< highlight "java" >}}

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
Чтобы изменить ширину столбца:

1. Нажмите на любую ячейку внутри столбца.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Ширина колонки** кнопка, чтобы открыть**Ширина колонки** диалог.
1. Введите новое значение в диалоговом окне.
1.  Нажмите**Закрывать**.

Редактор изменит ширину столбца.

**Как изменить высоту строки?**

Чтобы изменить высоту строки:

1. Нажмите на любую ячейку внутри строки.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Высота строки** кнопка, чтобы открыть**Высота строки** диалог.
1. Введите новое значение в диалоговом окне.
1.  Нажмите**Закрывать**.

Редактор изменит высоту строки.

**Как это работает?**

 Когда пользователь отправляет значение ширины и высоты, эти значения обрабатываются на стороне сервера**setCurrentRowHeight** и**setCurrentColumnWidth** методы внутреннего компонента JSF**Вид рабочего листа**.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **Вставьте Cell**
Чтобы добавить новую ячейку:

1. Нажмите на ячейку, которую вы хотите создать.
1.  Переключить на**Вкладка «Вставка»**.
1.  Нажмите**Cell** кнопка.
1.  выберите**Сдвиг Cells Вправо** или же**Сдвиг Cells Вниз** кнопка.

Редактор добавит новую ячейку в выбранное место. Соседние ячейки будут автоматически сдвинуты по горизонтали или вертикали, чтобы освободить место для новой.

**Как это работает?**

**Сдвиг Cells Вправо** и**Сдвиг Cells Вниз** обрабатываются внутренним компонентом JSF**Вид рабочего листа**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.addCellShiftRight**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
