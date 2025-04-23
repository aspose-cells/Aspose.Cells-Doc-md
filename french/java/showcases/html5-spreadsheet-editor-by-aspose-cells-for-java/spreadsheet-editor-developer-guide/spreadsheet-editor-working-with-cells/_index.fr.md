---
title: Éditeur de feuilles de calcul  Travailler avec les cellules
type: docs
weight: 40
url: /fr/java/spreadsheet-editor-working-with-cells/
---

**Table des matières**

- [Sélection d'une cellule](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Rappel de sélection de cellule
- [Supprimer une cellule](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Effacer une cellule](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Sélection d'une cellule**
Utilisez votre pointeur de souris pour pointer vers une cellule. Cliquez sur une cellule pour la sélectionner. La cellule sélectionnée est mise en évidence par un rectangle en gras.

**Comment cela fonctionne?**

Lorsque l'utilisateur clique sur une cellule, l'événement est traité par une fonction de rappel JavaScript qui est attachée au composant Primefaces.
#### **Callback de sélection de cellule**
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
### **Supprimer une cellule**
Pour supprimer une cellule:

1. Cliquez sur une cellule que vous voulez supprimer.
1. Basculez sur l'onglet **Format**.
1. Cliquez sur le bouton **Supprimer la cellule**.
1. Choisissez le bouton **Décaler les cellules vers le haut** ou **Décaler les cellules vers la gauche**.

L'éditeur supprimera la cellule sélectionnée. Les cellules adjacentes seront automatiquement déplacées soit horizontalement, soit verticalement pour adapter l'espace.

**Comment cela fonctionne?**

Les **Décaler les cellules vers le haut** et **Décaler les cellules vers la gauche** sont gérés par le bean backend JSF **WorksheetView**. Le code source des méthodes respectives est le suivant:
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
### **Effacer une cellule**
Pour effacer une cellule:

1. Cliquez sur une cellule que vous voulez effacer.
1. Basculez sur l'onglet **Format**.
1. Cliquez sur le bouton **Effacer la cellule**.
1. Choisissez l'option **Formats**, **Contenus** ou **Les deux**.

L'éditeur effacera la cellule sélectionnée.

**Comment cela fonctionne?**

Les **Formats**, **Contenus** et **Les deux** sont gérés par le bean backend JSF **WorksheetView**. Le code source des méthodes respectives est le suivant:
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
{{< app/cells/assistant language="java" >}}
