---
title: Gérer les contrôles de cellules dans les feuilles de calcul
type: docs
weight: 130
url: /fr/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,contrôle de cellule,contrôle,contrôles
description: Cet article présente comment travailler avec les contrôles de cellules dans GridDesktop.
---

{{% alert color="primary" %}} 

Ce sujet aborde quelques concepts importants sur la gestion des contrôles de cellules en utilisant l'API de Aspose.Cells.GridDesktop. Nous expliquerons comment les développeurs peuvent accéder, modifier et supprimer des contrôles de cellules de leurs feuilles de calcul. Jetons un coup d'œil.

{{% /alert %}} 
## **Accéder aux contrôles de cellules**
Pour accéder et modifier un contrôle de cellule existant dans la feuille de calcul, les développeurs peuvent accéder à un contrôle de cellule spécifique à partir de la collection **Controls** de la **Worksheet** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéros de ligne et de colonne) dans laquelle le contrôle de cellule est affiché. Une fois qu'un contrôle de cellule est accessible, les développeurs peuvent modifier ses propriétés à l'exécution. Par exemple, dans l'exemple ci-dessous, nous avons accédé à un contrôle de cellule **CheckBox** existant à partir de la **Worksheet** et modifié sa propriété Checked.

**IMPORTANT :** La collection **Controls** contient tous les types de contrôles de cellules sous forme d'objets **CellControl**. Donc, si vous devez accéder à un type spécifique de contrôle de cellules, disons **CheckBox**, alors vous devrez convertir l'objet **CellControl** en classe **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Suppression des contrôles de cellules**
Pour supprimer un contrôle de cellule existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée et ensuite **supprimer** le contrôle de cellule de la collection **Controls** de la **Worksheet** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) contenant le contrôle de cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
