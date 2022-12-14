---
title: Ajout de contrôles Cell dans les colonnes
type: docs
weight: 90
url: /fr/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Dans nos discussions ultérieures, nous avons discuté de l'ajout et de la gestion des contrôles de cellule dans la feuille de calcul. Mais, en utilisant ces approches, nous pouvons ajouter des contrôles de cellule à des cellules individuelles une par une. Que se passe-t-il si quelqu'un souhaite ajouter des contrôles de cellule à toutes les cellules d'une ou plusieurs colonnes ? Dans de tels cas, pour réduire les efforts des développeurs, Aspose.Cells.GridDesktop offre la possibilité d'ajouter des contrôles de cellule par colonne. Cela signifie que les développeurs ne peuvent sélectionner qu'une colonne souhaitée et spécifier n'importe quel contrôle de cellule. Le contrôle de cellule spécifié sera ajouté à toutes les cellules de la colonne spécifiée. Voyons comment pouvons-nous utiliser cette fonctionnalité.

{{% /alert %}} 
## **Introduction**
Actuellement, Aspose.Cells.GridDesktop prend en charge l'ajout de trois types de contrôles de cellule, notamment :

- **Bouton**
- **Case à cocher**
- **Boîte combo**

 Tous ces contrôles sont dérivés d'une classe abstraite,**CellControl**.

**IMPORTANT:** Si vous souhaitez ajouter des contrôles de cellule à une seule cellule au lieu de toute la colonne, vous pouvez vous référer à[Ajout de contrôles Cell dans les feuilles de calcul.](/cells/fr/net/adding-cell-controls-in-worksheets/)
### **Ajouter un bouton**
Pour ajouter des boutons dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Bouton** à tout spécifié**Colonne** de la**Feuille de travail**

**REMARQUE:** En ajoutant**Bouton**, nous pouvons spécifier la largeur, la hauteur et la légende du bouton.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 L'extrait de code ci-dessus ajoute des boutons à toutes les cellules de la colonne spécifiée. Chaque fois qu'une cellule de cette colonne spécifique est sélectionnée, un bouton devient visible. Pour plus d'informations sur la gestion des événements des boutons, reportez-vous au[Gestion des événements d'un contrôle bouton.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Ajout d'une case à cocher**
Pour ajouter des cases à cocher dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Case à cocher** à tout spécifié**Colonne** de la**Feuille de travail**

**REMARQUE:** En ajoutant**Case à cocher**, nous pouvons également spécifier l'état de la case à cocher.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 L'extrait de code ci-dessus ajoute des cases à cocher à toutes les cellules de la colonne spécifiée. Pour plus d'informations sur la gestion des événements des cases à cocher, reportez-vous au[Gestion des événements d'un contrôle CheckBox.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Ajout d'un ComboBox**
Pour ajouter des listes déroulantes dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Créez un tableau d'éléments (ou de valeurs) qui seront ajoutés à**Boîte combo**
-  Ajouter**Boîte combo** (contenant des éléments ou des valeurs) à tout spécifié**Colonne** de la**Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 L'extrait de code ci-dessus ajoute des listes déroulantes à toutes les cellules de la colonne spécifiée. Chaque fois qu'une cellule de cette colonne spécifique est sélectionnée, une liste déroulante devient visible. Pour plus d'informations sur la gestion des événements des listes déroulantes, reportez-vous au[Gestion des événements d'un contrôle ComboBox.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
