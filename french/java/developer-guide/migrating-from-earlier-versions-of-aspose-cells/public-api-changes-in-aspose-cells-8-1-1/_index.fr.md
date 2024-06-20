---
title: Changements d API public dans Aspose.Cells 8.1.1
type: docs
weight: 60
url: /fr/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.1.0 à 8.1.1, qui peuvent intéresser les développeurs de modules et d'applications. Il comprend non seulement les [nouvelles méthodes publiques ajoutées et mises à jour](/cells/fr/java/public-api-changes-in-aspose-cells-8-1-1/), mais également une description de [tous les changements de comportement](/cells/fr/java/public-api-changes-in-aspose-cells-8-1-1/) en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **Propriétés et fonctionnalités ajoutées**
### **Propriété HtmlSaveOptions.PresentationPreference ajoutée**
La classe HtmlSaveOptions a exposé un getter/setter pour la propriété PresentationPreference qui peut être utilisée pour rendre les résultats avec une meilleure mise en page lors de l'exportation des feuilles de calcul au format HTML ou MHTML. La valeur par défaut est false, tandis que si elle est définie sur true, l'API Aspose.Cells exporte le contenu de la feuille de calcul avec une meilleure présentation.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Prise en charge ajoutée pour les scénarios de feuille de calcul**
Un scénario est un modèle de simulation qui comprend des cellules d'entrée variables liées par une ou plusieurs formules. Aspose.Cells a exposé un getter et un setter pour la propriété Worksheet.Scenarios ainsi que les classes suivantes pour aider les développeurs à créer, manipuler et supprimer des scénarios.

1. Scénario: Représente un scénario individuel.
1. ScenarioCollection: Représente une collection de scénarios.
1. ScenarioInputCellCollection: Représente une liste de cellules d'entrée pour un scénario particulier.
1. ScenarioInputCell: Représente une cellule d'entrée de la collection de cellules d'entrée pour un scénario particulier.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Comment créer, manipuler ou supprimer des scénarios des feuilles de calcul](/cells/fr/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Changement de comportement pour CellsException**
Avec les versions précédentes de l'API Aspose.Cells for Java, lorsqu'une feuille de calcul potentiellement endommagée était chargée dans une instance de Workbook, l'API avait tendance à générer un message générique sans mentionner où se situait le problème. Nous avons modifié ce comportement pour 8.1.1 afin que l'API génère une exception avec un message significatif qui indique où (quelle cellule) et quoi (expression de formule) cause l'exception lors de la lecture du fichier modèle.
