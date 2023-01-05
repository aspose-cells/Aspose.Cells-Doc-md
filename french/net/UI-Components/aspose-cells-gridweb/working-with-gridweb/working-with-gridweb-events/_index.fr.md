---
title: Utilisation des événements GridWeb
type: docs
weight: 70
url: /fr/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Tous les programmeurs doivent être familiarisés avec les événements et leur objectif. Les événements sont utilisés pour envoyer des notifications de modifications pouvant survenir dans un contrôle ou une classe. Aspose.Cells.GridWeb a plusieurs événements qui peuvent être utilisés pour effectuer des tâches spécifiques lorsque certains changements se produisent dans le contrôle.

Cette rubrique fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridWeb ainsi que des détails sur la façon de gérer ces événements.

{{% /alert %}} 
## **Utilisation des événements de grille**
### **Introduction aux événements de grille**
Aspose.Cells.Le contrôle GridWeb prend en charge plusieurs événements qui offrent plus de contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés dans le contrôle. Vous trouverez ci-dessous une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Cette liste n'inclut pas les événements hérités par Aspose.Cells.GridWeb de la classe Control.

{{% /alert %}} 

|**Événements** |**Description** |
|:- |:- |
| CellCommand| Se produit lorsque le lien hypertexte de commande d'une cellule est cliqué. Lorsque cet événement est déclenché, son paramètre e.Argument fournit le nom de la commande.|
| DoubleClicCellule| Se produit lorsque la cellule est double-cliquée.|
| CellErreur| Se produit lorsque la valeur d'entrée d'une cellule comporte une erreur.|
| ColonneSupprimée|Se produit lorsqu'un utilisateur supprime une colonne d'une feuille de calcul à l'aide du menu côté client.|
| ColonneSuppression| Se produit lorsqu'un utilisateur tente de supprimer une colonne d'une feuille de calcul à l'aide du menu côté client.|
| ColonneDoubleClic| Se produit lorsque l'en-tête de colonne est double-cliqué.|
| ColonneInsérée| Se produit lorsqu'un utilisateur insère une colonne dans une feuille de calcul à l'aide du menu côté client.|
| Commande personnalisée| Se produit lorsqu'un utilisateur clique sur un bouton de commande personnalisé.|
| ChargerDonnéesPersonnalisées| Se produit lorsque la propriété EnableSession du contrôle est définie sur false et doit charger des données de feuille de calcul. Vous pouvez gérer cet événement en mode sans session pour charger des données de feuille de calcul à partir d'un fichier ou d'une base de données.|
| PageIndexChanged| Se produit lorsque l'index de page de feuille du contrôle est modifié.|
| LigneSupprimée| Se produit lorsqu'un utilisateur supprime une ligne d'une feuille de calcul à l'aide du menu côté client.|
| Suppression de ligne| Se produit lorsqu'un utilisateur essaie de supprimer une ligne d'une feuille de calcul à l'aide du menu côté client.|
| LigneDoubleClic|Se produit lorsque l'en-tête de ligne est double-cliqué.|
| LigneInsérée| Se produit lorsqu'un utilisateur insère une ligne dans une feuille de calcul à l'aide du menu côté client.|
| Enregistrer la commande| Se produit lorsque le**Sauver** bouton est cliqué.|
| SheetDataUpdated| Se produit lorsque le contrôle a chargé les données publiées et mis à jour les données de la feuille de calcul.|
| SheetTabClick| Se produit lorsqu'un onglet de feuille est cliqué.|
| SoumettreCommande| Se produit lorsque le**Nous faire parvenir** bouton est cliqué.|
| Annuler la commande| Se produit lorsque le**annuler** bouton est cliqué.|
| AjaxAppelTerminé| Se déclenche lorsque la mise à jour AJAX du contrôle est terminée. (EnableAJAX doit être défini sur true).|
| CellModifiedOnAjax| Se déclenche lorsque la cellule est modifiée dans un appel AJAX.|
| SurAprèsFiltreColonne| Se déclenche après l'application du filtre sur une colonne.|
| OnBeforeColumnFilter| Se déclenche avant que le filtre ne soit appliqué sur une colonne.|
## **Gestion des événements de grille**
Pour effectuer une opération spécifique lors du déclenchement d'un événement spécifique, nous devons créer un gestionnaire d'événements. Un gestionnaire d'événements exécute la tâche souhaitée lorsqu'un certain événement est déclenché. Les étapes illustrées ci-dessous montrent comment gérer un événement de grille simple à l'aide de Visual Studio.
### **Étape 1 : Sélection d'un événement de Aspose.Cells.GridWeb Control**
1. Sélectionnez le contrôle Aspose.Cells.GridWeb et ouvrez sa boîte de dialogue Propriétés sur le côté droit.
1.  Clique le**Onglet Événements** bouton.
1. Sélectionnez un événement.
 Pour cet exemple, l'événement SaveCommand est sélectionné.
### **Étape 2 : Création d'un gestionnaire d'événements**
1.  Double-cliquez sur un événement dans la boîte de dialogue Propriétés.

   **Double-cliquer sur un événement sélectionné** 

![tâche : image_autre_texte](working-with-gridweb-events_1.png)




 Lorsque l'événement est double-cliqué, un gestionnaire d'événements est automatiquement créé par Visual Studio.

**Un gestionnaire d'événements créé par Visual Studio** 

![tâche : image_autre_texte](working-with-gridweb-events_2.png)




1. Ajoutez du code pour effectuer une action dans le gestionnaire d'événements.

 Ici, une seule ligne de code qui enregistre le contenu de la grille dans un fichier Excel lorsque le**Sauver** bouton est cliqué a été ajouté.

Pour obtenir plus d'informations, déplacez le curseur ci-dessus pour voir du code, puis vous découvrirez que Visual Studio est suffisamment intelligent pour ajouter un gestionnaire d'événements à l'événement SaveCommand de GridWeb.
### **Étape 3 : Lancer votre application**
1. Créez et exécutez l'application.
1.  Cliquez sur**Sauver**.

 Le contenu de la grille est enregistré dans un fichier Excel.

**Application en mode exécution** 

![tâche : image_autre_texte](working-with-gridweb-events_3.png)
