---
title: Éditeur de feuille de calcul  Travailler avec des feuilles
type: docs
weight: 20
url: /fr/java/spreadsheet-editor-working-with-sheets/
---

**Table des matières**

- [Ajouter et supprimer des feuilles?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Renommer les feuilles](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Passer d'une feuille à l'autre](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Ajouter et supprimer des feuilles?**
Microsoft Excel permet plusieurs feuilles dans un seul fichier. L'éditeur de feuilles HTML5 permet à l'utilisateur d'ajouter et de supprimer des feuilles. Sur l'onglet Feuilles, nous avons une liste déroulante de feuilles. La feuille sélectionnée est celle qui est ouverte par l'éditeur.

Pour ajouter une nouvelle feuille:

1. Basculez vers l'onglet **Feuilles**.
1. Cliquez sur le bouton **+** (plus).

Une nouvelle feuille sera ajoutée et l'éditeur basculera dessus.

Pour supprimer la feuille actuellement sélectionnée:

1. Basculez vers l'onglet **Feuilles**.
1. Cliquez sur le bouton **-** (moins).

La feuille actuellement sélectionnée sera supprimée et l'éditeur basculera sur la dernière sélectionnée.

![todo:image_alt_text](4wgvmu8.png)

**Comment cela fonctionne?**

Lorsque l'utilisateur clique sur les boutons **+** (plus) et **-** (moins), le bean backend JSF **WorksheetView** gère les événements en utilisant les méthodes **WorksheetView.onAddNewSheet** et **WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight java >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **Renommer les feuilles**
Pour renommer une feuille:

1. Basculez vers l'onglet **Feuilles**.
1. Cliquez sur le nom de la feuille dans la zone de texte pour le modifier.
1. Changez le nom de la feuille.
1. Lorsque vous avez terminé, appuyez sur la touche ENTRÉE ou cliquez n'importe où à l'extérieur de la boîte.

La feuille sera renommée.

![todo:image_alt_text](4wgvmu8.png)

**Comment cela fonctionne?**

Lorsque la valeur de la zone de texte est modifiée, l'événement est géré côté serveur par le bean backend JSF **WorksheetView** à l'aide de la méthode **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **Passer d'une feuille à l'autre**
Pour passer à une autre feuille :

1. Basculez vers l'onglet **Feuilles**.
1. Sélectionnez une feuille dans le menu déroulant.

L'éditeur passera à la feuille sélectionnée.

![todo:image_alt_text](4wgvmu8.png)

**Comment cela fonctionne?**

Lorsque la valeur du sélecteur déroulant est modifiée, l'événement est géré côté serveur par le bean backend JSF **WorksheetView** à l'aide de la méthode **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
