---
title: Gestion des événements après la suppression de colonnes et de lignes dans GridDesktop
type: docs
weight: 80
url: /fr/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Scénarios d'utilisation possibles**
Aspose.Cells pour GridDesktop a ajouté deux nouveaux événements, à savoir AfterDeleteColumns et AfterDeleteRows, comme indiqué dans la capture d'écran suivante. Ces événements sont déclenchés lorsque vous supprimez respectivement des colonnes et des lignes.

![tâche : image_autre_texte](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Gestion des événements après la suppression de colonnes et de lignes dans GridDesktop**
L'exemple de code suivant explique comment utiliser les événements AfterDeleteColumns et AfterDeleteRows. Chaque fois que vous supprimez des colonnes ou des lignes, la fonction donnée sera appelée et affichera une boîte de message qui affiche l'index de la colonne ou de la ligne supprimée.
## **Exemple de code**
{{< highlight "java" >}}

 private void gridDesktop1_AfterDeleteColumnsAndRows(object sender, Aspose.Cells.GridDesktop.WorksheetEventArgs args)

{

    if(args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.ColumnDeleted)

    {

        MessageBox.Show("Deleted Column Index: " + args.Index);

    }

    if (args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.RowDeleted)

    {

        MessageBox.Show("Deleted Row Index: " + args.Index);

    }

}

{{< /highlight >}}
