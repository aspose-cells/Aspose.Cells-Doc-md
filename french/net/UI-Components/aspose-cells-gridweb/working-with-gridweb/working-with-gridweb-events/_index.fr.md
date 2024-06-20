---
title: Travailler avec les événements de GridWeb
type: docs
weight: 70
url: /fr/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb, événements, événement
description: Cet article présente comment travailler avec différents types d événements dans GridWeb.
---

{{% alert color="primary" %}} 

Tous les programmeurs doivent être familiers avec les événements et leur but. Les événements sont utilisés pour envoyer des notifications des changements qui peuvent survenir dans un contrôle ou une classe. Aspose.Cells.GridWeb dispose de plusieurs événements qui peuvent être utilisés pour effectuer des tâches spécifiques lorsque certains changements se produisent dans le contrôle.

Ce sujet fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridWeb ainsi que des détails sur la manière de gérer ces événements.

{{% /alert %}} 
## **Travailler avec les événements de Grid**
### **Introduction aux événements de grille**
Le contrôle Aspose.Cells.GridWeb prend en charge plusieurs événements qui offrent davantage de contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés dans le contrôle. Une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridWeb peut être trouvée ci-dessous.

{{% alert color="primary" %}} 

Cette liste n'inclut pas les événements hérités par Aspose.Cells.GridWeb de la classe Control.

{{% /alert %}} 

|**Événements** |**Description** |
| :- | :- |
|CellCommand | Se déclenche lorsque le lien de commande d'une cellule est cliqué. Lorsque cet événement est déclenché, son paramètre e.Argument fournit le nom de la commande. |
|CellDoubleClick | Se déclenche lorsque la cellule est double-cliquée. |
|CellError | Se déclenche lorsque la valeur d'entrée d'une cellule contient une erreur. |
|ColumnDeleted |Se produit lorsqu'un utilisateur supprime une colonne d'une feuille de calcul à l'aide du menu côté client. |
|ColumnDeleting |Se produit lorsqu'un utilisateur essaie de supprimer une colonne d'une feuille de calcul à l'aide du menu côté client. |
|ColumnDoubleClick |Se produit lorsque l'en-tête de colonne est double-cliqué. |
|ColumnInserted |Se produit lorsqu'un utilisateur insère une colonne dans une feuille de calcul à l'aide du menu côté client. |
|CustomCommand |Se produit lorsqu'un utilisateur clique sur un bouton de commande personnalisé. |
|LoadCustomData |Se produit lorsque la propriété EnableSession du contrôle est définie sur false et que les données de la feuille de calcul doivent être chargées. Vous pouvez gérer cet événement en mode sans session pour charger les données de la feuille de calcul à partir d'un fichier ou d'une base de données. |
|PageIndexChanged |Se produit lorsque l'index de la page de feuille du contrôle est modifié. |
|RowDeleted |Se produit lorsqu'un utilisateur supprime une ligne d'une feuille de calcul à l'aide du menu côté client. |
|RowDeleting |Se produit lorsqu'un utilisateur essaie de supprimer une ligne d'une feuille de calcul à l'aide du menu côté client. |
|RowDoubleClick |Se produit lorsque l'en-tête de ligne est double-cliqué. |
|RowInserted |Se produit lorsqu'un utilisateur insère une ligne dans une feuille de calcul à l'aide du menu côté client. |
|SaveCommand |Se produit lorsque le bouton **Enregistrer** est cliqué. |
|SheetDataUpdated |Se produit lorsque le contrôle a chargé les données postées et mis à jour les données de la feuille de calcul. |
|SheetTabClick |Se produit lorsqu'un onglet de feuille est cliqué. |
|SubmitCommand |Se produit lorsque le bouton **Soumettre** est cliqué. |
|UndoCommand |Se produit lorsque le bouton **Annuler** est cliqué. |
|AjaxCallFinished |Se déclenche lorsque la mise à jour AJAX du contrôle est terminée (EnableAJAX doit être défini sur true). |
|CellModifiedOnAjax |Se déclenche lorsque la cellule est modifiée dans l'appel AJAX. |
|OnAfterColumnFilter |Se déclenche après l'application du filtre sur une colonne. |
|OnBeforeColumnFilter |Se déclenche avant l'application du filtre sur une colonne. |
## **Gestion des événements de grille**
Pour exécuter une opération spécifique lors de la déclenchement d'un événement spécifique, on doit créer un gestionnaire d'événement. Un gestionnaire d'événement réalise la tâche désirée lorsqu'un certain événement est déclenché. Les étapes illustrées ci-dessous montrent comment gérer un événement de grille simple en utilisant Visual Studio.
### **Étape 1 : Sélection de un événement du contrôle Aspose.Cells.GridWeb**
1. Sélectionnez le contrôle Aspose.Cells.GridWeb et ouvrez sa boîte de dialogue Propriétés sur le côté droit.
1. Cliquez sur le bouton **Onglet Événements**.
1. Sélectionnez un événement.
   Pour cet exemple, l'événement SaveCommand est sélectionné.
### **Étape 2 : Création d'un gestionnaire d'événement**
1. Double-cliquez sur un événement dans la boîte de dialogue Propriétés. 

   **Double-cliquer sur un événement sélectionné** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




Lorsque l'événement est double-cliqué, un gestionnaire d'événement est automatiquement créé par Visual Studio. 

**Un gestionnaire d'événement créé par Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Ajoutez du code pour effectuer une action à l'intérieur du gestionnaire d'événement.

Ici, une seule ligne de code qui enregistre le contenu de la grille dans un fichier Excel lorsque le bouton **Enregistrer** est cliqué a été ajoutée.

Pour obtenir plus d'informations, déplacez le curseur au-dessus pour voir du code, vous découvrirez alors que Visual Studio est suffisamment intelligent pour ajouter un gestionnaire d'événement à l'événement SaveCommand de GridWeb.
### **Étape 3 : Exécution de votre application**
1. Construisez et exécutez l'application.
1. Cliquez sur **Enregistrer**.

Le contenu de la grille est enregistré dans un fichier Excel. 

**Application en mode exécution** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
