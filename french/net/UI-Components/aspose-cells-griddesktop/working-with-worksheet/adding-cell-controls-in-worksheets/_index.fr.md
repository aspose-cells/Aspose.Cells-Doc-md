---
title: Ajout de contrôles de cellules dans les feuilles de calcul
type: docs
weight: 120
url: /fr/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Cet article présente comment ajouter un contrôle dans une feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

Les contrôles de cellules sont en fait des contrôles qui peuvent être ajoutés aux feuilles de calcul. Nous les appelons **Contrôles de cellules** car ces contrôles sont affichés dans les cellules. Dans ce sujet, nous discuterons de l'ajout et de la gestion des événements de ces contrôles de cellules.

{{% /alert %}} 
## **Introduction**
Actuellement, Aspose.Cells.GridDesktop prend en charge l'ajout de trois types de contrôles de cellules, qui comprennent les éléments suivants :

- **Bouton**
- **Case à cocher**
- **Zone de liste déroulante**

Tous ces contrôles sont dérivés d'une classe abstraite, **CellControl**. Chaque feuille de calcul contient une collection de **Contrôles**. De nouveaux contrôles de cellules peuvent être ajoutés et les existants peuvent être accédés en utilisant cette collection de **Contrôles** facilement.

**IMPORTANT :** Si vous souhaitez ajouter des contrôles de cellules à toutes les cellules d'une colonne au lieu d'ajouter un par un, vous pouvez consulter [Gérer les contrôles de cellules dans les colonnes.](/cells/fr/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **Ajout d'un bouton**
Pour ajouter un bouton dans la feuille de calcul à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajouter le contrôle Aspose.Cells.GridDesktop à votre **Formulaire**
- Accéder à n'importe quelle **Feuille de calcul** désirée
- Ajouter un **Bouton** à la collection de **Contrôles** de la **Feuille de calcul**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Lors de l'ajout d'un **Bouton**, nous pouvons spécifier l'emplacement de la cellule (où l'afficher), la largeur et la hauteur et la légende du bouton.
#### **Gestion des événements du bouton**
Nous avons discuté de l'ajout du contrôle **Bouton** à la **Feuille de calcul** mais quel est l'avantage d'avoir simplement un bouton dans la feuille de calcul si nous ne pouvons pas l'utiliser. Ainsi, voici la nécessité de la gestion des événements du bouton.

Pour gérer l'événement **Clic** du contrôle **Bouton**, Aspose.Cells.GridDesktop fournit l'événement **CellButtonClick** qui doit être implémenté par les développeurs selon leurs besoins. Par exemple, nous avons simplement affiché un message lorsque le bouton est cliqué comme indiqué ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Spécifier une image d'arrière-plan pour le contrôle de bouton**
Nous pouvons définir une image d'arrière-plan pour le contrôle de bouton avec son libellé/texte comme indiqué dans le code ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANT:** Tous les événements des contrôles de cellules contiennent un argument **CellControlEventArgs** qui fournit les numéros de ligne et de colonne de la cellule contenant le contrôle de cellule (dont l'événement est déclenché).
### **Ajout de CheckBox**
Pour ajouter une case à cocher dans la feuille de calcul en utilisant Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous:

- Ajouter le contrôle Aspose.Cells.GridDesktop à votre **Formulaire**
- Accéder à n'importe quelle **Feuille de calcul** désirée
- Ajouter une **CheckBox** à la collection des **Contrôles** de la **Feuille de calcul**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Lors de l'ajout d'une **CheckBox**, nous pouvons spécifier l'emplacement de la cellule (où l'afficher) et l'état de la case à cocher.
#### **Gestion d'événements de la case à cocher**
Aspose.Cells.GridDesktop fournit un événement **CellCheckedChanged** qui est déclenché lorsque l'état **Checked** de la case à cocher est modifié. Les développeurs peuvent gérer cet événement selon leurs besoins. Par exemple, nous venons d'afficher un message pour montrer l'état **Checked** de la case à cocher dans le code ci-dessous:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Ajout de ComboBox**
Pour ajouter une combobox dans la feuille de calcul en utilisant Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous:

- Ajouter le contrôle Aspose.Cells.GridDesktop à votre **Formulaire**
- Accéder à n'importe quelle **Feuille de calcul** désirée
- Créer un tableau d'éléments (ou valeurs) qui seront ajoutés à la **ComboBox**
- Ajouter une **ComboBox** à la collection des **Contrôles** de la **Feuille de calcul** en spécifiant l'emplacement de la cellule (où la combobox sera affichée) et les éléments/valeurs qui seront affichés lorsque la combobox sera cliquée



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Gestion d'événements de la ComboBox**
Aspose.Cells.GridDesktop fournit un événement **CellSelectedIndexChanged** qui est déclenché lorsque l'**Index Sélectionné** de la combobox est modifié. Les développeurs peuvent gérer cet événement selon leurs désirs. Par exemple, nous venons d'afficher un message pour montrer l'**Élément Sélectionné** de la combobox:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
