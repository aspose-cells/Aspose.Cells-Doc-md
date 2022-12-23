---
title: Tabelleneditor - Arbeiten mit Cells
type: docs
weight: 40
url: /de/java/spreadsheet-editor-working-with-cells/
---
**Inhaltsverzeichnis**

- [Auswahl einer Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell Auswahl Rückruf
- [Löschen Sie eine Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Löschen Sie eine Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Auswahl einer Cell**
Verwenden Sie Ihren Mauszeiger, um auf eine Zelle zu zeigen. Klicken Sie auf eine Zelle, um sie auszuwählen. Die ausgewählte Zelle wird durch ein dickes Rechteck hervorgehoben.

**Wie es funktioniert?**

Wenn der Benutzer auf eine Zelle klickt, wird das Ereignis von der JavaScript-Callback-Funktion verarbeitet, die an die Primefaces-Komponente angehängt ist.
#### **Cell Auswahl Rückruf**
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
### **Löschen Sie eine Cell**
So löschen Sie eine Zelle:

1. Klicken Sie auf eine Zelle, die Sie löschen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Cell löschen** Knopf.
1.  Wählen**Schicht Cells Hoch** oder**Schicht Cells Links** Knopf.

Der Editor löscht die ausgewählte Zelle. Die angrenzenden Zellen werden automatisch entweder horizontal oder vertikal verschoben, um den Abstand anzupassen.

**Wie es funktioniert?**

 Das**Schicht Cells Hoch** und**Schicht Cells Links** werden von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht**. Der Quellcode der jeweiligen Methoden sieht wie folgt aus:
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
### **Löschen Sie eine Cell**
So löschen Sie eine Zelle:

1. Klicken Sie auf eine Zelle, die Sie löschen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Klar Cell** Knopf.
1.  Wählen**Formate**, **Inhalt** oder**Beide** Möglichkeit.

Der Editor löscht die ausgewählte Zelle.

**Wie es funktioniert?**

 Das**Formate**, **Inhalt** und**Beide** werden von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht**. Der Quellcode der jeweiligen Methoden sieht wie folgt aus:
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
