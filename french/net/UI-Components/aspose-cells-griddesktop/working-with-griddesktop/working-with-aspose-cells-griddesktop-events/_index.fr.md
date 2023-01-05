---
title: Utilisation des événements Aspose.Cells.GridDesktop
type: docs
weight: 30
url: /fr/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Les événements sont utilisés pour envoyer des notifications lorsqu'un changement se produit dans un contrôle ou une classe. Aspose.Cells.GridDesktop a plusieurs événements qui sont utilisés pour effectuer des tâches spécifiques lorsque certains changements se produisent dans le contrôle. Cette rubrique fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridDesktop et explique comment gérer ces événements.

{{% /alert %}} 
## **Introduction**
Le contrôle Aspose.Cells.GridDesktop prend en charge plusieurs événements qui offrent plus de contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés. Vous trouverez ci-dessous une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Cette liste n'inclut pas les événements hérités par Aspose.Cells.GridDesktop de la classe Control.

{{% /alert %}} 

|**Événements**|**Description**|
|:- |:- |
|AvantCalculer|Se produit avant la formule de calcul dans le classeur.|
|AvantChargerFichier|Se produit avant le chargement du classeur à partir du fichier.|
|Clic sur l'en-tête de la colonne|Se produit lorsque l'en-tête de colonne est cliqué.|
|ColumnHeaderDoubleClick|Se produit lorsque l'en-tête de colonne est double-cliqué.|
|CellDataChanged|Se produit lorsque les données ou la valeur à l'intérieur d'une cellule de grille sont modifiées. Cet événement peut également être déclenché si la valeur d'une cellule est modifiée par programmation à l'aide de la propriété Value ou de la méthode SetCellValue d'un GridCell.|
|ClicBoutonCellule|Se produit lorsque le bouton de la cellule est cliqué.|
|CelluleVérifiéeModifiée|Se produit lorsque la case à cocher de la propriété cochée de la cellule est modifiée.|
|CellSelectedIndexChanged|Se produit lorsque la propriété SelectedIndex de la zone de liste déroulante des cellules est modifiée.|
|CellClick|Se produit lorsqu'une cellule de grille est cliquée.|
|DoubleClicCellule|Se produit lorsqu'une cellule de grille est double-cliquée.|
|CellKeyPressed|Se produit lorsqu'une touche est enfoncée alors qu'une cellule a le focus. Si vous souhaitez créer un gestionnaire d'événements pour l'événement CellKeyPressed, définissez la propriété Handled de l'argument CellKeyEventArgs sur true pour empêcher le contrôle GridDesktop de gérer l'événement key.|
|AprèsInsérerColonnes|Se produit lorsqu'une colonne est insérée. Vous pouvez obtenir l'index de colonne en utilisant la propriété Index de l'argument Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|Se produit lorsqu'une ligne est insérée. Vous pouvez obtenir l'index de ligne en utilisant la propriété Index de l'argument Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|ÉchecChargerFichier|Se produit lorsque le chargement du classeur échoue.|
|TerminerCalculer|Se produit après la formule de calcul dans le classeur.|
|TerminerChargerFichier|Se produit lorsque le classeur est chargé.|
|FocusedCellChanged|Se produit chaque fois que le focus d'une cellule est modifié.|
|RowHeaderClick|Se produit lorsque l'en-tête de ligne est cliqué.|
|RowHeaderDoubleClick|Se produit lorsque l'en-tête de ligne est double-cliqué.|
|RowColumnHiddenChanged|Se produit lorsque l'état masqué de la ligne ou de la colonne est modifié.|
|SelectedSheetIndexChanged|Se produit lorsqu'un utilisateur sélectionne une nouvelle feuille de calcul, c'est-à-dire lorsque la feuille sélectionnée passe d'une feuille de calcul à une autre. Cet événement peut également être déclenché par programme si la propriété ActiveSheetIndex du contrôle GridDesktop change.|
## **Gestion des événements de grille**
Pour effectuer une opération spécifique lorsqu'un événement spécifique est déclenché, créez un gestionnaire d'événements. Un gestionnaire d'événements exécute une tâche particulière lorsqu'un certain événement est déclenché. Ci-dessous, un gestionnaire d'événements est configuré pour gérer un événement Grid simple à l'aide de Visual Studio.NET.

**Étape 1 : Sélection d'un événement de Aspose.Cells.GridDesktop Control**

1. Dans Visual Studio, sélectionnez le contrôle Aspose.Cells.GridDesktop et ouvrez son**Propriétés** dialogue.
1.  Clique le**Événements** languette.
1.  Sélectionnez un événement. (pour cet exemple, le**CellClick** l'événement est sélectionné).

**Étape 2 : Création d'un gestionnaire d'événements**

1.  Double-cliquez sur un événement sélectionné dans le**Propriétés** dialogue.
1. Lorsque l'événement est double-cliqué, un gestionnaire d'événements est créé par Visual Studio.NET. Voici le code généré par le concepteur qui montre qu'un événement est créé pour le GridControl Control.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Maintenant, ajoutez du code pour effectuer l'opération souhaitée dans le gestionnaire d'événements. Pour cet exemple, nous avons ajouté une ligne de code qui affiche une boîte de message pour les notifications.
Examinez le gestionnaire d'événements que Visual Studio a ajouté à l'événement CellClick du contrôle GridDesktop. Cela ressemblera à quelque chose comme le code ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Étape 3 : Exécution de l'application**

1. Créez et exécutez l'application.
1. Chaque fois qu'une cellule de la grille est cliquée, une boîte de message avec le message "Cell est cliqué" apparaît.
