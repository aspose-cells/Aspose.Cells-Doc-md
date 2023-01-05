---
title: Редактор электронных таблиц — работа с Cells
type: docs
weight: 40
url: /ru/java/spreadsheet-editor-working-with-cells/
---
**Оглавление**

- [Выбор Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell выбор обратного вызова
- [Удалить Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Очистить Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Выбор Cell**
Используйте указатель мыши, чтобы указать на ячейку. Щелкните ячейку, чтобы выбрать ее. Выбранная ячейка выделяется жирным прямоугольником.

**Как это работает?**

Когда пользователь щелкает ячейку, событие обрабатывается функцией обратного вызова JavaScript, которая прикреплена к компоненту Primefaces.
#### **Cell выбор обратного вызова**
{{< highlight "java" >}}

                     var columnId = $(this).find('.ui-cell-editor-input input').attr('data-columnid');

                    var rowId = $(this).find('.ui-cell-editor-input input').attr('data-rowid');

                    var clientId = $(this).find('.ui-cell-editor').attr('id');

                    PF('currentColumnIdValue').jq.val(columnId);

                    PF('currentRowIdValue').jq.val(rowId);

                    PF('currentCellClientIdValue').jq.val(clientId);

                    if ($(this).find('.ui-cell-editor-output div').hasClass('b')) {

                        PF('boldOptionButton').check();

                    } else {

                        PF('boldOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('i')) {

                        PF('italicOptionButton').check();

                    } else {

                        PF('italicOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('u')) {

                        PF('underlineOptionButton').check();

                    } else {

                        PF('underlineOptionButton').uncheck();

                    }

                    PF('fontOptionSelector').selectValue($(this).find('.ui-cell-editor-output div').css('font-family').slice(1, -1));

                    PF('fontSizeOptionSelector').selectValue($(this).find('.ui-cell-editor-output div')[0].style.fontSize.replace('pt', ''));

                    ['al', 'ac', 'ar', 'aj'].forEach(function(v) {

                        if ($(this).find('.ui-cell-editor-output div').hasClass(v)) {

                            // TODO: save the value to PF('alignOptionSelector');

                        }

                    });

                    PF('currentColumnWidthValue').jq.val($(this).width());

                    PF('currentRowHeightValue').jq.val($(this).height());

                    $($this.selectedCell).removeClass('sheet-selected-cell');

                    $(this).addClass('sheet-selected-cell');

                    $this.selectedCell = this;

{{< /highlight >}}
### **Удалить Cell**
Чтобы удалить ячейку:

1. Нажмите на ячейку, которую хотите удалить.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Удалить Cell** кнопка.
1.  выберите**Сдвиг Cells Вверх** или же**Сдвиг Cells Левый** кнопка.

Редактор удалит выбранную ячейку. Соседние ячейки будут автоматически сдвигаться по горизонтали или по вертикали, чтобы отрегулировать пространство.

**Как это работает?**

**Сдвиг Cells Вверх** и**Сдвиг Cells Левый** обрабатываются внутренним компонентом JSF**Вид рабочего листа**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.removeCellShiftUp**
{{< highlight "java" >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight "java" >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **Очистить Cell**
Чтобы очистить ячейку:

1. Нажмите на ячейку, которую хотите очистить.
1.  Переключить на**Вкладка Формат**.
1.  Нажмите**Очистить Cell** кнопка.
1.  выберите**Форматы**, **Содержание** или же**Обе** вариант.

Редактор очистит выбранную ячейку.

**Как это работает?**

**Форматы**, **Содержание** и**Обе** обрабатываются внутренним компонентом JSF**Вид рабочего листа**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.clearCurrentCellFormatting**
{{< highlight "java" >}}

     public void clearCurrentCellFormatting() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearFormats(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCellContents**
{{< highlight "java" >}}

     public void clearCurrentCellContents() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearContents(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCell**
{{< highlight "java" >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}
