---
title: Gestion des contrôles Cell dans les feuilles de calcul
type: docs
weight: 130
url: /fr/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Cette rubrique aborde certains concepts importants concernant la gestion des contrôles de cellule à l'aide du API de Aspose.Cells.GridDesktop. Nous expliquerons comment les développeurs peuvent accéder, modifier et supprimer les contrôles de cellule de leurs feuilles de calcul. Jetons-y un œil.

{{% /alert %}} 
## **Accès aux commandes Cell**
 Pour accéder à un contrôle de cellule existant dans la feuille de calcul et le modifier, les développeurs peuvent accéder à un contrôle de cellule spécifique à partir du**Les contrôles** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéros de ligne et de colonne) dans laquelle le contrôle de cellule est affiché. Une fois qu'un contrôle de cellule est accédé, les développeurs peuvent modifier ses propriétés lors de l'exécution. Pour une instance, dans l'exemple ci-dessous, nous avons accédé à une instance existante**Case à cocher** contrôle des cellules à partir du**Feuille de travail** et modifié sa propriété Checked.

**IMPORTANT:** **Les contrôles** collection contient tous les types de contrôles de cellule sous la forme de**CellControl** objets. Donc, si vous avez besoin d'accéder à un type spécifique de contrôle de cellule, dites**Case à cocher** alors vous devrez transtyper le**CellControl** s'opposer à**Case à cocher** classer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Retrait des commandes Cell**
 Pour supprimer un contrôle de cellule existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis**Retirer** le contrôle de la cellule de la**Les contrôles** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) contenant le contrôle de cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
