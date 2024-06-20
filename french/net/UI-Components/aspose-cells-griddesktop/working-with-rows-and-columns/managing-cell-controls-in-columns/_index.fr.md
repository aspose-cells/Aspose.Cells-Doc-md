---
title: Gestion des contrôles de cellules dans les colonnes
type: docs
weight: 100
url: /fr/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, contrôles, contrôle
description: Cet article présente comment définir un contrôle dans une colonne GridDesktop.
---

{{% alert color="primary" %}} 

Ce sujet aborde certains concepts importants concernant la gestion des contrôles de cellules dans les colonnes à l'aide de l'API Aspose.Cells.GridDesktop. Nous expliquerons comment les développeurs peuvent accéder, modifier et supprimer les contrôles de cellules des colonnes de leurs feuilles de calcul. Jetons-y un coup d'œil.

{{% /alert %}} 
## **Accéder aux contrôles de cellules**
Pour accéder et modifier un contrôle de cellule existant dans la colonne, les développeurs peuvent utiliser la propriété CellControl d'un **Aspose.Cells.GridDesktop.Data.GridColumn**. Une fois qu'un contrôle de cellule est accédé, les développeurs peuvent modifier ses propriétés à l'exécution. Par exemple, dans l'exemple ci-dessous, nous avons accédé à un **CheckBox** existant dans une **Aspose.Cells.GridDesktop.Data.GridColumn** spécifique et modifié sa propriété Checked.

**IMPORTANT :** La propriété CellControl fournit un contrôle de cellule sous forme d'objet **CellControl**. Ainsi, si vous avez besoin d'accéder à un type spécifique de contrôle de cellule, disons **CheckBox**, alors vous devrez convertir l'objet **CellControl** en classe **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Suppression des contrôles de cellules**
Pour supprimer un contrôle de cellule existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée et ensuite **supprimer** le contrôle de cellule de la colonne spécifique en utilisant la méthode **RemoveCellControl** de **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Chaque colonne dans la collection **Colonnes** de la **Feuille de calcul** est représentée par une instance de la classe **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{% /alert %}}
