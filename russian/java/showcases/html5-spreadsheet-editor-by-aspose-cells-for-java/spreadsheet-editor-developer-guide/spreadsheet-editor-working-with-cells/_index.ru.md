---
title: Редактор электронных таблиц  Работа с ячейками
type: docs
weight: 40
url: /ru/java/spreadsheet-editor-working-with-cells/
---

**Содержание**

- [Выбор ячейки](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Обратный вызов выбора ячейки
- [Удаление ячейки](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Очистить ячейку](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Выбор ячейки**
Используйте указатель мыши для выделения ячейки. Щелкните по ячейке, чтобы выбрать ее. Выбранная ячейка выделяется жирным прямоугольником.

**Как это работает?**

Когда пользователь щелкает по ячейке, событие обрабатывается функцией обратного вызова JavaScript, которая привязана к компоненту Primefaces.
#### **Функция обратного вызова выбора ячейки**
{{< highlight java >}}

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
### **Удаление ячейки**
Чтобы удалить ячейку:

1. Щелкните по ячейке, которую хотите удалить.
1. Переключитесь на вкладку **Формат**.
1. Нажмите на кнопку **Удалить ячейку**.
1. Выберите кнопку **Сдвинуть ячейки вверх** или **Сдвинуть ячейки влево**.

Редактор удалит выбранную ячейку. Смежные ячейки автоматически сдвинутся горизонтально или вертикально, чтобы скорректировать пространство.

**Как это работает?**

**Сдвинуть ячейки вверх** и **Сдвинуть ячейки влево** обрабатываются бэкэнд-бином JSF **WorksheetView**. Исходный код соответствующих методов выглядит следующим образом:
#### **WorksheetView.removeCellShiftUp**
{{< highlight java >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight java >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **Очистить ячейку**
Чтобы очистить ячейку:

1. Щелкните по ячейке, которую хотите очистить.
1. Переключитесь на вкладку **Формат**.
1. Нажмите на кнопку **Очистить ячейку**.
1. Выберите опцию **Форматы**, **Содержимое** или **Оба**.

Редактор очистит выбранную ячейку.

**Как это работает?**

**Форматы**, **Содержимое** и **Оба** обрабатываются бэкэнд-бином JSF **WorksheetView**. Исходный код соответствующих методов приведен ниже:
#### **WorksheetView.clearCurrentCellFormatting**
{{< highlight java >}}

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
{{< highlight java >}}

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
{{< highlight java >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}
