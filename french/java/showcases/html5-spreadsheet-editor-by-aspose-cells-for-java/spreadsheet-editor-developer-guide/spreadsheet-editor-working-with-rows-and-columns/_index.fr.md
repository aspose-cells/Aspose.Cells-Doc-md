---
title: Éditeur de feuille de calcul - Travailler avec des lignes et des colonnes
type: docs
weight: 30
url: /fr/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Table des matières**

- [Ajouter une ligne](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 - WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [Ajouter une colonne](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 - WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [Supprimer une ligne](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 - WorksheetView.deleteRow
- [Supprimer une colonne](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [Largeur de colonne et hauteur de ligne](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 - WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [Insérez un Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Ajouter une ligne**
Pour ajouter une nouvelle ligne :

1. Cliquez sur une cellule où vous souhaitez ajouter une ligne.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Ajouter une ligne au-dessus** pour ajouter une ligne au-dessus de la cellule sélectionnée.
1.  Cliquez sur**Ajouter une ligne ci-dessous** pour ajouter une ligne sous la cellule sélectionnée.

L'éditeur ajoutera une nouvelle ligne à l'emplacement sélectionné.

![tâche : image_autre_texte](jjsornm.png)

**Comment ça fonctionne?**

 La**Ajouter une ligne au-dessus** et**Ajouter une ligne ci-dessous** sont gérés par le bean backend JSF**Feuille de calcul**. Le code source des méthodes respectives est le suivant :
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
### **Ajouter une colonne**
Pour ajouter une nouvelle colonne :

1. Cliquez sur une cellule où vous souhaitez ajouter une colonne.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Ajouter une colonne avant**pour ajouter une colonne avant la cellule sélectionnée.
1.  Cliquez sur**Ajouter une colonne après** pour ajouter une colonne après la cellule sélectionnée.

L'éditeur ajoutera une nouvelle colonne à l'emplacement sélectionné.

![tâche : image_autre_texte](jjsornm.png)

**Comment ça fonctionne?**

 La**Ajouter une colonne avant** et**Ajouter une colonne après** sont gérés par le bean backend JSF**Feuille de calcul**. Le code source des méthodes respectives est le suivant :
#### **WorksheetView.addColumnBeforeWorksheetView.addColumnBefore**
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
### **Supprimer une ligne**
Pour supprimer une ligne :

1. Cliquez sur une cellule de la ligne que vous souhaitez supprimer.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Supprimer la ligne** bouton.

L'éditeur supprimera la ligne qui comprend la cellule sélectionnée.

![tâche : image_autre_texte](jjsornm.png)

**Comment ça fonctionne?**

 La**Supprimer la ligne** le bouton est géré par le bean backend JSF**Feuille de calcul** en utilisant la méthode**WorksheetView.deleteRowWorksheetView.deleteRow**:
#### **WorksheetView.deleteRowWorksheetView.deleteRow**
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
### **Supprimer une colonne**
Pour supprimer une colonne :

1. Cliquez sur une cellule de la colonne que vous souhaitez supprimer.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Supprimer la colonne** bouton.

L'éditeur supprimera la colonne qui contient la cellule sélectionnée.

![tâche : image_autre_texte](jjsornm.png)

**Comment ça fonctionne?**

 La**Supprimer la colonne** le bouton est géré par le bean backend JSF**Feuille de calcul** en utilisant la méthode**WorksheetView.deleteColumn**:
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
### **Largeur de colonne et hauteur de ligne**
Pour modifier la largeur d'une colonne :

1. Cliquez sur n'importe quelle cellule à l'intérieur de la colonne.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Largeur de colonne** bouton pour ouvrir**Largeur de colonne**dialogue.
1. Saisissez une nouvelle valeur dans la boîte de dialogue.
1.  Cliquez sur**proche**.

L'éditeur modifiera la largeur de la colonne.

**Comment changer la hauteur de ligne ?**

Pour modifier la hauteur d'une ligne :

1. Cliquez sur n'importe quelle cellule à l'intérieur de la ligne.
1.  Basculer vers**Onglet Format**.
1.  Cliquez sur**Hauteur de ligne** bouton pour ouvrir**Hauteur de ligne**dialogue.
1. Saisissez une nouvelle valeur dans la boîte de dialogue.
1.  Cliquez sur**proche**.

L'éditeur modifiera la hauteur de la ligne.

**Comment ça fonctionne?**

 Lorsque l'utilisateur soumet la valeur de largeur et de hauteur, ces valeurs sont gérées côté serveur par**setCurrentRowHeight** et**setCurrentColumnWidth** méthodes du bean backend JSF**Feuille de calcul**.
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
### **Insérez un Cell**
Pour ajouter une nouvelle cellule :

1. Cliquez sur une cellule où vous voulez créer un nouveau.
1.  Basculer vers**Insérer un onglet**.
1.  Cliquez sur**Cell** bouton.
1.  Choisir**Maj Cells Droite** ou**Maj Cells vers le bas** bouton.

L'éditeur ajoutera une nouvelle cellule à l'emplacement sélectionné. Les cellules adjacentes seront automatiquement décalées horizontalement ou verticalement pour créer de l'espace pour la nouvelle.

**Comment ça fonctionne?**

 La**Maj Cells Droite** et**Maj Cells vers le bas** sont gérés par le bean backend JSF**Feuille de calcul**. Le code source des méthodes respectives est le suivant :
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
