---
title: Gérer les événements après la suppression de colonnes et de lignes dans GridDesktop
type: docs
weight: 80
url: /fr/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop, événements, supprimer ligne, supprimer colonne
description: Cet article introduit les événements après la suppression de lignes/colonnes dans GridDesktop.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells pour GridDesktop a ajouté deux nouveaux événements, à savoir AfterDeleteColumns et AfterDeleteRows comme le montre la capture d'écran suivante. Ces événements sont déclenchés lorsque vous supprimez des colonnes et des lignes respectivement.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Gérer les événements après la suppression de colonnes et de lignes dans GridDesktop**
Le code d'exemple suivant explique comment utiliser les événements AfterDeleteColumns et AfterDeleteRows. Chaque fois que vous supprimez des colonnes ou des lignes, la fonction donnée sera appelée et affichera une boîte de message qui affiche l'index de la colonne ou de la ligne supprimée.
## **Code d'exemple**
{{< highlight java >}}

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
