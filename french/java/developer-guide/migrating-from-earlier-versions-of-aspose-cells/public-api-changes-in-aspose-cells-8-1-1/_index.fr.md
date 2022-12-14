---
title: Public API Changements dans Aspose.Cells 8.1.1
type: docs
weight: 60
url: /fr/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.1.0 à 8.1.1, qui peuvent intéresser les développeurs de modules et d'applications. Il comprend non seulement[méthodes publiques nouvelles et mises à jour](/cells/fr/java/public-api-changes-in-aspose-cells-8-1-1/) , mais aussi une description de tout[changements dans le comportement](/cells/fr/java/public-api-changes-in-aspose-cells-8-1-1/) dans les coulisses au Aspose.Cells.

{{% /alert %}} 
## **Propriétés et fonctionnalités ajoutées**
### **Ajout de la propriété HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions a exposé la propriété getter/setter pour PresentationPreference qui peut être utilisée pour rendre les résultats avec une meilleure mise en page lors de l'exportation de feuilles de calcul au format HTML ou MHTML. La valeur par défaut est faux. alors que s'il est défini sur true, le Aspose.Cells API exporte le contenu de la feuille de calcul avec une meilleure présentation.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Ajout de la prise en charge des scénarios de feuille de calcul**
Un scénario est un modèle hypothétique qui inclut des cellules d'entrée variables liées entre elles par une ou plusieurs formules. Aspose.Cells a exposé un getter et un setter pour la propriété Worksheet.Scenarios ainsi que les classes suivantes pour aider les développeurs à créer, manipuler et supprimer des scénarios.

1. Scénario : représente un scénario individuel.
1. ScenarioCollection : représente une collection de scénarios.
1. ScenarioInputCellCollection : représente une liste de cellules d'entrée pour un scénario particulier.
1. ScenarioInputCell : représente une cellule d'entrée de la collection de cellules d'entrée pour un scénario particulier.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Comment créer, manipuler ou supprimer des scénarios des feuilles de travail](/cells/fr/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Changement de comportement pour CellsException**
Avec les versions précédentes du Aspose.Cells for Java API, lorsqu'une feuille de calcul éventuellement endommagée était chargée dans une instance de Workbook, le API avait tendance à lancer un message générique sans mentionner d'où pouvait provenir le problème. Nous avons modifié ce comportement pour 8.1.1 afin que le API lève une exception avec un message significatif qui indique où (quelle cellule) et quoi (expression de formule) provoque l'exception lors de la lecture du fichier de modèle.
