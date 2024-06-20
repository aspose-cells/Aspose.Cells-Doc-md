---
title: Ajout de contrôles de cellule dans les colonnes
type: docs
weight: 90
url: /fr/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Cet article présente comment ajouter un contrôle dans une colonne dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans nos discussions ultérieures, nous avons parlé de l'ajout et de la gestion des contrôles de cellules dans les feuilles de calcul. Mais en utilisant ces approches, nous pouvons ajouter des contrôles de cellules à une seule cellule à la fois. Et si quelqu'un voulait ajouter des contrôles de cellules à toutes les cellules d'une ou plusieurs colonnes? Dans de tels cas, pour réduire les efforts des développeurs, Aspose.Cells.GridDesktop offre la fonctionnalité d'ajouter des contrôles de cellules par colonne. Cela signifie que les développeurs ne peuvent sélectionner qu'une colonne souhaitée et spécifier un contrôle de cellule. Le contrôle de cellule spécifié sera ajouté à toutes les cellules de la colonne spécifiée. Voyons comment utiliser cette fonctionnalité.

{{% /alert %}} 
## **Introduction**
Actuellement, Aspose.Cells.GridDesktop prend en charge l'ajout de trois types de contrôles de cellules, qui comprennent les éléments suivants :

- **Bouton**
- **Case à cocher**
- **Zone de liste déroulante**

Tous ces contrôles sont dérivés d'une classe abstraite, **CellControl**.

**IMPORTANT:** Si vous souhaitez ajouter des contrôles de cellules à une seule cellule au lieu de toute la colonne, vous pouvez consulter [Ajouter des contrôles de cellules dans des feuilles de calcul.](/cells/fr/net/adding-cell-controls-in-worksheets/)
### **Ajout d'un bouton**
Pour ajouter des boutons dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajoutez un **Bouton** à une **Colonne** spécifiée de la **Feuille de travail**

**REMARQUE :** Lors de l'ajout du **Bouton**, nous pouvons spécifier la largeur, la hauteur et la légende du bouton.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Le snippet de code ci-dessus ajoute des boutons à toutes les cellules de la colonne spécifiée. Lorsqu'une cellule de cette colonne spécifique est sélectionnée, un bouton devient visible. Pour plus d'informations sur la gestion des événements des boutons, veuillez vous référer à la [Gestion des événements d'un contrôle de bouton.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Ajout de CheckBox**
Pour ajouter des cases à cocher dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajoutez une **Case à cocher** à une **Colonne** spécifiée de la **Feuille de travail**

**REMARQUE :** Lors de l'ajout de **CheckBox**, nous pouvons également spécifier l'état de la case à cocher.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Le snippet de code ci-dessus ajoute des cases à cocher à toutes les cellules de la colonne spécifiée. Pour plus d'informations sur la gestion des événements des cases à cocher, veuillez vous référer à la [Gestion des événements d'un contrôle de case à cocher.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Ajout de ComboBox**
Pour ajouter des zones de liste déroulante dans une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Créez un tableau d'éléments (ou valeurs) qui seront ajoutés à la **Zone de liste déroulante**
- Ajoutez une **Zone de liste déroulante** (contenant des éléments ou valeurs) à une **Colonne** spécifiée de la **Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Le snippet de code ci-dessus ajoute des zones de liste déroulante à toutes les cellules de la colonne spécifiée. Lorsqu'une cellule de cette colonne spécifique est sélectionnée, une zone de liste déroulante devient visible. Pour plus d'informations sur la gestion des événements des zones de liste déroulante, veuillez vous référer à la [Gestion des événements d'un contrôle de zones de liste déroulante.](/cells/fr/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
