---
title: Éditeur de feuille de calcul - Travailler avec des feuilles
type: docs
weight: 20
url: /fr/java/spreadsheet-editor-working-with-sheets/
---
**Table des matières**

- [Ajouter et supprimer des feuilles ?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Renommer les feuilles](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Basculer entre les feuilles](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Ajouter et supprimer des feuilles ?**
Microsoft Excel autorise plusieurs feuilles dans un seul fichier. HTML5 Spreadsheet Editor permet à l'utilisateur d'ajouter et de supprimer des feuilles. Dans l'onglet Feuilles, nous avons une liste déroulante de feuilles. La feuille sélectionnée est celle qui est ouverte par l'éditeur.

Pour ajouter une nouvelle feuille :

1.  Basculer vers**Onglet Feuilles**.
1. Cliquez sur le bouton ***+** (plus).

Une nouvelle feuille sera ajoutée et l'éditeur y basculera.

Pour supprimer la feuille actuellement sélectionnée :

1.  Basculer vers**Onglet Feuilles**.
1. Cliquez sur le bouton **-** (moins).

La feuille actuellement sélectionnée sera supprimée et l'éditeur passera à la dernière feuille sélectionnée.

![tâche : image_autre_texte](4wgvmu8.png)

**Comment ça fonctionne?**

 Lorsque l'utilisateur clique sur** +** (plus) et**-** (moins) sont cliqués, le bean backend JSF**Feuille de calcul** gère les événements à l'aide**WorksheetView.onAddNewSheet** et**Méthodes WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
Pour renommer une feuille :

1.  Basculer vers**Onglet Feuilles**.
1. Cliquez sur le nom de la feuille dans la zone de texte pour la modifier.
1. Modifiez le nom de la feuille.
1. Lorsque vous avez terminé, appuyez sur la touche ENTREE ou cliquez n'importe où en dehors de la zone.

La feuille sera renommée.

![tâche : image_autre_texte](4wgvmu8.png)

**Comment ça fonctionne?**

 Lorsque la valeur de la zone de texte est modifiée, l'événement est géré sur le serveur par le bean backend JSF**Feuille de calcul** en utilisant la méthode**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
### **Basculer entre les feuilles**
Pour passer à une autre feuille :

1.  Basculer vers**Onglet Feuilles**.
1. Sélectionnez une feuille dans le menu déroulant.

L'éditeur passera à la feuille sélectionnée.

![tâche : image_autre_texte](4wgvmu8.png)

**Comment ça fonctionne?**

 Lorsque la valeur du sélecteur déroulant est modifiée, l'événement est géré sur le serveur par le bean backend JSF**Feuille de calcul** en utilisant la méthode**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
