---
title: Travailler avec les événements Aspose.Cells.GridDesktop
type: docs
weight: 30
url: /fr/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, événement, événements
description: Cet article présente comment utiliser les événements dans GridDesktop.
---

{{% alert color="primary" %}} 

Les événements sont utilisés pour envoyer des notifications lorsqu'un changement survient dans un contrôle ou une classe. Aspose.Cells.GridDesktop possède plusieurs événements qui sont utilisés pour effectuer des tâches spécifiques lorsque certaines modifications surviennent dans le contrôle. Ce sujet fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridDesktop et explique comment gérer ces événements.

{{% /alert %}} 
## **Introduction**
Le contrôle Aspose.Cells.GridDesktop prend en charge plusieurs événements qui offrent un plus grand contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés. Ci-dessous se trouve une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Cette liste ne comprend pas les événements hérités par Aspose.Cells.GridDesktop de la classe Control.

{{% /alert %}} 

|**Evénements**|**Description**|
| :- | :- |
|BeforeCalculate| Se produit avant le calcul de la formule dans le classeur.|
|BeforeLoadFile| Se produit avant le chargement du classeur à partir du fichier.|
|ColumnHeaderClick| Se produit lorsque l'en-tête de colonne est cliqué.|
|ColumnHeaderDoubleClick| Se produit lorsque l'en-tête de colonne est double-cliqué.|
|CellDataChanged| Se produit lorsque les données ou la valeur à l'intérieur d'une cellule de la grille sont modifiées. Cet événement peut également être déclenché si la valeur d'une cellule est modifiée de manière programmée en utilisant la propriété Value ou la méthode SetCellValue d'un GridCell.|
|CellButtonClick|Se produit lorsque le bouton de la cellule est cliqué.|
|CellCheckedChanged|Se produit lorsque la propriété Checked de la case à cocher de la cellule est modifiée.|
|CellSelectedIndexChanged|Se produit lorsque la propriété SelectedIndex de la cellule de la liste déroulante est modifiée.|
|CellClick|Se produit lorsqu'une cellule de la grille est cliquée.|
|CellDoubleClick|Se produit lorsqu'une cellule de la grille est double-cliquée.|
|CellKeyPressed|Se produit lorsqu'une touche est enfoncée alors qu'une cellule a le focus. Si vous souhaitez créer un gestionnaire d'événement pour l'événement CellKeyPressed, définissez la propriété Handled de l'argument CellKeyEventArgs sur true pour empêcher le contrôle GridDesktop de gérer l'événement clavier.|
|AfterInsertColumns|Se produit lorsqu'une colonne est insérée. Vous pouvez obtenir l'index de la colonne en utilisant la propriété Index de l'argument Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|Se produit lorsqu'une ligne est insérée. Vous pouvez obtenir l'index de la ligne en utilisant la propriété Index de l'argument Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|FailLoadFile| Se produit en cas d'échec du chargement du classeur.|
|FinishCalculate|Se produit après le calcul de la formule dans le classeur.|
|FinishLoadFile|Se produit lorsque le classeur est chargé.|
|FocusedCellChanged|Se produit chaque fois que le focus d'une cellule est modifié.|
|RowHeaderClick|Se produit lorsque l'en-tête de ligne est cliqué.|
|RowHeaderDoubleClick|Se produit lorsque l'en-tête de ligne est double cliqué.|
|RowColumnHiddenChanged|Se produit lorsque l'état masqué de la ligne ou de la colonne est modifié.|
|SelectedSheetIndexChanged|Se produit lorsque l'utilisateur sélectionne une nouvelle feuille de calcul, c'est-à-dire lorsque la feuille sélectionnée change d'une feuille à une autre. Cet événement peut également être déclenché de manière programmée si la propriété ActiveSheetIndex du contrôle GridDesktop change.|
## **Gestion des événements de grille**
Pour effectuer une opération spécifique lorsqu'un événement spécifique est déclenché, créez un gestionnaire d'événements. Un gestionnaire d'événements effectue une tâche particulière lorsqu'un certain événement est déclenché. Ci-dessous, un gestionnaire d'événements est configuré pour gérer un événement simple de la grille à l'aide de Visual Studio.NET.

**Étape 1 : Sélection d'un événement du contrôle Aspose.Cells.GridDesktop**

1. Dans Visual Studio, sélectionnez le contrôle Aspose.Cells.GridDesktop et ouvrez sa boîte de dialogue **Propriétés**.
1. Cliquez sur l'onglet **Événements**.
1. Sélectionnez un événement. (pour cet exemple, l'événement **CellClick** est sélectionné).

**Étape 2: Création d'un gestionnaire d'événements**

1. Double-cliquez sur un événement sélectionné dans la boîte de dialogue **Propriétés**.
1. Lorsque l'événement est double-cliqué, un gestionnaire d'événements est créé par Visual Studio.NET. Voici le code généré par le concepteur qui montre qu'un événement est créé pour le contrôle GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Ajoutez maintenant du code pour effectuer l'opération souhaitée à l'intérieur du gestionnaire d'événements. Pour cet exemple, nous avons ajouté une ligne de code qui affiche une boîte de dialogue pour les notifications. 
Jetez un œil au gestionnaire d'événements que Visual Studio a ajouté à l'événement CellClick du contrôle GridDesktop. Il ressemblera à quelque chose comme le code ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Étape 3: Exécution de l'application**

1. Construisez et exécutez l'application.
1. Chaque fois qu'une cellule de grille est cliquée, une boîte de dialogue avec le message "La cellule est cliquée" apparaît.
