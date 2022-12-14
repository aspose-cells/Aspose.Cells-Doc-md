---
title: Ajout de contrôles Cell dans les feuilles de calcul
type: docs
weight: 120
url: /fr/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 Les contrôles Cell sont en fait les contrôles qui peuvent être ajoutés aux feuilles de calcul. Nous les appelons**Cell Commandes** car ces contrôles sont affichés dans des cellules. Dans cette rubrique, nous discuterons de l'ajout et de la gestion des événements de ces contrôles de cellule.

{{% /alert %}} 
## **Introduction**
Actuellement, Aspose.Cells.GridDesktop prend en charge l'ajout de trois types de contrôles de cellule, notamment :

- **Bouton**
- **Case à cocher**
- **Boîte combo**

Tous ces contrôles sont dérivés d'une classe abstraite,**CellControl**. Chaque feuille de travail contient une collection de**Les contrôles**De nouveaux contrôles de cellule peuvent être ajoutés et les contrôles existants sont accessibles à l'aide de cette**Les contrôles**collecte facilement.

**IMPORTANT:**Si vous souhaitez ajouter des contrôles de cellule à toutes les cellules d'une colonne au lieu d'en ajouter une par une, vous pouvez vous référer à[Gestion des contrôles Cell en colonnes.](/cells/fr/net/adding-cell-controls-in-worksheets/)
### **Ajouter un bouton**
Pour ajouter un bouton dans la feuille de calcul à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
- Accédez à tout**Feuille de travail**
- Ajouter**Bouton**au**Les contrôles**collecte de la**Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


En ajoutant**Bouton**, nous pouvons spécifier l'emplacement de la cellule (où l'afficher), la largeur et la hauteur et la légende du bouton.
#### **Gestion des événements du bouton**
Nous avons discuté de l'ajout**Bouton**contrôle à la**Feuille de travail**mais quel est l'avantage d'avoir juste un bouton dans la feuille de calcul si nous ne pouvons pas l'utiliser. Donc, voici le besoin de gestion des événements du bouton.

Pour gérer le**Cliquez sur**événement de la**Bouton**contrôle, Aspose.Cells.GridDesktop fournit**ClicBoutonCellule**événement qui devrait être mis en œuvre par les développeurs en fonction de leurs besoins. Pour une instance, nous venons d'afficher un message lorsque le bouton est cliqué comme indiqué ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Spécification d'une image d'arrière-plan pour le contrôle de bouton**
Nous pouvons définir une image/image d'arrière-plan pour le contrôle du bouton avec son étiquette/texte comme indiqué dans le code ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANT:**Tous les événements des contrôles de cellule contiennent un**CellControlEventArgsCellControlEventArgs**argument qui fournit les numéros de ligne et de colonne de la cellule qui contient le contrôle de cellule (dont l'événement est déclenché).
### **Ajout d'une case à cocher**
Pour ajouter une case à cocher dans la feuille de calcul à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
- Accédez à tout**Feuille de travail**
- Ajouter**Case à cocher**au**Les contrôles**collecte de la**Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


En ajoutant**Case à cocher**, nous pouvons spécifier l'emplacement de la cellule (où l'afficher) et l'état de la case à cocher.
#### **Gestion des événements de CheckBox**
Aspose.Cells.GridDesktop fournit**CelluleVérifiéeModifiée**événement qui se déclenche lorsque le**Vérifié**l'état de la case à cocher est modifié. Les développeurs peuvent gérer cet événement en fonction de leurs besoins. Pour une instance, nous venons d'afficher un message pour montrer le**Vérifié**état de la case à cocher dans le code ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Ajout d'un ComboBox**
Pour ajouter une zone de liste déroulante dans la feuille de calcul à l'aide de Aspose.Cells.GridDesktop , veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
- Accédez à tout**Feuille de travail**
- Créez un tableau d'éléments (ou de valeurs) qui seront ajoutés à**Boîte combo**
- Ajouter**Boîte combo**au**Les contrôles**collecte de la**Feuille de travail**en spécifiant l'emplacement de la cellule (où la combobox sera affichée) et les éléments/valeurs qui seront affichés lorsque la combobox sera cliqué



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Gestion des événements de ComboBox**
Aspose.Cells.GridDesktop fournit**CellSelectedIndexChanged**événement qui se déclenche lorsque le**Index sélectionné**de combobox est modifié. Les développeurs peuvent gérer cet événement selon leurs envies. Pour une instance, nous venons d'afficher un message pour montrer le**Élément sélectionné**de la combobox :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
