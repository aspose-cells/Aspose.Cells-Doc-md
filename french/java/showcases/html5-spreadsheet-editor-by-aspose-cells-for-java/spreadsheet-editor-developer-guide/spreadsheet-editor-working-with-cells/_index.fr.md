---
title: Éditeur de feuille de calcul - Travailler avec Cells
type: docs
weight: 40
url: /fr/java/spreadsheet-editor-working-with-cells/
---
**Table des matières**

- [Sélection d'un Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Rappel de sélection Cell
- [Supprimer un Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Effacer un Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Sélection d'un Cell**
Utilisez le pointeur de votre souris pour pointer sur une cellule. Cliquez sur une cellule pour la sélectionner. La cellule sélectionnée est mise en évidence par un rectangle gras.

**Comment ça fonctionne?**

Lorsque l'utilisateur clique sur une cellule, l'événement est géré par la fonction de rappel JavaScript qui est attachée au composant Primefaces.
#### **Cell rappel de sélection**
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
### **Supprimer un Cell**
Pour supprimer une cellule :

1. Cliquez sur une cellule que vous souhaitez supprimer.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Supprimer Cell** bouton.
1.  Choisir**Maj Cells vers le haut** ou alors**Maj Cells Gauche** bouton.

L'éditeur supprimera la cellule sélectionnée. Les cellules adjacentes seront automatiquement décalées horizontalement ou verticalement pour ajuster l'espace.

**Comment ça fonctionne?**

 Le**Maj Cells vers le haut** et**Maj Cells Gauche** sont gérés par le bean backend JSF**Feuille de calcul**. Le code source des méthodes respectives est le suivant :
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
### **Effacer un Cell**
Pour vider une cellule :

1. Cliquez sur une cellule que vous souhaitez effacer.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Clair Cell** bouton.
1.  Choisir**Formats**, **Contenu** ou alors**Tous les deux** option.

L'éditeur effacera la cellule sélectionnée.

**Comment ça fonctionne?**

 Le**Formats**, **Contenu** et**Tous les deux** sont gérés par le bean backend JSF**Feuille de calcul**. Le code source des méthodes respectives est le suivant :
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
