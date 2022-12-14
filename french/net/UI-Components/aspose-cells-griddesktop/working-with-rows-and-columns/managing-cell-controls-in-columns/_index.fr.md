---
title: Gestion des contrôles Cell dans les colonnes
type: docs
weight: 100
url: /fr/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Cette rubrique aborde certains concepts importants concernant la gestion des contrôles de cellule dans les colonnes à l'aide de Aspose.Cells.GridDesktop API. Nous expliquerons comment les développeurs peuvent accéder, modifier et supprimer les contrôles de cellule des colonnes de leurs feuilles de calcul. Jetons-y un œil.

{{% /alert %}} 
## **Accès aux commandes Cell**
 Pour accéder à un contrôle de cellule existant dans la colonne et le modifier, les développeurs peuvent utiliser la propriété CellControl d'un**Aspose.Cells.GridDesktop.Data.GridColumn** . Une fois qu'un contrôle de cellule est accédé, les développeurs peuvent modifier ses propriétés lors de l'exécution. Pour une instance, dans l'exemple ci-dessous, nous avons accédé à une instance existante**Case à cocher** contrôle cellulaire à partir d'un**Aspose.Cells.GridDesktop.Data.GridColumn** et modifié sa propriété Checked.

**IMPORTANT:** La propriété CellControl fournit un contrôle de cellule sous la forme de**CellControl**objet. Donc, si vous avez besoin d'accéder à un type spécifique de contrôle de cellule, dites**Case à cocher** alors vous devrez transtyper le**CellControl** s'opposer à**Case à cocher** classer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Retrait des commandes Cell**
 Pour supprimer un contrôle de cellule existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis**Retirer** le contrôle de cellule de la colonne spécifique en utilisant le**RemoveCellControl** méthode de**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Chaque colonne du**Colonnes** collecte de la**Feuille de travail** est représenté par une instance de**Aspose.Cells.GridDesktop.Data.GridColumn** classer.

{{% /alert %}}
