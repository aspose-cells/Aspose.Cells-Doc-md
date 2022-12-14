---
title: Public API Changements dans Aspose.Cells 8.2.1
type: docs
weight: 90
url: /fr/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.2.0 à 8.2.1, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la méthode getValidation() pour la classe Cell**
La validation des données est l'une des fonctionnalités que les concepteurs de feuilles de calcul utilisent pour empêcher les utilisateurs d'insérer des valeurs non valides dans une cellule particulière. Avec Aspose.Cells for Java 8.2.1, le API a exposé un mécanisme simple qui identifie si la validation des données a été appliquée sur une cellule. Utilisez la méthode getValidation de la classe Cell pour acquérir toute validation appliquée. S'il n'y a pas de validation, la méthode renvoie null. De même, vous pouvez utiliser la méthode getValidationInCell de la classe ValidationCollection pour acquérir la validation appliquée à n'importe quelle cellule en fournissant ses indices de ligne et de colonne.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Obtenez la validation appliquée sur un Cell](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) pour plus d'informations.

{{% /alert %}}
## **Ajout de la méthode getValidationValue() pour la classe Cell**
En plus de déterminer si la validation a été appliquée, vous pouvez également vérifier si une valeur donnée satisfait aux règles de validation des données pour une cellule particulière. Cette fonctionnalité est utile dans les scénarios où vous souhaitez vérifier si la valeur saisie dans la cellule satisfait les règles de validation des données à la volée. Le Aspose.Cells API a exposé la méthode getValidationValue pour la classe Cell. Si la valeur entrée dans une cellule ne satisfait pas les règles de validation des données, la méthode getValidationValue pour la classe Cell renvoie false.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Vérifiez que la valeur Cell satisfait aux règles de validation des données](/cells/fr/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Ajout d'une surcharge à la méthode Printer(PrinterSettings printerSettings) pour la classe WorkbookRender**
Vous pouvez utiliser la méthode surchargée pour rendre le classeur à l'imprimante via PrinterSettings.
