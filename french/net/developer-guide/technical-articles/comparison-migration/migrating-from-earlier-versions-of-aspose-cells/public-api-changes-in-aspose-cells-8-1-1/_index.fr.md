---
title: Changements d API public dans Aspose.Cells 8.1.1
type: docs
weight: 50
url: /fr/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.1.0 à la version 8.1.1, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes et mises à jour publiques, mais aussi une description de tout changement dans le comportement en coulisses d'Aspose.Cells.

{{% /alert %}} 
## **Ajout de la propriété HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions a exposé la propriété PresentationPreference qui peut être utilisée pour rendre les résultats avec une meilleure mise en page lors de l'exportation de feuilles de calcul en HTML ou MHTML. La valeur par défaut est false. alors que si elle est définie sur true, l'API Aspose.Cells exportera le contenu de la feuille de calcul avec une meilleure présentation.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Prise en charge ajoutée pour les scénarios de feuille de calcul**
Un scénario est un modèle de simulation qui inclut des cellules d'entrée variables liées par une ou plusieurs formules en conséquence. L'API Aspose.Cells a exposé la propriété Worksheet.Scenarios ainsi que les classes suivantes afin de faciliter la création, la manipulation et la suppression de scénarios à partir de feuilles de calcul, 

1. Scénario: Représente un scénario individuel.
1. ScenarioCollection: Représente une collection de scénarios.
1. ScenarioInputCellCollection: Représente une liste de cellules d'entrée pour un scénario particulier.
1. ScenarioInputCell: Représente une cellule d'entrée de la collection de cellules d'entrée pour un scénario particulier.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Comment créer, manipuler ou supprimer des scénarios à partir de feuilles de calcul](/cells/fr/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
