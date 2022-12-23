---
title: Public API Changements dans Aspose.Cells 8.1.1
type: docs
weight: 50
url: /fr/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.1.0 à 8.1.1, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la propriété HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions a exposé la propriété PresentationPreference qui peut être utilisée pour rendre les résultats avec une meilleure mise en page lors de l'exportation de feuilles de calcul vers HTML ou MHTML. La valeur par défaut est false. alors que s'il est défini sur true, le Aspose.Cells API exportera le contenu de la feuille de calcul avec une meilleure présentation.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Ajout de la prise en charge des scénarios de feuille de calcul**
 Un scénario est nommé modèle hypothétique qui inclut des cellules d'entrée variables liées entre elles par une ou plusieurs formules en conséquence. Aspose.Cells API a exposé la propriété Worksheet.Scenarios avec les classes suivantes afin de faciliter aux utilisateurs la création, la manipulation et la suppression de scénarios à partir de feuilles de calcul,

1. Scénario : représente un scénario individuel.
1. ScenarioCollection : représente une collection de scénarios.
1. ScenarioInputCellCollection : représente une liste de cellules d'entrée pour un scénario particulier.
1. ScenarioInputCell : représente une cellule d'entrée de la collection de cellules d'entrée pour un scénario particulier.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Comment créer, manipuler ou supprimer des scénarios des feuilles de travail](/cells/fr/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
