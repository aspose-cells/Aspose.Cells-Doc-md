---
title: Tabellenkalkulation Editor  Arbeiten mit Zellen
type: docs
weight: 40
url: /de/java/spreadsheet-editor-working-with-cells/
---

**Inhaltsverzeichnis**

- [Auswahl einer Zelle](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Callback für die Auswahl einer Zelle
- [Löschen einer Zelle](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Eine Zelle löschen](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Auswahl einer Zelle**
Verwenden Sie Ihren Mauszeiger, um auf eine Zelle zu zeigen. Klicken Sie auf eine Zelle, um sie auszuwählen. Die ausgewählte Zelle wird durch ein fett gedrucktes Rechteck hervorgehoben.

**Wie funktioniert es?**

Wenn der Benutzer auf eine Zelle klickt, wird das Ereignis von der JavaScript-Callback-Funktion behandelt, die an das Primefaces-Komponente angehängt ist.
#### **Callback zur Zellenauswahl**
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
### **Löschen einer Zelle**
Um eine Zelle zu löschen:

1. Klicken Sie auf die Zelle, die Sie löschen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Zelle löschen**.
1. Wählen Sie die Schaltfläche **Zellen nach oben verschieben** oder **Zellen nach links verschieben**.

Der Editor wird die ausgewählte Zelle löschen. Die benachbarten Zellen werden automatisch entweder horizontal oder vertikal verschoben, um den Platz anzupassen.

**Wie funktioniert es?**

Das Verschieben von Zellen nach oben und nach links wird vom JSF-Backend-Bean **WorksheetView** behandelt. Der Quellcode der entsprechenden Methoden lautet wie folgt:
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
### **Eine Zelle löschen**
Um eine Zelle zu löschen:

1. Klicken Sie auf eine Zelle, die Sie löschen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Zelle löschen**.
1. Wählen Sie die Option **Formate**, **Inhalte** oder **Beides**.

Der Editor wird die ausgewählte Zelle löschen.

**Wie funktioniert es?**

Die **Formate**, **Inhalte** und **Beides** werden von der JSF-Back-End-Bean **WorksheetView** behandelt. Der Quellcode der entsprechenden Methoden lautet wie folgt:
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
